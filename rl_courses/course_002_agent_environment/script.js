// Course 2: Agent-Environment Interaction

let isRunning = false;
let step = 0;
let data = { states: [], actions: [], rewards: [], cumulative: [] };

class Agent {
    selectAction(state) {
        return Math.random() > 0.5 ? 1 : 0; // 1=right, 0=left
    }
}

class Environment {
    constructor() {
        this.state = 0;
        this.maxState = 10;
    }
    
    step(action) {
        const reward = action === 1 ? 1 : -0.5;
        this.state = (this.state + action) % this.maxState;
        return { state: this.state, reward: reward };
    }
    
    reset() {
        this.state = 0;
    }
}

const agent = new Agent();
const env = new Environment();

// UI Elements
const stepsSlider = document.getElementById('steps');
const stepsValue = document.getElementById('stepsValue');
const speedSlider = document.getElementById('speed');
const speedValue = document.getElementById('speedValue');
const startBtn = document.getElementById('startBtn');
const resetBtn = document.getElementById('resetBtn');
const progressBar = document.getElementById('progressBar');
const metricsPanel = document.getElementById('metricsPanel');

stepsSlider.addEventListener('input', (e) => {
    stepsValue.textContent = e.target.value;
});

speedSlider.addEventListener('input', (e) => {
    speedValue.textContent = e.target.value;
});

function initMetrics() {
    metricsPanel.innerHTML = '';
    const metrics = [
        { label: 'Steps', value: '0', id: 'metricSteps' },
        { label: 'Total Reward', value: '0.00', id: 'metricTotal' },
        { label: 'Avg Reward', value: '0.00', id: 'metricAvg' },
        { label: 'Right Actions', value: '0%', id: 'metricRight' }
    ];
    
    metrics.forEach(m => {
        const card = createMetricCard(m.label, m.value);
        card.id = m.id;
        metricsPanel.appendChild(card);
    });
}

function initCharts() {
    const trace1 = {
        x: [],
        y: [],
        name: 'Reward',
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: '#2563eb', width: 2 }
    };
    
    const layout1 = {
        title: 'Rewards Over Time',
        xaxis: { title: 'Step' },
        yaxis: { title: 'Reward' }
    };
    
    Plotly.newPlot('mainChart', [trace1], layout1, { responsive: true });
    
    const trace2 = {
        x: [],
        y: [],
        name: 'State',
        type: 'scatter',
        mode: 'lines',
        fill: 'tozeroy',
        line: { color: '#10b981', width: 2 }
    };
    
    const layout2 = {
        title: 'State Trajectory',
        xaxis: { title: 'Step' },
        yaxis: { title: 'State' }
    };
    
    Plotly.newPlot('secondaryChart', [trace2], layout2, { responsive: true });
}

function updateCharts() {
    const steps = Array.from({ length: data.rewards.length }, (_, i) => i + 1);
    
    Plotly.update('mainChart', {
        x: [steps],
        y: [data.rewards]
    }, {}, [0]);
    
    Plotly.update('secondaryChart', {
        x: [steps],
        y: [data.states]
    }, {}, [0]);
}

async function runStep() {
    const action = agent.selectAction(env.state);
    const { state, reward } = env.step(action);
    
    data.states.push(state);
    data.actions.push(action);
    data.rewards.push(reward);
    data.cumulative.push(data.cumulative.length > 0 ? data.cumulative[data.cumulative.length - 1] + reward : reward);
    
    step++;
    
    const totalReward = data.cumulative[data.cumulative.length - 1];
    const avgReward = totalReward / step;
    const rightActions = data.actions.filter(a => a === 1).length;
    const rightPct = (rightActions / step * 100).toFixed(1);
    
    updateMetricCard(document.getElementById('metricSteps'), step);
    updateMetricCard(document.getElementById('metricTotal'), formatNumber(totalReward, 2));
    updateMetricCard(document.getElementById('metricAvg'), formatNumber(avgReward, 2));
    updateMetricCard(document.getElementById('metricRight'), rightPct + '%');
    
    const progress = (step / parseInt(stepsSlider.value)) * 100;
    progressBar.style.width = `${progress}%`;
    progressBar.textContent = `${Math.round(progress)}%`;
    
    if (step % 5 === 0) {
        updateCharts();
    }
}

async function start() {
    if (isRunning) return;
    isRunning = true;
    startBtn.disabled = true;
    
    const maxSteps = parseInt(stepsSlider.value);
    const speed = parseInt(speedSlider.value);
    const delay = 1000 / speed;
    
    while (step < maxSteps && isRunning) {
        await runStep();
        await sleep(delay);
    }
    
    updateCharts();
    isRunning = false;
    startBtn.disabled = false;
}

function reset() {
    isRunning = false;
    step = 0;
    data = { states: [], actions: [], rewards: [], cumulative: [] };
    env.reset();
    
    progressBar.style.width = '0%';
    progressBar.textContent = '0%';
    startBtn.disabled = false;
    
    initMetrics();
    initCharts();
}

startBtn.addEventListener('click', start);
resetBtn.addEventListener('click', reset);

window.addEventListener('load', () => {
    initMetrics();
    initCharts();
});
