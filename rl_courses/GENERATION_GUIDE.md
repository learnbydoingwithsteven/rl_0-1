# Course Generation Guide

## Status: 2/100 Courses Created

### Completed Courses
- ✅ Course 1: Introduction to RL
- ✅ Course 2: Agent-Environment Interaction

### Remaining: 98 Courses

## Quick Generation Instructions

Each course needs 2 files:
1. `course_XXX_title/index.html` - Main course page
2. `course_XXX_title/script.js` - Interactive JavaScript

## Template Structure

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Course X: Title</title>
    <script src="https://cdn.plot.ly/plotly-2.26.0.min.js"></script>
    <link rel="stylesheet" href="../shared/styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🎯 Title</h1>
            <p class="course-meta">Course X of 100 | Level: [beginner/intermediate/advanced/expert]</p>
        </header>
        
        <nav class="course-nav">
            <button onclick="window.location.href='../course_XXX/index.html'">← Previous</button>
            <button onclick="window.location.href='../course_XXX/index.html'">Next →</button>
        </nav>
        
        <!-- Theory Section -->
        <!-- Controls Section -->
        <!-- Visualization Section -->
        <!-- Metrics Section -->
        <!-- Code Section -->
        <!-- Exercises Section -->
    </div>
    <script src="../shared/utils.js"></script>
    <script src="script.js"></script>
</body>
</html>
```

### JavaScript Template (script.js)
```javascript
// Course X: Title
let isRunning = false;
let data = { rewards: [], values: [] };

// Algorithm implementation
class Algorithm {
    constructor(config) {
        this.config = config;
    }
    step() {
        return Math.random();
    }
}

// UI setup
// Event listeners
// Chart initialization
```

## Courses to Generate (3-100)

### Beginner (3-30)
- Course 3: Markov Decision Processes
- Course 4: Rewards and Returns
- Course 5: Policies and Value Functions
- Course 6: Bellman Equations
- Course 7: Optimal Policies
- Course 8: Multi-Armed Bandits
- Course 9: Epsilon-Greedy
- Course 10: Upper Confidence Bound
- Course 11: Thompson Sampling
- Course 12: Contextual Bandits
- Course 13: Finite MDPs
- Course 14: Discount Factor
- Course 15: State Value Functions
- Course 16: Action Value Functions
- Course 17: Policy Evaluation
- Course 18: Policy Improvement
- Course 19: Policy Iteration
- Course 20: Value Iteration
- Course 21: Dynamic Programming
- Course 22: Generalized Policy Iteration
- Course 23: Asynchronous DP
- Course 24: GridWorld
- Course 25: Cliff Walking
- Course 26: Frozen Lake
- Course 27: Taxi Problem
- Course 28: Model-Based vs Model-Free
- Course 29: Exploration vs Exploitation
- Course 30: Beginner Review

### Intermediate (31-60)
[See courses_data.js for full list]

### Advanced (61-85)
[See courses_data.js for full list]

### Expert (86-100)
[See courses_data.js for full list]

## Generation Priority
1. Core algorithm courses (Q-Learning, SARSA, DQN, PPO, etc.)
2. Environment courses (GridWorld, Cliff Walking, etc.)
3. Theoretical courses (Bellman, Convergence, etc.)
4. Review courses (summaries at 30, 60, 85, 100)

## Features Each Course Must Have
✅ Interactive visualization with Plotly.js
✅ Real-time metrics display
✅ Adjustable parameters (learning rate, discount, etc.)
✅ Progress bar
✅ Start/Reset buttons
✅ Code implementation example
✅ 3 exercises
✅ Navigation to previous/next course
✅ Theory explanation
✅ Mathematical formulas where applicable

## File Naming Convention
- Directory: `course_XXX_title_in_lowercase_with_underscores`
- HTML: `index.html`
- JavaScript: `script.js`

Example: `course_039_q_learning/index.html`
