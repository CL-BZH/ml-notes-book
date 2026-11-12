import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import minimize

class RobustThreeCoinEM:
    def __init__(self, n_iter=100, tol=1e-8, n_restarts=20):
        self.n_iter = n_iter
        self.tol = tol
        self.n_restarts = n_restarts
        self.history = []
    
    def simulate_data(self, n_samples, true_pi, true_p, true_q):
        """Simulate data from the three-coin model with known parameters"""
        np.random.seed(42)  # For reproducibility
        Y = np.zeros(n_samples, dtype=int)
        Z_true = np.zeros(n_samples, dtype=int)
        
        for i in range(n_samples):
            if np.random.random() < true_pi:
                Z_true[i] = 1
                Y[i] = 1 if np.random.random() < true_p else 0
            else:
                Z_true[i] = 0
                Y[i] = 1 if np.random.random() < true_q else 0
        
        return Y, Z_true
    
    def log_likelihood(self, Y, pi, p, q):
        """Compute log-likelihood of observed data"""
        n = len(Y)
        log_lik = 0
        
        for j in range(n):
            y_j = Y[j]
            term_B = pi * (p ** y_j) * ((1 - p) ** (1 - y_j))
            term_C = (1 - pi) * (q ** y_j) * ((1 - q) ** (1 - y_j))
            # Add small epsilon to avoid log(0)
            #log_lik += np.log(term_B + term_C + 1e-10)
            s = term_B + term_C
            log_lik += np.log(s) if s!=0 else np.log(1e-10)
        
        return log_lik
    
    def direct_mle(self, Y):
        """Try direct numerical optimization for comparison"""
        def neg_log_lik(params):
            pi, p, q = params
            # Enforce parameter constraints
            if not (0 <= pi <= 1 and 0 <= p <= 1 and 0 <= q <= 1):
                return 1e10
            return -self.log_likelihood(Y, pi, p, q)
        
        # Try multiple starting points
        best_ll = -np.inf
        best_params = None
        
        for _ in range(10):
            x0 = np.random.uniform(0.1, 0.9, 3)
            result = minimize(neg_log_lik, x0, method='L-BFGS-B', 
                            bounds=[(0.01, 0.99), (0.01, 0.99), (0.01, 0.99)])
            
            if result.success:
                ll = -result.fun
                if ll > best_ll:
                    best_ll = ll
                    best_params = result.x
        
        return best_params, best_ll
    
    def e_step(self, Y, pi, p, q):
        """E-step: Compute responsibilities"""
        n = len(Y)
        gamma = np.zeros(n)
        
        for j in range(n):
            y_j = Y[j]
            num_B = pi * (p ** y_j) * ((1 - p) ** (1 - y_j))
            num_C = (1 - pi) * (q ** y_j) * ((1 - q) ** (1 - y_j))
            gamma[j] = num_B / (num_B + num_C + 1e-10)  # Avoid division by zero
        
        return gamma
    
    def m_step(self, Y, gamma):
        """M-step: Update parameters"""
        
        # Update pi
        pi_new = np.clip(np.mean(gamma), 0.01, 0.99)
        
        # Update p with regularization
        sum_gamma = np.sum(gamma)
        if sum_gamma > 1e-10:
            p_new = np.clip(np.sum(gamma * Y) / sum_gamma, 0.01, 0.99)
        else:
            p_new = 0.5
        
        # Update q with regularization
        sum_one_minus_gamma = np.sum(1 - gamma)
        if sum_one_minus_gamma > 1e-10:
            q_new = np.clip(np.sum((1 - gamma) * Y) / sum_one_minus_gamma, 0.01, 0.99)
        else:
            q_new = 0.5
        
        return pi_new, p_new, q_new
    
    def single_em_run(self, Y, init_params, true_params=None, run_id=0):
        """Run EM from a single initialization"""
        pi, p, q = init_params
        history = []
        
        initial_ll = self.log_likelihood(Y, pi, p, q)
        history.append({'iteration': 0, 'pi': pi, 'p': p, 'q': q, 'log_likelihood': initial_ll})
        
        for i in range(self.n_iter):
            # E-step
            gamma = self.e_step(Y, pi, p, q)
            
            # M-step
            pi_new, p_new, q_new = self.m_step(Y, gamma)
            
            # Compute log-likelihood
            log_lik = self.log_likelihood(Y, pi_new, p_new, q_new)
            
            history.append({
                'iteration': i + 1,
                'pi': pi_new, 'p': p_new, 'q': q_new,
                'log_likelihood': log_lik,
                'gamma': gamma.copy()
            })
            
            # Check convergence
            param_change = np.abs(pi_new - pi) + np.abs(p_new - p) + np.abs(q_new - q)
            
            if param_change < self.tol:
                break
            
            pi, p, q = pi_new, p_new, q_new
        
        final_ll = history[-1]['log_likelihood']
        n_iterations = len(history) - 1
        
        if true_params is not None:
            true_pi, true_p, true_q = true_params
            error = (abs(pi - true_pi) + abs(p - true_p) + abs(q - true_q))
            print(f"Run {run_id:2d}: π={pi:.3f}({true_pi:.3f}) p={p:.3f}({true_p:.3f}) "
                  f"q={q:.3f}({true_q:.3f}) LL={final_ll:.3f} Error={error:.3f} "
                  f"Iters={n_iterations}")
        else:
            print(f"Run {run_id:2d}: π={pi:.3f} p={p:.3f} q={q:.3f} "
                  f"LL={final_ll:.3f} Iters={n_iterations}")
        
        return pi, p, q, final_ll, history
    
    def fit(self, Y, true_params=None):
        """Run EM with multiple restarts and careful initialization"""
        n = len(Y)
        obs_heads = np.mean(Y)
        
        print(f"Data: {n} observations, {obs_heads:.1%} heads")
        
        best_params = None
        best_ll = -np.inf
        best_history = None
        
        # Smart initializations based on data characteristics
        initializations = []
        
        # Strategy 1: Assume coins have different biases
        initializations.append((0.5, 0.7, 0.3))
        initializations.append((0.5, 0.3, 0.7))
        
        # Strategy 2: Assume one coin is fair
        initializations.append((0.5, 0.5, obs_heads))
        initializations.append((0.5, obs_heads, 0.5))
        
        # Strategy 3: Random initializations
        offset = len(initializations)
        for _ in range(self.n_restarts - offset):
            # Prefer initializations where p and q are different
            while True:
                p, q = np.random.uniform(0.1, 0.9, 2)
                if abs(p - q) > 0.2:  # Ensure coins are different
                    break
            pi = np.random.uniform(0.3, 0.7)
            initializations.append((pi, p, q))
        
        print("Running EM with multiple initializations:")
        print("Run  | π(est/true) p(est/true) q(est/true) Log-Lik Error Iters")
        print("-" * 80)
        
        for i, init_params in enumerate(initializations):
            pi, p, q, ll, history = self.single_em_run(Y, init_params, true_params, i)
            
            if ll > best_ll:
                best_ll = ll
                best_params = (pi, p, q)
                best_history = history
        
        self.history = best_history
        return best_params[0], best_params[1], best_params[2]
    
    def analyze_solution_quality(self, Y, true_params=None):
        """Analyze why EM might converge to poor solutions"""
        n = len(Y)
        obs_heads = np.mean(Y)
        
        print("\n=== SOLUTION QUALITY ANALYSIS ===")
        print(f"Dataset: {n} observations, {obs_heads:.1%} heads")
        
        if true_params is not None:
            true_pi, true_p, true_q = true_params
            print(f"True parameters: π={true_pi:.3f}, p={true_p:.3f}, q={true_q:.3f}")
            
            # Compute expected heads proportion
            expected_heads = true_pi * true_p + (1 - true_pi) * true_q
            print(f"Expected heads: {expected_heads:.3f} (observed: {obs_heads:.3f})")
        
        final_params = self.history[-1]
        pi, p, q = final_params['pi'], final_params['p'], final_params['q']
        print(f"EM solution: π={pi:.3f}, p={p:.3f}, q={q:.3f}")
        
        # Check identifiability
        if abs(p - q) < 0.1:
            print("⚠️ Warning: p and q are very similar - model may not be identifiable!")
            print("The problem is symmetric: swapping p and q with 1-π gives same likelihood")
        
        # Compare with direct MLE
        print("\nComparing with direct numerical optimization:")
        mle_params, mle_ll = self.direct_mle(Y)
        if mle_params is not None:
            print(f"Direct MLE: π={mle_params[0]:.3f}, p={mle_params[1]:.3f}, q={mle_params[2]:.3f}")
            print(f"EM likelihood: {final_params['log_likelihood']:.3f}, MLE likelihood: {mle_ll:.3f}")

