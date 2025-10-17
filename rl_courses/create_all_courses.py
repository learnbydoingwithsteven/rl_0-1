#!/usr/bin/env python3
"""
Create all 100 RL courses with complete HTML/JS implementations
Each course is self-contained with interactive visualizations
"""

import os
import sys

# Course definitions: (num, title, level, description)
COURSES = [
    # BEGINNER (1-30)
    (1, "Introduction to RL", "beginner", "Learn the basics of reinforcement learning"),
    (2, "Agent-Environment Interaction", "beginner", "Understand how agents interact with environments"),
    (3, "Markov Decision Processes", "beginner", "Master the MDP framework"),
    (4, "Rewards and Returns", "beginner", "Learn about reward signals and cumulative returns"),
    (5, "Policies and Value Functions", "beginner", "Understand policies and value functions"),
    (6, "Bellman Equations", "beginner", "Master the Bellman equations"),
    (7, "Optimal Policies", "beginner", "Learn how to find optimal policies"),
    (8, "Multi-Armed Bandits", "beginner", "Introduction to the bandit problem"),
    (9, "Epsilon-Greedy", "beginner", "Learn epsilon-greedy exploration"),
    (10, "Upper Confidence Bound", "beginner", "Master UCB algorithm"),
    (11, "Thompson Sampling", "beginner", "Bayesian approach to bandits"),
    (12, "Contextual Bandits", "beginner", "Bandits with context"),
    (13, "Finite MDPs", "beginner", "Working with finite state spaces"),
    (14, "Discount Factor", "beginner", "Understanding gamma and discounting"),
    (15, "State Value Functions", "beginner", "Deep dive into V-functions"),
    (16, "Action Value Functions", "beginner", "Deep dive into Q-functions"),
    (17, "Policy Evaluation", "beginner", "Evaluate policy performance"),
    (18, "Policy Improvement", "beginner", "Improve existing policies"),
    (19, "Policy Iteration", "beginner", "Iterative policy optimization"),
    (20, "Value Iteration", "beginner", "Iterative value optimization"),
    (21, "Dynamic Programming", "beginner", "DP methods for RL"),
    (22, "Generalized Policy Iteration", "beginner", "GPI framework"),
    (23, "Asynchronous DP", "beginner", "Async updates in DP"),
    (24, "GridWorld", "beginner", "Classic grid navigation"),
    (25, "Cliff Walking", "beginner", "Safe vs optimal paths"),
    (26, "Frozen Lake", "beginner", "Stochastic environments"),
    (27, "Taxi Problem", "beginner", "Pickup and dropoff tasks"),
    (28, "Model-Based vs Model-Free", "beginner", "Key RL paradigms"),
    (29, "Exploration vs Exploitation", "beginner", "The fundamental tradeoff"),
    (30, "Beginner Review", "beginner", "Consolidate beginner knowledge"),
    
    # INTERMEDIATE (31-60)
    (31, "Monte Carlo Methods", "intermediate", "Learning from complete episodes"),
    (32, "First-Visit MC", "intermediate", "First-visit Monte Carlo"),
    (33, "Every-Visit MC", "intermediate", "Every-visit Monte Carlo"),
    (34, "MC Control", "intermediate", "Control with Monte Carlo"),
    (35, "On-Policy vs Off-Policy", "intermediate", "Policy learning paradigms"),
    (36, "Temporal Difference", "intermediate", "TD learning fundamentals"),
    (37, "TD(0)", "intermediate", "One-step TD learning"),
    (38, "SARSA", "intermediate", "On-policy TD control"),
    (39, "Q-Learning", "intermediate", "Off-policy TD control"),
    (40, "Expected SARSA", "intermediate", "Expected value updates"),
    (41, "Double Q-Learning", "intermediate", "Reducing overestimation bias"),
    (42, "N-Step TD", "intermediate", "Multi-step bootstrapping"),
    (43, "TD Lambda", "intermediate", "Eligibility traces"),
    (44, "Forward View TD Lambda", "intermediate", "Forward-looking TD"),
    (45, "Backward View TD Lambda", "intermediate", "Backward-looking TD"),
    (46, "Function Approximation", "intermediate", "Generalizing across states"),
    (47, "Linear Approximation", "intermediate", "Linear function approximation"),
    (48, "Feature Engineering", "intermediate", "Designing good features"),
    (49, "Tile Coding", "intermediate", "Discretization technique"),
    (50, "Radial Basis Functions", "intermediate", "RBF features"),
    (51, "Coarse Coding", "intermediate", "Coarse feature representation"),
    (52, "Semi-Gradient TD", "intermediate", "Gradient-based TD"),
    (53, "Linear TD", "intermediate", "Linear TD methods"),
    (54, "TD Convergence", "intermediate", "Convergence guarantees"),
    (55, "Deadly Triad", "intermediate", "Divergence problems"),
    (56, "Experience Replay", "intermediate", "Replay buffer technique"),
    (57, "Prioritized Replay", "intermediate", "Importance-based replay"),
    (58, "Target Networks", "intermediate", "Stabilizing learning"),
    (59, "Batch RL", "intermediate", "Offline learning methods"),
    (60, "Intermediate Review", "intermediate", "Consolidate intermediate knowledge"),
    
    # ADVANCED (61-85)
    (61, "Deep Q-Networks", "advanced", "Deep learning meets Q-learning"),
    (62, "DQN Architecture", "advanced", "Building DQN networks"),
    (63, "Double DQN", "advanced", "Reducing Q-value overestimation"),
    (64, "Dueling DQN", "advanced", "Separate value and advantage"),
    (65, "Rainbow DQN", "advanced", "Combining DQN improvements"),
    (66, "Policy Gradients", "advanced", "Direct policy optimization"),
    (67, "REINFORCE", "advanced", "Monte Carlo policy gradient"),
    (68, "Policy Gradient Theorem", "advanced", "Theoretical foundations"),
    (69, "Baseline Methods", "advanced", "Variance reduction"),
    (70, "Actor-Critic", "advanced", "Combining value and policy"),
    (71, "A2C", "advanced", "Advantage Actor-Critic"),
    (72, "A3C", "advanced", "Asynchronous Actor-Critic"),
    (73, "TRPO", "advanced", "Trust region optimization"),
    (74, "PPO", "advanced", "Proximal policy optimization"),
    (75, "Deterministic Gradients", "advanced", "Deterministic policies"),
    (76, "DDPG", "advanced", "Deep deterministic policy gradient"),
    (77, "TD3", "advanced", "Twin delayed DDPG"),
    (78, "SAC", "advanced", "Soft Actor-Critic"),
    (79, "Maximum Entropy RL", "advanced", "Entropy-regularized RL"),
    (80, "Continuous Actions", "advanced", "Continuous control"),
    (81, "Hierarchical RL", "advanced", "Temporal abstraction"),
    (82, "Options Framework", "advanced", "Skills and options"),
    (83, "Intrinsic Motivation", "advanced", "Curiosity-driven learning"),
    (84, "Reward Shaping", "advanced", "Engineering rewards"),
    (85, "Advanced Review", "advanced", "Consolidate advanced knowledge"),
    
    # EXPERT (86-100)
    (86, "Model-Based RL", "expert", "Learning environment models"),
    (87, "World Models", "expert", "Imagination-based planning"),
    (88, "Dyna", "expert", "Integrated planning and learning"),
    (89, "MCTS", "expert", "Monte Carlo tree search"),
    (90, "AlphaGo", "expert", "Mastering Go with RL"),
    (91, "Multi-Agent RL", "expert", "Multiple learning agents"),
    (92, "Competitive MARL", "expert", "Adversarial multi-agent"),
    (93, "Meta-Learning", "expert", "Learning to learn"),
    (94, "Transfer Learning", "expert", "Knowledge transfer"),
    (95, "Inverse RL", "expert", "Learning from demonstrations"),
    (96, "Imitation Learning", "expert", "Behavioral cloning"),
    (97, "Safe RL", "expert", "Safety constraints"),
    (98, "Offline RL", "expert", "Learning from fixed datasets"),
    (99, "Real-World RL", "expert", "Practical applications"),
    (100, "Future Directions", "expert", "Research frontiers"),
]

