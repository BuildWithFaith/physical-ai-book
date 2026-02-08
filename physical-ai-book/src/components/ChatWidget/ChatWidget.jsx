import React, { useState, useRef, useEffect } from 'react';
import { useColorMode } from '@docusaurus/theme-common';
import './ChatWidget.css';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const { colorMode } = useColorMode();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    const userMessage = { role: 'user', content: inputValue };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // In production, this should be the deployed backend URL
      // For development, we're assuming the backend is running on localhost:8000
      const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';

      const response = await fetch(`${BACKEND_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: inputValue,
          top_k: 5
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      const assistantMessage = {
        role: 'assistant',
        content: data.answer,
        sources: data.sources
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = {
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const closeChat = () => {
    setIsOpen(false);
  };

  return (
    <>
      {!isOpen ? (
        <button className={`chat-float-button chat-float-button-${colorMode}`} onClick={toggleChat}>
          💬
        </button>
      ) : null}

      {isOpen && (
        <div className={`chat-widget-container chat-widget-container-${colorMode}`}>
          <div className="chat-header">
            <span>Physical AI Tutor</span>
            <button className="chat-close-button" onClick={closeChat}>×</button>
          </div>

          <div className="chat-messages">
            {messages.map((msg, index) => (
              <div key={index} className={`message message-${msg.role}`}>
                <div className="message-content">{msg.content}</div>
                {msg.sources && msg.sources.length > 0 && (
                  <div className="message-sources">
                    Sources: {msg.sources.map(source => `${source.module}/${source.chapter}`).join(', ')}
                  </div>
                )}
              </div>
            ))}
            {isLoading && (
              <div className="message message-assistant">
                <div className="message-content">Thinking...</div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <form onSubmit={handleSubmit} className="chat-input-form">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask about Physical AI..."
              className="chat-input"
              disabled={isLoading}
            />
            <button type="submit" disabled={!inputValue.trim() || isLoading} className="chat-send-button">
              Send
            </button>
          </form>
        </div>
      )}
    </>
  );
};

export default ChatWidget;