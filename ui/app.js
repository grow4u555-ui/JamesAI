document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const terminal = document.getElementById('terminal');
    const statusText = document.getElementById('status-text');
    const reactor = document.getElementById('reactor');

    // Send Message Handler
    const handleSend = () => {
        const text = userInput.value.trim();
        if (!text) return;

        // Append to Terminal
        appendLog(`[USER] ${text}`);
        userInput.value = '';

        // Change JARVIS State to Thinking
        setJarvisState('THINKING...', 'thinking');

        // Simulate Multi-Agent Workflow
        setTimeout(() => {
            appendLog('[AGENT: Recon] Target analysis started...');
        }, 1000);

        setTimeout(() => {
            appendLog('[AGENT: Exploit] Generating POC script...');
        }, 2500);

        setTimeout(() => {
            appendLog('[JARVIS] Execution complete. Report generated.');
            setJarvisState('JARVIS SYSTEM ONLINE', 'online');
        }, 4000);
    };

    sendBtn.addEventListener('click', handleSend);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });

    function appendLog(msg) {
        const p = document.createElement('p');
        p.className = 'term-line';
        p.textContent = msg;
        terminal.appendChild(p);
        terminal.scrollTop = terminal.scrollHeight;
    }

    function setJarvisState(label, state) {
        statusText.textContent = label;
        if (state === 'thinking') {
            reactor.style.filter = 'drop-shadow(0 0 25px #ff0055)';
        } else {
            reactor.style.filter = 'drop-shadow(0 0 15px #00f3ff)';
        }
    }

    // Simulate Telemetry Fluctuations
    setInterval(() => {
        document.getElementById('cpu-val').textContent = `${Math.floor(20 + Math.random() * 15)}%`;
        document.getElementById('ram-val').textContent = `${Math.floor(40 + Math.random() * 5)}%`;
    }, 3000);
});