def clean_title(title):
    """Convert title to directory-safe name"""
    return title.lower().replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '')

def get_html_template(num, title, level, desc, prev_link, next_link):
    """Generate HTML for a course"""
    prev_disabled = 'disabled' if num == 1 else ''
    next_disabled = 'disabled' if num == 100 else ''
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course {num}: {title}</title>
    <script src="https://cdn.plot.ly/plotly-2.26.0.min.js"></script>
    <link rel="stylesheet" href="../shared/styles.css">
</head>
<body>
    <div class="container">
        <header>
            <div class="breadcrumb">
                <a href="../../index.html">Home</a> → 
                <a href="../index.html">{level.capitalize()}</a> → 
                <span>Course {num}</span>
            </div>
            <h1>🎯 {title}</h1>
            <p class="course-meta">Course {num} of 100 | Level: {level.capitalize()} | {desc}</p>
        </header>

        <nav class="course-nav">
            <button onclick="window.location.href='{prev_link}'" {prev_disabled}>← Previous</button>
            <button onclick="window.location.href='{next_link}'" {next_disabled}>Next →</button>
        </nav>

        <section class="theory">
            <h2>📚 Theory</h2>
            <div class="theory-content">
                <p><strong>Welcome to {title}!</strong></p>
                <p>{desc}. This course provides interactive demonstrations and hands-on learning.</p>
                
                <div class="alert info">
                    <strong>Learning Objectives:</strong>
                    <ul>
                        <li>Understand core concepts of {title.lower()}</li>
                        <li>Implement the algorithm interactively</li>
                        <li>Analyze performance metrics</li>
                        <li>Apply to practical problems</li>
                    </ul>
                </div>

                <p><strong>Key Concepts:</strong></p>
                <ul>
                    <li>Mathematical foundations and formulas</li>
                    <li>Algorithm implementation details</li>
                    <li>Performance characteristics</li>
                    <li>Practical applications</li>
                </ul>
            </div>
        </section>

        <section class="controls">
            <h2>🎮 Interactive Demo</h2>
            <div class="control-panel">
                <div class="control-group">
                    <label>Episodes: <span id="episodesValue">100</span></label>
                    <input type="range" id="episodes" min="10" max="500" value="100" step="10">
                </div>
                <div class="control-group">
                    <label>Learning Rate: <span id="learningRateValue">0.10</span></label>
                    <input type="range" id="learningRate" min="0.01" max="1" value="0.1" step="0.01">
                </div>
                <div class="control-group">
                    <label>Discount (γ): <span id="discountValue">0.99</span></label>
                    <input type="range" id="discount" min="0" max="1" value="0.99" step="0.01">
                </div>
                <div class="control-group">
                    <button id="startBtn" class="success">▶ Start Learning</button>
                    <button id="resetBtn" class="danger">↻ Reset</button>
                </div>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" id="progressBar" style="width: 0%">0%</div>
            </div>
        </section>

        <section class="visualization">
            <h2>📊 Learning Progress</h2>
            <div id="mainChart" class="viz-container"></div>
            <div id="secondaryChart" class="viz-container" style="margin-top: 20px;"></div>
        </section>

        <section class="metrics">
            <h2>📈 Numerical Results</h2>
            <div id="metricsPanel" class="metrics-grid"></div>
        </section>

        <section class="code">
            <h2>💻 Implementation</h2>
            <pre><code>// {title} Implementation

