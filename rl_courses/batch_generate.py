"""
Batch Generate 100 RL Courses
Creates all course directories with HTML, JS, and interactive visualizations
"""

import os
import json

# Define all 100 courses
COURSES = [
    # Beginner (1-30)
    (1, "Introduction to Reinforcement Learning", "beginner", ["basics", "agent", "environment"]),
    (2, "Agent-Environment Interaction", "beginner", ["states", "actions", "rewards"]),
    (3, "Markov Decision Processes", "beginner", ["MDP", "states", "transitions"]),
    (4, "Rewards and Returns", "beginner", ["rewards", "returns", "cumulative"]),
    (5, "Policies and Value Functions", "beginner", ["policy", "value", "function"]),
    (6, "Bellman Equations", "beginner", ["bellman", "equations", "recursion"]),
    (7, "Optimal Policies", "beginner", ["optimal", "policy", "best"]),
    (8, "Multi-Armed Bandits Intro", "beginner", ["bandits", "exploration", "exploitation"]),
    (9, "Epsilon-Greedy Strategy", "beginner", ["epsilon", "greedy", "exploration"]),
    (10, "Upper Confidence Bound", "beginner", ["UCB", "confidence", "bound"]),
    (11, "Thompson Sampling", "beginner", ["thompson", "sampling", "bayesian"]),
    (12, "Contextual Bandits", "beginner", ["contextual", "bandits", "features"]),
    (13, "Finite MDPs", "beginner", ["finite", "MDP", "states"]),
    (14, "Discount Factor", "beginner", ["discount", "gamma", "future"]),
    (15, "State Value Functions", "beginner", ["state", "value", "V"]),
    (16, "Action Value Functions", "beginner", ["action", "value", "Q"]),
    (17, "Policy Evaluation", "beginner", ["evaluation", "policy", "prediction"]),
    (18, "Policy Improvement", "beginner", ["improvement", "policy", "better"]),
    (19, "Policy Iteration", "beginner", ["iteration", "policy", "convergence"]),
    (20, "Value Iteration", "beginner", ["value", "iteration", "optimal"]),
    (21, "Dynamic Programming Basics", "beginner", ["DP", "dynamic", "programming"]),
    (22, "Generalized Policy Iteration", "beginner", ["GPI", "generalized", "iteration"]),
    (23, "Asynchronous DP", "beginner", ["asynchronous", "DP", "updates"]),
    (24, "GridWorld Environment", "beginner", ["gridworld", "grid", "navigation"]),
    (25, "Cliff Walking Problem", "beginner", ["cliff", "walking", "safety"]),
    (26, "Frozen Lake Problem", "beginner", ["frozen", "lake", "stochastic"]),
    (27, "Taxi Problem", "beginner", ["taxi", "pickup", "dropoff"]),
    (28, "Model-Based vs Model-Free", "beginner", ["model", "based", "free"]),
    (29, "Exploration vs Exploitation", "beginner", ["exploration", "exploitation", "tradeoff"]),
    (30, "Beginner Review", "beginner", ["review", "practice", "summary"]),
    
    # Intermediate (31-60)
    (31, "Monte Carlo Methods", "intermediate", ["monte", "carlo", "sampling"]),
    (32, "First-Visit Monte Carlo", "intermediate", ["first", "visit", "MC"]),
    (33, "Every-Visit Monte Carlo", "intermediate", ["every", "visit", "MC"]),
    (34, "Monte Carlo Control", "intermediate", ["MC", "control", "improvement"]),
    (35, "On-Policy vs Off-Policy", "intermediate", ["on", "off", "policy"]),
    (36, "Temporal Difference Learning", "intermediate", ["TD", "temporal", "difference"]),
    (37, "TD(0) Algorithm", "intermediate", ["TD0", "one", "step"]),
    (38, "SARSA Algorithm", "intermediate", ["SARSA", "on", "policy"]),
    (39, "Q-Learning Algorithm", "intermediate", ["Q", "learning", "off"]),
    (40, "Expected SARSA", "intermediate", ["expected", "SARSA", "average"]),
    (41, "Double Q-Learning", "intermediate", ["double", "Q", "bias"]),
    (42, "N-Step TD Methods", "intermediate", ["n", "step", "TD"]),
    (43, "TD Lambda", "intermediate", ["TD", "lambda", "traces"]),
    (44, "Forward View TD Lambda", "intermediate", ["forward", "TD", "lambda"]),
    (45, "Backward View TD Lambda", "intermediate", ["backward", "TD", "lambda"]),
    (46, "Function Approximation", "intermediate", ["function", "approximation", "generalization"]),
    (47, "Linear Function Approximation", "intermediate", ["linear", "function", "features"]),
    (48, "Feature Engineering", "intermediate", ["features", "engineering", "design"]),
    (49, "Tile Coding", "intermediate", ["tile", "coding", "discretization"]),
    (50, "Radial Basis Functions", "intermediate", ["RBF", "radial", "basis"]),
    (51, "Coarse Coding", "intermediate", ["coarse", "coding", "features"]),
    (52, "Semi-Gradient TD", "intermediate", ["semi", "gradient", "TD"]),
    (53, "Linear TD Approximation", "intermediate", ["linear", "TD", "approximation"]),
    (54, "Convergence of TD", "intermediate", ["convergence", "TD", "guarantees"]),
    (55, "Deadly Triad Problem", "intermediate", ["deadly", "triad", "divergence"]),
    (56, "Experience Replay", "intermediate", ["experience", "replay", "buffer"]),
    (57, "Prioritized Replay", "intermediate", ["prioritized", "replay", "importance"]),
    (58, "Target Networks", "intermediate", ["target", "network", "stability"]),
    (59, "Batch RL Methods", "intermediate", ["batch", "RL", "offline"]),
    (60, "Intermediate Review", "intermediate", ["review", "practice", "summary"]),
    
    # Advanced (61-85)
    (61, "Deep Q-Networks", "advanced", ["DQN", "deep", "Q"]),
    (62, "DQN Architecture", "advanced", ["DQN", "architecture", "training"]),
    (63, "Double DQN", "advanced", ["double", "DQN", "overestimation"]),
    (64, "Dueling DQN", "advanced", ["dueling", "DQN", "advantage"]),
    (65, "Rainbow DQN", "advanced", ["rainbow", "DQN", "combined"]),
    (66, "Policy Gradient Methods", "advanced", ["policy", "gradient", "direct"]),
    (67, "REINFORCE Algorithm", "advanced", ["REINFORCE", "monte", "carlo"]),
    (68, "Policy Gradient Theorem", "advanced", ["theorem", "gradient", "proof"]),
    (69, "Baseline Methods", "advanced", ["baseline", "variance", "reduction"]),
    (70, "Actor-Critic Methods", "advanced", ["actor", "critic", "combined"]),
    (71, "Advantage Actor-Critic", "advanced", ["A2C", "advantage", "actor"]),
    (72, "A3C Algorithm", "advanced", ["A3C", "asynchronous", "parallel"]),
    (73, "Trust Region Policy Optimization", "advanced", ["TRPO", "trust", "region"]),
    (74, "Proximal Policy Optimization", "advanced", ["PPO", "proximal", "clipping"]),
    (75, "Deterministic Policy Gradients", "advanced", ["deterministic", "policy", "continuous"]),
    (76, "Deep Deterministic Policy Gradient", "advanced", ["DDPG", "continuous", "control"]),
    (77, "Twin Delayed DDPG", "advanced", ["TD3", "twin", "delayed"]),
    (78, "Soft Actor-Critic", "advanced", ["SAC", "soft", "entropy"]),
    (79, "Maximum Entropy RL", "advanced", ["entropy", "maximum", "exploration"]),
    (80, "Continuous Action Spaces", "advanced", ["continuous", "actions", "control"]),
    (81, "Hierarchical RL", "advanced", ["hierarchical", "options", "skills"]),
    (82, "Options Framework", "advanced", ["options", "temporal", "abstraction"]),
    (83, "Intrinsic Motivation", "advanced", ["intrinsic", "curiosity", "exploration"]),
    (84, "Reward Shaping", "advanced", ["reward", "shaping", "engineering"]),
    (85, "Advanced Review", "advanced", ["review", "practice", "summary"]),
    
    # Expert (86-100)
    (86, "Model-Based RL", "expert", ["model", "based", "planning"]),
    (87, "World Models", "expert", ["world", "models", "imagination"]),
    (88, "Dyna Architecture", "expert", ["dyna", "planning", "learning"]),
    (89, "Monte Carlo Tree Search", "expert", ["MCTS", "tree", "search"]),
    (90, "AlphaGo and AlphaZero", "expert", ["alphago", "alphazero", "games"]),
    (91, "Multi-Agent RL", "expert", ["multi", "agent", "cooperative"]),
    (92, "Competitive Multi-Agent RL", "expert", ["competitive", "adversarial", "games"]),
    (93, "Meta-Learning", "expert", ["meta", "learning", "adaptation"]),
    (94, "Transfer Learning in RL", "expert", ["transfer", "learning", "reuse"]),
    (95, "Inverse RL", "expert", ["inverse", "IRL", "imitation"]),
    (96, "Imitation Learning", "expert", ["imitation", "learning", "demonstration"]),
    (97, "Safe RL", "expert", ["safe", "constrained", "safety"]),
    (98, "Offline RL", "expert", ["offline", "batch", "data"]),
    (99, "Real-World Applications", "expert", ["applications", "robotics", "real"]),
    (100, "Future Directions", "expert", ["future", "research", "frontiers"]),
]

