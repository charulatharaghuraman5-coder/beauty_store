import React, { useState, useRef, useEffect } from 'react'
import './AIChat.css'

function AIChat() {
  const [isOpen, setIsOpen] = useState(false)
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Hi! I\'m your beauty assistant. How can I help you today?' }
  ])
  const [input, setInput] = useState('')
  const [isTyping, setIsTyping] = useState(false)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const getAIResponse = (userMessage) => {
    const msg = userMessage.toLowerCase()
    
    if (msg.includes('makeup') || msg.includes('foundation') || msg.includes('lipstick')) {
      return 'Our makeup collection includes foundations, lipsticks, eyeshadows, and more! Check out our Makeup section for the latest products.'
    }
    if (msg.includes('skincare') || msg.includes('skin') || msg.includes('moisturizer')) {
      return 'We have amazing skincare products! Visit our Skincare section for moisturizers, serums, cleansers, and face masks.'
    }
    if (msg.includes('hair') || msg.includes('shampoo') || msg.includes('conditioner')) {
      return 'Transform your hair with our Haircare products! We offer shampoos, conditioners, hair masks, and styling products.'
    }
    if (msg.includes('sale') || msg.includes('discount') || msg.includes('offer')) {
      return 'Great news! Check out our Beauty Fashion Sale section for up to 30% OFF on selected products!'
    }
    if (msg.includes('luxe') || msg.includes('luxury') || msg.includes('premium')) {
      return 'Explore our Luxe Collection for premium luxury beauty products from top brands!'
    }
    if (msg.includes('order') || msg.includes('track') || msg.includes('delivery')) {
      return 'You can track your orders by clicking on the Orders icon in the header. Each order has a tracking ID for easy monitoring.'
    }
    if (msg.includes('payment') || msg.includes('pay') || msg.includes('razorpay')) {
      return 'We accept secure payments through Razorpay. You can pay using UPI, cards, net banking, or wallets.'
    }
    if (msg.includes('return') || msg.includes('refund') || msg.includes('exchange')) {
      return 'We offer easy returns within 7 days of delivery. Contact our support team for assistance with returns or exchanges.'
    }
    if (msg.includes('recommend') || msg.includes('suggest') || msg.includes('best')) {
      return 'I recommend checking out our bestsellers! Visit the All Products section and look for highly-rated items in your preferred category.'
    }
    if (msg.includes('brand') || msg.includes('brands')) {
      return 'We carry trusted beauty brands! Visit our Brands section to explore all available brands and their products.'
    }
    if (msg.includes('help') || msg.includes('support')) {
      return 'I\'m here to help! You can ask me about products, orders, payments, or anything else related to our beauty store.'
    }
    
    return 'I can help you with product recommendations, orders, payments, and more! Try asking about makeup, skincare, sales, or tracking your order.'
  }

  const handleSend = () => {
    if (!input.trim()) return

    const userMessage = { role: 'user', content: input }
    setMessages([...messages, userMessage])
    setInput('')
    setIsTyping(true)

    setTimeout(() => {
      const aiResponse = { role: 'assistant', content: getAIResponse(input) }
      setMessages(prev => [...prev, aiResponse])
      setIsTyping(false)
    }, 1000)
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <>
      <button className="ai-chat-button" onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? '✕' : '💬'}
      </button>

      {isOpen && (
        <div className="ai-chat-window">
          <div className="ai-chat-header">
            <h3>🤖 AI Beauty Assistant</h3>
          </div>
          <div className="ai-chat-messages">
            {messages.map((msg, idx) => (
              <div key={idx} className={`ai-message ${msg.role}`}>
                <div className="message-content">{msg.content}</div>
              </div>
            ))}
            {isTyping && (
              <div className="ai-message assistant">
                <div className="message-content typing">
                  <span></span><span></span><span></span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
          <div className="ai-chat-input">
            <input
              type="text"
              placeholder="Ask me anything..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
            />
            <button onClick={handleSend}>Send</button>
          </div>
        </div>
      )}
    </>
  )
}

export default AIChat