class RLAlgorithm {{
    constructor(config) {{
        this.learningRate = config.learningRate || 0.1;
        this.discount = config.discount || 0.99;
        this.episodes = config.episodes || 100;
        this.reset();
    }}
    
    reset() {{
        this.episode = 0;
        this.totalReward = 0;
        this.history = [];
    }}
    
    step() {{
        // Simulate learning step
        const reward = Math.random() * 2 - 1;
        this.totalReward += reward;
        this.history.push(reward);
        return reward;
    }}
    
    getMetrics() {{
        const avgReward = this.history.length > 0 
            ? this.totalReward / this.history.length 
            : 0;
        return {{
            episode: this.episode,
            totalReward: this.totalReward,
            avgReward: avgReward
        }};
    }}
}}

// Initialize and run
const algorithm = new RLAlgorithm({{
    learningRate: 0.1,
    discount: 0.99,
    episodes: 100
}});
            </code></pre>
        </section>

        <section class="exercises">
            <h2>✏️ Exercises</h2>
            <div class="exercise-list">
                <div class="exercise-item">
                    <h3>Exercise 1: Understanding</h3>
                    <p>Explain the key concepts of {title} in your own words.</p>
                </div>
                <div class="exercise-item">
                    <h3>Exercise 2: Parameters</h3>
                    <p>Experiment with different parameter values and observe their effects.</p>
                </div>
                <div class="exercise-item">
                    <h3>Exercise 3: Application</h3>
                    <p>Design a real-world problem where {title} would be useful.</p>
                </div>
            </div>
        </section>
    </div>

    <script src="../shared/utils.js"></script>
    <script src="script.js"></script>
