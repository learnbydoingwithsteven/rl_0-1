// Utility functions for RL courses

// Format numbers with precision
function formatNumber(num, decimals = 4) {
    return Number(num).toFixed(decimals);
}

// Generate random number in range
function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
}

// Argmax function
function argmax(array) {
    return array.reduce((maxIdx, val, idx, arr) => val > arr[maxIdx] ? idx : maxIdx, 0);
}

// Softmax function
function softmax(array) {
    const max = Math.max(...array);
    const exps = array.map(x => Math.exp(x - max));
    const sum = exps.reduce((a, b) => a + b, 0);
    return exps.map(x => x / sum);
}

// Sample from probability distribution
function sampleFromDistribution(probs) {
    const rand = Math.random();
    let cumsum = 0;
    for (let i = 0; i < probs.length; i++) {
        cumsum += probs[i];
        if (rand < cumsum) return i;
    }
    return probs.length - 1;
}

// Create metric card
function createMetricCard(label, value, change = null) {
    const card = document.createElement('div');
    card.className = 'metric-card';
    
    const labelDiv = document.createElement('div');
    labelDiv.className = 'metric-label';
    labelDiv.textContent = label;
    
    const valueDiv = document.createElement('div');
    valueDiv.className = 'metric-value';
    valueDiv.textContent = value;
    
    card.appendChild(labelDiv);
    card.appendChild(valueDiv);
    
    if (change !== null) {
        const changeDiv = document.createElement('div');
        changeDiv.className = `metric-change ${change >= 0 ? 'positive' : 'negative'}`;
        changeDiv.textContent = `${change >= 0 ? '↑' : '↓'} ${Math.abs(change).toFixed(2)}%`;
        card.appendChild(changeDiv);
    }
    
    return card;
}

// Update metric card value
function updateMetricCard(card, value, change = null) {
    const valueDiv = card.querySelector('.metric-value');
    valueDiv.textContent = value;
    
    if (change !== null) {
        let changeDiv = card.querySelector('.metric-change');
        if (!changeDiv) {
            changeDiv = document.createElement('div');
            changeDiv.className = 'metric-change';
            card.appendChild(changeDiv);
        }
        changeDiv.className = `metric-change ${change >= 0 ? 'positive' : 'negative'}`;
        changeDiv.textContent = `${change >= 0 ? '↑' : '↓'} ${Math.abs(change).toFixed(2)}%`;
    }
}

// Create Plotly line chart
function createLineChart(divId, data, title, xLabel = 'Step', yLabel = 'Value') {
    const traces = data.map(d => ({
        x: d.x,
        y: d.y,
        name: d.name,
        type: 'scatter',
        mode: 'lines+markers',
        line: { width: 2 },
        marker: { size: 4 }
    }));
    
    const layout = {
        title: title,
        xaxis: { title: xLabel },
        yaxis: { title: yLabel },
        hovermode: 'closest',
        showlegend: true,
        legend: { x: 0, y: 1 }
    };
    
    Plotly.newPlot(divId, traces, layout, { responsive: true });
}

// Update Plotly chart
function updateLineChart(divId, data) {
    const update = {
        x: data.map(d => d.x),
        y: data.map(d => d.y)
    };
    
    Plotly.update(divId, update);
}

// Create heatmap
function createHeatmap(divId, zData, xLabels, yLabels, title) {
    const data = [{
        z: zData,
        x: xLabels,
        y: yLabels,
        type: 'heatmap',
        colorscale: 'Viridis'
    }];
    
    const layout = {
        title: title,
        xaxis: { title: 'X' },
        yaxis: { title: 'Y' }
    };
    
    Plotly.newPlot(divId, data, layout, { responsive: true });
}

// Create bar chart
function createBarChart(divId, xData, yData, title, xLabel = 'Category', yLabel = 'Value') {
    const data = [{
        x: xData,
        y: yData,
        type: 'bar',
        marker: {
            color: 'rgba(37, 99, 235, 0.7)',
            line: {
                color: 'rgba(37, 99, 235, 1)',
                width: 2
            }
        }
    }];
    
    const layout = {
        title: title,
        xaxis: { title: xLabel },
        yaxis: { title: yLabel }
    };
    
    Plotly.newPlot(divId, data, layout, { responsive: true });
}

// Sleep function for async delays
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Calculate moving average
function movingAverage(array, window) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        const start = Math.max(0, i - window + 1);
        const slice = array.slice(start, i + 1);
        const avg = slice.reduce((a, b) => a + b, 0) / slice.length;
        result.push(avg);
    }
    return result;
}

// Epsilon-greedy action selection
function epsilonGreedy(qValues, epsilon) {
    if (Math.random() < epsilon) {
        return Math.floor(Math.random() * qValues.length);
    }
    return argmax(qValues);
}

// Initialize Q-table
function initQTable(numStates, numActions, initialValue = 0) {
    return Array(numStates).fill(null).map(() => 
        Array(numActions).fill(initialValue)
    );
}

// Save data to localStorage
function saveToLocalStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
        return true;
    } catch (e) {
        console.error('Failed to save to localStorage:', e);
        return false;
    }
}

// Load data from localStorage
function loadFromLocalStorage(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (e) {
        console.error('Failed to load from localStorage:', e);
        return null;
    }
}

// Export data as JSON
function exportAsJSON(data, filename) {
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}

// Generate color palette
function generateColorPalette(n) {
    const colors = [];
    for (let i = 0; i < n; i++) {
        const hue = (i * 360 / n) % 360;
        colors.push(`hsl(${hue}, 70%, 50%)`);
    }
    return colors;
}

// Calculate statistics
function calculateStats(array) {
    const n = array.length;
    const mean = array.reduce((a, b) => a + b, 0) / n;
    const variance = array.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / n;
    const std = Math.sqrt(variance);
    const min = Math.min(...array);
    const max = Math.max(...array);
    
    return { mean, variance, std, min, max, n };
}