# Demonstration with different dataset sizes
def demonstrate_em_behavior():
    print("=" * 80)
    print("DEMONSTRATING EM BEHAVIOR WITH DIFFERENT DATASET SIZES")
    print("=" * 80)
    
    TRUE_PARAMS = (0.6, 0.8, 0.3)  # π, p, q
    
    for n_samples in [10, 100, 1000]:
        print(f"\n{'='*50}")
        print(f"Dataset size: {n_samples} samples")
        print(f"{'='*50}")
        
        model = RobustThreeCoinEM(n_restarts=15)
        Y, Z_true = model.simulate_data(n_samples, *TRUE_PARAMS)
        
        # Run EM
        pi_est, p_est, q_est = model.fit(Y, TRUE_PARAMS)
        
        # Analyze results
        model.analyze_solution_quality(Y, TRUE_PARAMS)
        
        if n_samples == 10:
            print("\nSmall dataset challenges:")
            print("- High variance in parameter estimates")
            print("- Multiple local optima with similar likelihood")
            print("- Sensitive to initialization")
            print("- Model identifiability issues when p ≈ q")

# Run with original small dataset
def run_original_small_dataset():
    print("\n" + "=" * 80)
    print("ORIGINAL SMALL DATASET (10 OBSERVATIONS)")
    print("=" * 80)
    
    Y_original = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1])
    
    model = RobustThreeCoinEM(n_restarts=20)
    pi, p, q = model.fit(Y_original)
    
    print("\nFinal EM estimates:")
    print(f"π = {pi:.3f} (probability of selecting coin B)")
    print(f"p = {p:.3f} (probability of heads for coin B)")
    print(f"q = {q:.3f} (probability of heads for coin C)")
    
    model.analyze_solution_quality(Y_original)
    
    # Show what the model learned
    print("\nModel interpretation:")
    expected_heads = pi * p + (1 - pi) * q
    actual_heads = np.mean(Y_original)
    print(f"Expected heads: {expected_heads:.3f}, Actual heads: {actual_heads:.3f}")

if __name__ == "__main__":
    demonstrate_em_behavior()
    run_original_small_dataset()