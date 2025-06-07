
async function performOperation(operationType) {
    const inputText = document.getElementById('inputText').value;
    const outputResult = document.getElementById('outputResult');

    if (!inputText.trim()) {
        outputResult.textContent = "Please enter some text.";
        return;
    }

    try {
        const response = await fetch(`/${operationType}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText })
        });

        const data = await response.json();

        if (response.ok) {
            outputResult.textContent = data.result;
        } else {
            outputResult.textContent = `Error: ${data.error || 'Something went wrong.'}`;
            outputResult.style.color = 'red'; // Indicate error
        }
    } catch (error) {
        outputResult.textContent = `Network error: ${error.message}`;
        outputResult.style.color = 'red';
    } finally {
        // Reset color if it was changed due to error
        if (outputResult.style.color === 'red' && response.ok) {
            outputResult.style.color = 'inherit';
        }
    }
}