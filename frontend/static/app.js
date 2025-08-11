document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const messageForm = document.getElementById('message-form');
    const userInput = document.getElementById('user-input');
    
    // Get the current host and port from the browser
    const API_BASE_URL = window.location.origin;
    const API_URL = `${API_BASE_URL}/query`;
    
    console.log('API URL:', API_URL);

    // Add a message to the chat
    function addMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        
        // Format the message (convert newlines to <br> and preserve other HTML)
        const formattedMessage = message.replace(/\n/g, '<br>');
        messageDiv.innerHTML = formattedMessage;
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return messageDiv;
    }

    // Show typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = `
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        `;
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        return typingDiv;
    }

    // Remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    // Handle form submission
    messageForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const userMessage = userInput.value.trim();
        if (!userMessage) return;
        
        // Add user message to chat
        addMessage(userMessage, true);
        userInput.value = '';
        userInput.disabled = true;
        
        // Show typing indicator
        const typingIndicator = showTypingIndicator();
        
        try {
            console.log('Sending request to:', API_URL);
            console.log('Request payload:', { question: userMessage });
            
            // Send message to FastAPI backend
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    question: userMessage
                }),
                credentials: 'same-origin'  // Include cookies if any
            });
            
            console.log('Response status:', response.status);
            
            if (!response.ok) {
                const errorText = await response.text();
                console.error('Error response:', errorText);
                throw new Error(`Server responded with status: ${response.status}`);
            }
            
            const data = await response.json();
            console.log('Response data:', data);
            
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add bot response to chat
            if (data && data.answer) {
                addMessage(data.answer);
            } else if (data && data.error) {
                addMessage(`Error: ${data.error}`);
            } else {
                addMessage("I received your message but couldn't process it. Here's what I got: " + JSON.stringify(data));
            }
            
        } catch (error) {
            console.error('Error:', error);
            removeTypingIndicator();
            addMessage(`Sorry, I encountered an error: ${error.message}. Please check the console for more details.`);
        } finally {
            userInput.disabled = false;
            userInput.focus();
        }
    });

    // Allow sending message with Enter key
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            messageForm.dispatchEvent(new Event('submit'));
        }
    });

    // Focus the input field on page load
    userInput.focus();
});