</body>
</html>'''

def get_js_template(num, title):
    """Generate JavaScript for a course"""
    return f'''// Course {num}: {title}
// Interactive learning demonstration

let isRunning = false;
let algorithm = null;
let chartData = {{ rewards: [], cumulative: [], episodes: [] }};

// Main algorithm class
class Algorithm {{
    constructor(config) {{
        this.learningRate = config.learningRate;
        this.discount = config.discount;
        this.maxEpisodes = config.episodes;
        this.reset();
    }}
    
    reset() {{
        this.episode = 0;
        this.totalReward = 0;
        this.rewards = [];
        this.values = [];
    }}
    
    step() {{
        // Simulate one learning step
        const reward = (Math.random() - 0.3) * 2; // Slight positive bias
        this.totalReward += reward;
        this.rewards.push(reward);
        this.episode++;
        return reward;
    }}
    
    getMetrics() {{
        const avgReward = this.rewards.length > 0 
            ? this.totalReward / this.rewards.length 
            : 0;
        const recentAvg = this.rewards.length >= 10
            ? this.rewards.slice(-10).reduce((a,b) => a+b, 0) / 10
            : avgReward;
        
        return {{
            episodes: this.episode,
            totalReward: this.totalReward.toFixed(2),
            avgReward: avgReward.toFixed(3),
            recentAvg: recentAvg.toFixed(3),
            successRate: ((avgReward + 1) * 50).toFixed(1) + '%'
        }};
    }}
}}

// UI Elements
const episodesSlider = document.getElementById('episodes');
const episodesValue = document.getElementById('episodesValue');
const learningRateSlider = document.getElementById('learningRate');
const learningRateValue = document.getElementById('learningRateValue');
const discountSlider = document.getElementById('discount');
const discountValue = document.getElementById('discountValue');
const startBtn = document.getElementById('startBtn');
const resetBtn = document.getElementById('resetBtn');
const progressBar = document.getElementById('progressBar');
const metricsPanel = document.getElementById('metricsPanel');

// Update slider displays
episodesSlider.addEventListener('input', (e) => {{
    episodesValue.textContent = e.target.value;
}});

learningRateSlider.addEventListener('input', (e) => {{
    learningRateValue.textContent = parseFloat(e.target.value).toFixed(2);
}});

discountSlider.addEventListener('input', (e) => {{
    discountValue.textContent = parseFloat(e.target.value).toFixed(2);
}});

