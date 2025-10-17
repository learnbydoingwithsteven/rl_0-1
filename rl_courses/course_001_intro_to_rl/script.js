// Course 1: Introduction to RL - Interactive Script

let isRunning = false;
let currentEpisode = 0;
let rewardHistory = [];
let cumulativeRewards = [];

// Simple RL Agent
class SimpleRLAgent {
    constructor() {
        this.totalReward = 0;
        this.episodeRewards = [];
        this.successCount = 0;
    }
    
    takeAction() {
        // Random action (50-50 chance)
        return Math.random() > 0.5 ? 'right' : 'left';
    }
    
    receiveReward(reward) {
        this.totalReward += reward;
        this.episodeRewards.push(reward);
        if (reward > 0) this.successCount++;
    }
    
    getAverageReward() {
        if (this.episodeRewards.length === 0) return 0;
        return this.totalReward / this.episodeRewards.length;
    }
    
    getSuccessRate() {
        if (this.episodeRewards.length === 0) return 0;
        return (this.successCount / this.episodeRewards.length) * 100;
    }
}

// Simple Environment
class SimpleEnvironment {
    step(action) {
        // Right action gives +1 reward, left gives -1
        const reward = action === 'right' ? 1 : -1;
        const done = true; // Episode ends after one step
        return { reward, done };
    }
}

// Initialize
const agent = new SimpleRLAgent();
const env = new SimpleEnvironment();

// UI Elements
const numEpisodesSlider = document.getElementById('numEpisodes');
const numEpisodesValue = document.getElementById('numEpisodesValue');
const speedSlider = document.getElementById('speed');
const speedValue = document.getElementById('speedValue');
const startBtn = document.getElementById('startBtn');
const resetBtn = document.getElementById('resetBtn');
const progressBar = document.getElementById('progressBar');
const metricsPanel = document.getElementById('metricsPanel');

// Update slider values
numEpisodesSlider.addEventListener('input', (e) => {
    numEpisodesValue.textContent = e.target.value;
});

speedSlider.addEventListener('input', (e) => {
    speedValue.textContent = e.target.value;
});

// Initialize metrics
function initializeMetrics() {
    metricsPanel.innerHTML = '';
    
    const metrics = [
        { label: 'Episodes Completed', value: '0', id: 'episodes' },
        { label: 'Total Reward', value: '0', id: 'totalReward' },
        { label: 'Average Reward', value: '0.00', id: 'avgReward' },
        { label: 'Success Rate', value: '0%', id: 'successRate' }
    ];
    
    metrics.forEach(metric => {
        const card = createMetricCard(metric.label, metric.value);
        card.id = metric.id;
        metricsPanel.appendChild(card);
    });
}

// Update metrics
function updateMetrics() {
    updateMetricCard(document.getElementById('episodes'), currentEpisode);
    updateMetricCard(document.getElementById('totalReward'), agent.totalReward);
    updateMetricCard(document.getElementById('avgReward'), formatNumber(agent.getAverageReward(), 2));
    updateMetricCard(document.getElementById('successRate'), `${formatNumber(agent.getSuccessRate(), 1)}%`);
}

// Initialize chart
function initializeChart() {
    const data = [{
        x: [],
        y: [],
        name: 'Episode Reward',
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: '#2563eb', width: 2 },
        marker: { size: 6 }
    }, {
        x: [],
        y: [],
        name: 'Cumulative Reward',
        type: 'scatter',
        mode: 'lines',
        line: { color: '#10b981', width: 2 },
        yaxis: 'y2'
    }];
    
    const layout = {
        title: 'Agent Learning Progress',
        xaxis: { title: 'Episode' },
        yaxis: { title: 'Episode Reward' },
        yaxis2: {
            title: 'Cumulative Reward',
            overlaying: 'y',
            side: 'right'
        },
        showlegend: true,
        legend: { x: 0.1, y: 1 }
    };
    
    Plotly.newPlot('rewardChart', data, layout, { responsive: true });
}

// Update chart
function updateChart() {
    const episodes = Array.from({ length: currentEpisode }, (_, i) => i + 1);
    
    Plotly.update('rewardChart', {
        x: [episodes, episodes],
        y: [rewardHistory, cumulativeRewards]
    }, {}, [0, 1]);
}

// Run single episode
async function runEpisode() {
    // Agent takes action
    const action = agent.takeAction();
    
    // Environment responds
    const { reward, done } = env.step(action);
    
    // Agent receives reward
    agent.receiveReward(reward);
    
    // Record history
    rewardHistory.push(reward);
    const cumulative = cumulativeRewards.length > 0 
        ? cumulativeRewards[cumulativeRewards.length - 1] + reward 
        : reward;
    cumulativeRewards.push(cumulative);
    
    currentEpisode++;
    
    // Update UI
    const progress = (currentEpisode / parseInt(numEpisodesSlider.value)) * 100;
    progressBar.style.width = `${progress}%`;
    progressBar.textContent = `${Math.round(progress)}%`;
    
    updateMetrics();
    updateChart();
}

// Start learning
async function startLearning() {
    if (isRunning) return;
    
    isRunning = true;
    startBtn.disabled = true;
    startBtn.textContent = '⏸ Running...';
    
    const totalEpisodes = parseInt(numEpisodesSlider.value);
    const speed = parseInt(speedSlider.value);
    const delay = 1000 / speed; // Convert speed to delay
    
    while (currentEpisode < totalEpisodes && isRunning) {
        await runEpisode();
        await sleep(delay);
    }
    
    isRunning = false;
    startBtn.disabled = false;
    startBtn.textContent = '▶ Start Learning';
    
    // Show completion message
    if (currentEpisode >= totalEpisodes) {
        const avgReward = agent.getAverageReward();
        const successRate = agent.getSuccessRate();
        
        const message = document.createElement('div');
        message.className = 'alert success';
        message.innerHTML = `
            <strong>Learning Complete!</strong><br>
            Completed ${totalEpisodes} episodes.<br>
            Average Reward: ${formatNumber(avgReward, 2)}<br>
            Success Rate: ${formatNumber(successRate, 1)}%<br>
            <em>Note: This agent uses random actions. In future courses, you'll learn how agents can improve their performance!</em>
        `;
        
        document.querySelector('.visualization').appendChild(message);
    }
}

// Reset
function reset() {
    isRunning = false;
    currentEpisode = 0;
    rewardHistory = [];
    cumulativeRewards = [];
    
    // Reset agent
    agent.totalReward = 0;
    agent.episodeRewards = [];
    agent.successCount = 0;
    
    // Reset UI
    progressBar.style.width = '0%';
    progressBar.textContent = '0%';
    startBtn.disabled = false;
    startBtn.textContent = '▶ Start Learning';
    
    // Remove completion message if exists
    const alerts = document.querySelectorAll('.alert.success');
    alerts.forEach(alert => alert.remove());
    
    initializeMetrics();
    initializeChart();
}

// Event listeners
startBtn.addEventListener('click', startLearning);
resetBtn.addEventListener('click', reset);

// Navigation
document.getElementById('nextCourse').addEventListener('click', () => {
    window.location.href = '../course_002_agent_environment/index.html';
});

// Initialize on load
window.addEventListener('load', () => {
    initializeMetrics();
    initializeChart();
});