def clean_title(title):
    """Clean title for directory name"""
    return title.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')

def create_course_files(num, title, level, keywords):
    """Create HTML and JS files for a course"""
    
    dir_name = f"course_{num:03d}_{clean_title(title)}"
    base_path = "c:/Users/wjbea/Downloads/learnbydoingwithsteven/rl_0-1/rl_courses"
    course_path = os.path.join(base_path, dir_name)
    
    # Create directory
    os.makedirs(course_path, exist_ok=True)
    
    # Determine navigation
    prev_num = num - 1 if num > 1 else 0
    next_num = num + 1 if num < 100 else 0
    
    prev_title = COURSES[prev_num-1][1] if prev_num > 0 else ""
    next_title = COURSES[next_num-1][1] if next_num > 0 and next_num <= 100 else ""
    
    prev_link = f"../course_{prev_num:03d}_{clean_title(prev_title)}/index.html" if prev_num > 0 else "#"
    next_link = f"../course_{next_num:03d}_{clean_title(next_title)}/index.html" if 0 < next_num <= 100 else "#"
    
    # Create HTML file
    html_path = os.path.join(course_path, "index.html")
    js_path = os.path.join(course_path, "script.js")
    
    return dir_name, html_path, js_path, prev_link, next_link

# Generate course manifest
manifest = []
for course in COURSES:
    num, title, level, keywords = course
    dir_name, _, _, _, _ = create_course_files(num, title, level, keywords)
    manifest.append({
        "num": num,
        "title": title,
        "level": level,
        "keywords": keywords,
        "path": dir_name
    })

# Save manifest
manifest_path = "c:/Users/wjbea/Downloads/learnbydoingwithsteven/rl_0-1/rl_courses/course_manifest.json"
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"Generated manifest for {len(COURSES)} courses")
print(f"Saved to: {manifest_path}")