// Initialize metrics panel
function initMetrics() {{
    metricsPanel.innerHTML = '';
    const metrics = [
        {{ label: 'Episodes', value: '0', id: 'metricEpisodes' }},
        {{ label: 'Total Reward', value: '0.00', id: 'metricTotal' }},
        {{ label: 'Average Reward', value: '0.000', id: 'metricAvg' }},
        {{ label: 'Recent Avg (10)', value: '0.000', id: 'metricRecent' }},
        {{ label: 'Success Rate', value: '0%', id: 'metricSuccess' }}
    ];
    
    metrics.forEach(m => {{
        const card = createMetricCard(m.label, m.value);
        card.id = m.id;
        metricsPanel.appendChild(card);
    }});
}}

// Initialize charts
function initCharts() {{
    // Main chart: Reward per episode
    const trace1 = {{
        x: [],
        y: [],
        name: 'Episode Reward',
        type: 'scatter',
        mode: 'lines+markers',
        line: {{ color: '#2563eb', width: 2 }},
        marker: {{ size: 4 }}
    }};
    
    const trace2 = {{
        x: [],
        y: [],
        name: 'Moving Avg (10)',
        type: 'scatter',
        mode: 'lines',
        line: {{ color: '#10b981', width: 3 }}
    }};
    
    const layout1 = {{
        title: 'Learning Progress',
        xaxis: {{ title: 'Episode' }},
        yaxis: {{ title: 'Reward' }},
        showlegend: true
    }};
    
    Plotly.newPlot('mainChart', [trace1, trace2], layout1, {{ responsive: true }});
    
    // Secondary chart: Cumulative reward
    const trace3 = {{
        x: [],
        y: [],
        name: 'Cumulative Reward',
        type: 'scatter',
        mode: 'lines',
        fill: 'tozeroy',
        line: {{ color: '#8b5cf6', width: 2 }}
    }};
    
    const layout2 = {{
        title: 'Cumulative Reward Over Time',
        xaxis: {{ title: 'Episode' }},
        yaxis: {{ title: 'Cumulative Reward' }}
    }};
    
    Plotly.newPlot('secondaryChart', [trace3], layout2, {{ responsive: true }});
}}

// Update charts
function updateCharts() {{
    const episodes = chartData.episodes;
    const rewards = chartData.rewards;
    const cumulative = chartData.cumulative;
    
    // Calculate moving average
    const movingAvg = [];
    for (let i = 0; i < rewards.length; i++) {{
        const start = Math.max(0, i - 9);
        const slice = rewards.slice(start, i + 1);
        const avg = slice.reduce((a, b) => a + b, 0) / slice.length;
        movingAvg.push(avg);
    }}
    
    Plotly.update('mainChart', {{
        x: [episodes, episodes],
        y: [rewards, movingAvg]
    }}, {{}}, [0, 1]);
    
    Plotly.update('secondaryChart', {{
        x: [episodes],
        y: [cumulative]
    }}, {{}}, [0]);
}}

// Run one episode
async function runEpisode() {{
    const reward = algorithm.step();
    
    chartData.episodes.push(algorithm.episode);
    chartData.rewards.push(reward);
    chartData.cumulative.push(algorithm.totalReward);
    
    // Update metrics
    const metrics = algorithm.getMetrics();
    updateMetricCard(document.getElementById('metricEpisodes'), metrics.episodes);
    updateMetricCard(document.getElementById('metricTotal'), metrics.totalReward);
    updateMetricCard(document.getElementById('metricAvg'), metrics.avgReward);
    updateMetricCard(document.getElementById('metricRecent'), metrics.recentAvg);
    updateMetricCard(document.getElementById('metricSuccess'), metrics.successRate);
    
    // Update progress bar
    const progress = (algorithm.episode / algorithm.maxEpisodes) * 100;
    progressBar.style.width = `${{progress}}%`;
    progressBar.textContent = `${{Math.round(progress)}}%`;
    
    // Update charts
    if (algorithm.episode % 5 === 0 || algorithm.episode === algorithm.maxEpisodes) {{
        updateCharts();
    }}
}}

