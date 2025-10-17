// Course 72: A3C
// Interactive learning demonstration

let isRunning = false;
let algorithm = null;
let chartData = { rewards: [], cumulative: [], episodes: [] };

// Main algorithm class
class Algorithm {
    constructor(config) {
        this.learningRate = config.learningRate;
        this.discount = config.discount;
        this.maxEpisodes = config.episodes;
        this.reset();
    }
    
    reset() {
        this.episode = 0;
        this.totalReward = 0;
        this.rewards = [];
        this.values = [];
    }
    
    step() {
        // Simulate one learning step
        const reward = (Math.random() - 0.3) * 2; // Slight positive bias
        this.totalReward += reward;
        this.rewards.push(reward);
        this.episode++;
        return reward;
    }
    
    getMetrics() {
        const avgReward = this.rewards.length > 0 
            ? this.totalReward / this.rewards.length 
            : 0;
        const recentAvg = this.rewards.length >= 10
            ? this.rewards.slice(-10).reduce((a,b) => a+b, 0) / 10
            : avgReward;
        
        return {
            episodes: this.episode,
            totalReward: this.totalReward.toFixed(2),
            avgReward: avgReward.toFixed(3),
            recentAvg: recentAvg.toFixed(3),
            successRate: ((avgReward + 1) * 50).toFixed(1) + '%'
        };
    }
}

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
episodesSlider.addEventListener('input', (e) => {
    episodesValue.textContent = e.target.value;
});

learningRateSlider.addEventListener('input', (e) => {
    learningRateValue.textContent = parseFloat(e.target.value).toFixed(2);
});

discountSlider.addEventListener('input', (e) => {
    discountValue.textContent = parseFloat(e.target.value).toFixed(2);
});

// Initialize metrics panel
function initMetrics() {
    metricsPanel.innerHTML = '';
    const metrics = [
        { label: 'Episodes', value: '0', id: 'metricEpisodes' },
        { label: 'Total Reward', value: '0.00', id: 'metricTotal' },
        { label: 'Average Reward', value: '0.000', id: 'metricAvg' },
        { label: 'Recent Avg (10)', value: '0.000', id: 'metricRecent' },
        { label: 'Success Rate', value: '0%', id: 'metricSuccess' }
    ];
    
    metrics.forEach(m => {
        const card = createMetricCard(m.label, m.value);
        card.id = m.id;
        metricsPanel.appendChild(card);
    });
}

// Initialize charts
function initCharts() {
    // Main chart: Reward per episode
    const trace1 = {
        x: [],
        y: [],
        name: 'Episode Reward',
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: '#2563eb', width: 2 },
        marker: { size: 4 }
    };
    
    const trace2 = {
        x: [],
        y: [],
        name: 'Moving Avg (10)',
        type: 'scatter',
        mode: 'lines',
        line: { color: '#10b981', width: 3 }
    };
    
    const layout1 = {
        title: 'Learning Progress',
        xaxis: { title: 'Episode' },
        yaxis: { title: 'Reward' },
        showlegend: true
    };
    
    Plotly.newPlot('mainChart', [trace1, trace2], layout1, { responsive: true });
    
    // Secondary chart: Cumulative reward
    const trace3 = {
        x: [],
        y: [],
        name: 'Cumulative Reward',
        type: 'scatter',
        mode: 'lines',
        fill: 'tozeroy',
        line: { color: '#8b5cf6', width: 2 }
    };
    
    const layout2 = {
        title: 'Cumulative Reward Over Time',
        xaxis: { title: 'Episode' },
        yaxis: { title: 'Cumulative Reward' }
    };
    
    Plotly.newPlot('secondaryChart', [trace3], layout2, { responsive: true });
}

// Update charts
function updateCharts() {
    const episodes = chartData.episodes;
    const rewards = chartData.rewards;
    const cumulative = chartData.cumulative;
    
    // Calculate moving average
    const movingAvg = [];
    for (let i = 0; i < rewards.length; i++) {
        const start = Math.max(0, i - 9);
        const slice = rewards.slice(start, i + 1);
        const avg = slice.reduce((a, b) => a + b, 0) / slice.length;
        movingAvg.push(avg);
    }
    
    Plotly.update('mainChart', {
        x: [episodes, episodes],
        y: [rewards, movingAvg]
    }, {}, [0, 1]);
    
    Plotly.update('secondaryChart', {
        x: [episodes],
        y: [cumulative]
    }, {}, [0]);
}

// Run one episode
async function runEpisode() {
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
    progressBar.style.width = `${progress}%`;
    progressBar.textContent = `${Math.round(progress)}%`;
    
    // Update charts
    if (algorithm.episode % 5 === 0 || algorithm.episode === algorithm.maxEpisodes) {
        updateCharts();
    }
}

// Start learning
async function startLearning() {
    if (isRunning) return;
    
    if (!algorithm || algorithm.episode >= algorithm.maxEpisodes) {
        // Initialize new algorithm
        algorithm = new Algorithm({
            learningRate: parseFloat(learningRateSlider.value),
            discount: parseFloat(discountSlider.value),
            episodes: parseInt(episodesSlider.value)
        });
        chartData = { rewards: [], cumulative: [], episodes: [] };
    }
    
    isRunning = true;
    startBtn.textContent = '⏸ Running...';
    startBtn.disabled = true;
    
    while (algorithm.episode < algorithm.maxEpisodes && isRunning) {
        await runEpisode();
        await sleep(20); // Small delay for visualization
    }
    
    isRunning = false;
    startBtn.textContent = '✓ Complete';
    startBtn.disabled = false;
    
    // Show completion message
    if (algorithm.episode >= algorithm.maxEpisodes) {
        const metrics = algorithm.getMetrics();
        const alert = document.createElement('div');
        alert.className = 'alert success';
        alert.innerHTML = `
            <strong>Learning Complete!</strong><br>
            Completed ${algorithm.maxEpisodes} episodes.<br>
            Final Average Reward: ${metrics.avgReward}<br>
            Total Reward: ${metrics.totalReward}
        `;
        document.querySelector('.visualization').appendChild(alert);
        setTimeout(() => alert.remove(), 5000);
    }
}

// Reset everything
function reset() {
    isRunning = false;
    algorithm = null;
    chartData = { rewards: [], cumulative: [], episodes: [] };
    
    progressBar.style.width = '0%';
    progressBar.textContent = '0%';
    startBtn.textContent = '▶ Start Learning';
    startBtn.disabled = false;
    
    // Remove alerts
    document.querySelectorAll('.alert.success').forEach(el => el.remove());
    
    initMetrics();
    initCharts();
}

// Event listeners
startBtn.addEventListener('click', startLearning);
resetBtn.addEventListener('click', reset);

// Initialize on load
window.addEventListener('load', () => {
    initMetrics();
    initCharts();
});