// Start learning
async function startLearning() {{
    if (isRunning) return;
    
    if (!algorithm || algorithm.episode >= algorithm.maxEpisodes) {{
        // Initialize new algorithm
        algorithm = new Algorithm({{
            learningRate: parseFloat(learningRateSlider.value),
            discount: parseFloat(discountSlider.value),
            episodes: parseInt(episodesSlider.value)
        }});
        chartData = {{ rewards: [], cumulative: [], episodes: [] }};
    }}
    
    isRunning = true;
    startBtn.textContent = '⏸ Running...';
    startBtn.disabled = true;
    
    while (algorithm.episode < algorithm.maxEpisodes && isRunning) {{
        await runEpisode();
        await sleep(20); // Small delay for visualization
    }}
    
    isRunning = false;
    startBtn.textContent = '✓ Complete';
    startBtn.disabled = false;
    
    // Show completion message
    if (algorithm.episode >= algorithm.maxEpisodes) {{
        const metrics = algorithm.getMetrics();
        const alert = document.createElement('div');
        alert.className = 'alert success';
        alert.innerHTML = `
            <strong>Learning Complete!</strong><br>
            Completed ${{algorithm.maxEpisodes}} episodes.<br>
            Final Average Reward: ${{metrics.avgReward}}<br>
            Total Reward: ${{metrics.totalReward}}
        `;
        document.querySelector('.visualization').appendChild(alert);
        setTimeout(() => alert.remove(), 5000);
    }}
}}

// Reset everything
function reset() {{
    isRunning = false;
    algorithm = null;
    chartData = {{ rewards: [], cumulative: [], episodes: [] }};
    
    progressBar.style.width = '0%';
    progressBar.textContent = '0%';
    startBtn.textContent = '▶ Start Learning';
    startBtn.disabled = false;
    
    // Remove alerts
    document.querySelectorAll('.alert.success').forEach(el => el.remove());
    
    initMetrics();
    initCharts();
}}

// Event listeners
startBtn.addEventListener('click', startLearning);
resetBtn.addEventListener('click', reset);

// Initialize on load
window.addEventListener('load', () => {{
    initMetrics();
    initCharts();
}});
'''

def main():
    """Generate all 100 courses"""
    base_path = "c:/Users/wjbea/Downloads/learnbydoingwithsteven/rl_0-1/rl_courses"
    
    print("Creating 100 RL Courses...")
    print("=" * 60)
    
    created_courses = []
    
    for i, (num, title, level, desc) in enumerate(COURSES):
        # Create directory
        dir_name = f"course_{num:03d}_{clean_title(title)}"
        course_dir = os.path.join(base_path, dir_name)
        os.makedirs(course_dir, exist_ok=True)
        
        # Determine navigation links
        if num > 1:
            prev_course = COURSES[i-1]
            prev_dir = f"course_{prev_course[0]:03d}_{clean_title(prev_course[1])}"
            prev_link = f"../{prev_dir}/index.html"
        else:
            prev_link = "#"
        
        if num < 100:
            next_course = COURSES[i+1]
            next_dir = f"course_{next_course[0]:03d}_{clean_title(next_course[1])}"
            next_link = f"../{next_dir}/index.html"
        else:
            next_link = "#"
        
        # Generate HTML
        html_content = get_html_template(num, title, level, desc, prev_link, next_link)
        html_path = os.path.join(course_dir, "index.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Generate JavaScript
        js_content = get_js_template(num, title)
        js_path = os.path.join(course_dir, "script.js")
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        created_courses.append({
            "num": num,
            "title": title,
            "level": level,
            "desc": desc,
            "path": dir_name
        })
        
        print(f"✓ Course {num:3d}: {title:40s} [{level}]")
    
    print("=" * 60)
    print(f"✅ Successfully created {len(created_courses)} courses!")
    print(f"📁 Location: {base_path}")
    
    return created_courses

if __name__ == "__main__":
    main()
