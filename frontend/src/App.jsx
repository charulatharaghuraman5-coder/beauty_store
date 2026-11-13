import React, { useState, useEffect } from 'react'
import './App.css'

const API = window.location.pathname.includes('/codeeditor/default/ports/8000') 
  ? '/codeeditor/default/ports/8000/api' 
  : '/api'

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [username, setUsername] = useState('')
  const [showLoginForm, setShowLoginForm] = useState(true)
  const [loginUsername, setLoginUsername] = useState('')
  const [loginPassword, setLoginPassword] = useState('')
  const [view, setView] = useState('home')
  const [products, setProducts] = useState([])
  const [allProducts, setAllProducts] = useState([])
  const [categories, setCategories] = useState([])
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [searchTerm, setSearchTerm] = useState('')
  const [cart, setCart] = useState([])
  const [wishlist, setWishlist] = useState([])
  const [orders, setOrders] = useState([])
  const [showCart, setShowCart] = useState(false)
  const [showWishlist, setShowWishlist] = useState(false)
  const [selectedProduct, setSelectedProduct] = useState(null)
  const [showCheckout, setShowCheckout] = useState(false)
  const [showPayment, setShowPayment] = useState(false)
  const [showQRCode, setShowQRCode] = useState(false)
  const [showOrders, setShowOrders] = useState(false)
  const [shippingDetails, setShippingDetails] = useState({
    name: '',
    address: '',
    mobile: '',
    pincode: ''
  })
  const [selectedPayment, setSelectedPayment] = useState('')

  useEffect(() => {
    fetchProducts()
    fetchCategories()
  }, [])

  const fetchProducts = async (category = null, search = null) => {
    try {
      let url = `${API}/products/?limit=1000`
      if (category) url += `&category=${encodeURIComponent(category)}`
      if (search) url += `&search=${encodeURIComponent(search)}`
      console.log('Fetching:', url)
      const res = await fetch(url)
      console.log('Status:', res.status)
      if (res.ok) {
        const data = await res.json()
        console.log('Products:', data.length)
        setProducts(data)
        if (!category && !search) setAllProducts(data)
      } else {
        console.error('API failed:', res.status)
      }
    } catch (e) { 
      console.error('Fetch error:', e)
    }
  }

  const fetchCategories = async () => {
    const res = await fetch(`${API}/products/categories/all`)
    if (res.ok) setCategories((await res.json()).categories)
  }

  const viewProductDetails = async (productId) => {
    try {
      const res = await fetch(`${API}/products/${productId}`)
      if (res.ok) {
        const product = await res.json()
        setSelectedProduct(product)
      }
    } catch (e) { console.error('Error:', e) }
  }

  const addToCart = (product) => {
    const isSale = product.price < 600
    const salePrice = isSale ? product.price * 0.7 : product.price
    const existing = cart.find(item => item.id === product.id)
    if (existing) {
      setCart(cart.map(item => item.id === product.id ? {...item, quantity: item.quantity + 1} : item))
    } else {
      setCart([...cart, {...product, quantity: 1, isSale, salePrice, originalPrice: product.price}])
    }
  }

  const removeFromCart = (productId) => {
    setCart(cart.filter(item => item.id !== productId))
  }

  const toggleWishlist = (product) => {
    const inWishlist = wishlist.some(w => w.id === product.id)
    if (inWishlist) {
      setWishlist(wishlist.filter(w => w.id !== product.id))
    } else {
      setWishlist([...wishlist, product])
    }
  }

  const handleSearch = (e) => {
    const term = e.target.value
    setSearchTerm(term)
    fetchProducts(selectedCategory, term)
  }

  const handleCategoryFilter = (cat) => {
    setSelectedCategory(cat)
    if (cat) {
      setProducts(allProducts.filter(p => p.category === cat))
    } else {
      setProducts(allProducts)
    }
  }

  const cartTotal = cart.reduce((sum, item) => sum + ((item.salePrice || item.price) * item.quantity), 0)

  const handleCheckout = () => {
    if (cart.length > 0) {
      setShowCart(false)
      setShowCheckout(true)
    }
  }

  const handlePlaceOrder = async (e) => {
    e.preventDefault()
    setShowCheckout(false)
    
    // Check if Razorpay is loaded
    if (typeof window.Razorpay === 'undefined') {
      alert('Razorpay SDK not loaded. Please refresh the page and try again.')
      setShowCheckout(true)
      return
    }
    
    // Directly initiate Razorpay payment
    try {
      const response = await fetch(`${API}/payment/create-order`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount: cartTotal })
      })
      
      if (!response.ok) {
        throw new Error('Failed to create order')
      }
      
      const orderData = await response.json()
      console.log('Order created:', orderData)
      
      const options = {
        key: orderData.key,
        amount: orderData.amount,
        currency: orderData.currency,
        name: 'Beauty Store',
        description: 'Purchase from Beauty Store',
        order_id: orderData.order_id,
        prefill: {
          name: shippingDetails.name,
          contact: shippingDetails.mobile
        },
        method: {
          upi: true,
          card: true,
          netbanking: true,
          wallet: true
        },
        handler: function (response) {
          const newOrder = {
            id: Date.now(),
            items: [...cart],
            total: cartTotal,
            shippingDetails: {...shippingDetails},
            paymentMethod: 'Razorpay',
            paymentId: response.razorpay_payment_id,
            date: new Date().toLocaleDateString(),
            status: 'Order Placed',
            trackingId: `TRK${Date.now()}`,
            trackingHistory: [
              { status: 'Order Placed', date: new Date().toLocaleString(), description: 'Your order has been placed successfully' }
            ]
          }
          setOrders([...orders, newOrder])
          alert(`Payment Successful!\n\nOrder ID: ${newOrder.id}\nTracking ID: ${newOrder.trackingId}\nPayment ID: ${response.razorpay_payment_id}\nTotal: ₹${cartTotal.toFixed(2)}`)
          setCart([])
          setShippingDetails({ name: '', address: '', mobile: '', pincode: '' })
        },
        modal: {
          ondismiss: function() {
            alert('Payment cancelled. Please try again.')
            setShowCheckout(true)
          }
        },
        theme: {
          color: '#ff1493'
        }
      }
      
      console.log('Opening Razorpay with options:', options)
      const razorpay = new window.Razorpay(options)
      
      razorpay.on('payment.failed', function (response) {
        console.error('Payment failed:', response.error)
        alert(`Payment Failed!\n\nReason: ${response.error.description}\nPlease try again.`)
        setShowCheckout(true)
      })
      
      razorpay.open()
    } catch (error) {
      console.error('Payment error:', error)
      alert('Error initiating payment. Please try again.')
      setShowCheckout(true)
    }
  }



  const handlePaymentComplete = () => {
    const newOrder = {
      id: Date.now(),
      items: [...cart],
      total: cartTotal,
      shippingDetails: {...shippingDetails},
      paymentMethod: selectedPayment,
      date: new Date().toLocaleDateString(),
      status: 'Processing',
      trackingId: `TRK${Date.now()}`
    }
    setOrders([...orders, newOrder])
    alert(`Order placed successfully!\nOrder ID: ${newOrder.id}\nTracking ID: ${newOrder.trackingId}\nTotal: ₹${cartTotal.toFixed(2)}`)
    setCart([])
    setShowQRCode(false)
    setShippingDetails({ name: '', address: '', mobile: '', pincode: '' })
    setSelectedPayment('')
  }

  const handleLogin = (e) => {
    e.preventDefault()
    
    // Validate username (only alphabets)
    if (!/^[a-zA-Z]+$/.test(loginUsername)) {
      alert('Username must contain only alphabets')
      return
    }
    
    // Validate password (min 12 chars, uppercase, lowercase, number, special char)
    if (loginPassword.length < 12) {
      alert('Password must be at least 12 characters long')
      return
    }
    if (!/[a-z]/.test(loginPassword)) {
      alert('Password must contain at least one lowercase letter')
      return
    }
    if (!/[A-Z]/.test(loginPassword)) {
      alert('Password must contain at least one uppercase letter')
      return
    }
    if (!/[0-9]/.test(loginPassword)) {
      alert('Password must contain at least one number')
      return
    }
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(loginPassword)) {
      alert('Password must contain at least one special character')
      return
    }
    
    setUsername(loginUsername)
    setIsLoggedIn(true)
    setShowLoginForm(false)
  }

  if (!isLoggedIn) {
    return (
      <div className="login-container">
        <div className="login-box">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="120" height="120" style={{margin: '0 auto 20px', display: 'block'}}>
            <defs>
              <linearGradient id="pinkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style={{stopColor:'#ff1493',stopOpacity:1}} />
                <stop offset="50%" style={{stopColor:'#ff69b4',stopOpacity:1}} />
                <stop offset="100%" style={{stopColor:'#ff1493',stopOpacity:1}} />
              </linearGradient>
              <linearGradient id="goldShine" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style={{stopColor:'#ffd700',stopOpacity:1}} />
                <stop offset="50%" style={{stopColor:'#ffed4e',stopOpacity:1}} />
                <stop offset="100%" style={{stopColor:'#ff8c00',stopOpacity:1}} />
              </linearGradient>
              <radialGradient id="bgGlow">
                <stop offset="0%" style={{stopColor:'#ff69b4',stopOpacity:0.4}} />
                <stop offset="100%" style={{stopColor:'#ff1493',stopOpacity:0}} />
              </radialGradient>
              <filter id="glow">
                <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
                <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
            </defs>
            <circle cx="100" cy="100" r="95" fill="url(#bgGlow)"/>
            <circle cx="100" cy="100" r="88" fill="#fff" stroke="url(#pinkGrad)" strokeWidth="7" filter="url(#glow)"/>
            <circle cx="100" cy="100" r="80" fill="none" stroke="url(#goldShine)" strokeWidth="3" strokeDasharray="8,4" opacity="0.8"/>
            <circle cx="100" cy="100" r="72" fill="none" stroke="#ffc0cb" strokeWidth="1" strokeDasharray="3,2" opacity="0.5"/>
            <path d="M 55,50 L 60,38 L 65,50 L 77,50 L 67,58 L 72,70 L 60,62 L 48,70 L 53,58 L 43,50 Z" fill="url(#goldShine)" filter="url(#glow)"/>
            <path d="M 133,50 L 138,38 L 143,50 L 155,50 L 145,58 L 150,70 L 138,62 L 126,70 L 131,58 L 121,50 Z" fill="url(#goldShine)" filter="url(#glow)"/>
            <ellipse cx="100" cy="40" rx="15" ry="10" fill="url(#goldShine)" opacity="0.6"/>
            <path d="M 92,36 Q 100,30 108,36" stroke="url(#pinkGrad)" strokeWidth="2.5" fill="none"/>
            <circle cx="35" cy="100" r="7" fill="url(#pinkGrad)" filter="url(#glow)"/>
            <circle cx="165" cy="100" r="7" fill="url(#pinkGrad)" filter="url(#glow)"/>
            <path d="M 60,125 Q 70,135 80,125" stroke="url(#pinkGrad)" strokeWidth="4" fill="none" strokeLinecap="round" filter="url(#glow)"/>
            <path d="M 120,125 Q 130,135 140,125" stroke="url(#pinkGrad)" strokeWidth="4" fill="none" strokeLinecap="round" filter="url(#glow)"/>
            <ellipse cx="100" cy="145" rx="25" ry="12" fill="url(#goldShine)" opacity="0.2"/>
            <path d="M 40,80 L 43,73 L 46,80 L 53,80 L 47,85 L 50,92 L 43,87 L 36,92 L 39,85 L 33,80 Z" fill="#ff69b4" opacity="0.7"/>
            <path d="M 147,80 L 150,73 L 153,80 L 160,80 L 154,85 L 157,92 L 150,87 L 143,92 L 146,85 L 140,80 Z" fill="#ff69b4" opacity="0.7"/>
            <circle cx="100" cy="100" r="4" fill="url(#goldShine)"/>
            <path d="M 75,60 Q 80,55 85,60" stroke="#ff69b4" strokeWidth="2" fill="none" opacity="0.6"/>
            <path d="M 115,60 Q 120,55 125,60" stroke="#ff69b4" strokeWidth="2" fill="none" opacity="0.6"/>
            <text x="100" y="88" fontFamily="'Arial Black', Arial, sans-serif" fontSize="30" fontWeight="900" fill="url(#pinkGrad)" textAnchor="middle" letterSpacing="2" filter="url(#glow)">BEAUTY</text>
            <text x="100" y="118" fontFamily="'Arial Black', Arial, sans-serif" fontSize="26" fontWeight="900" fill="url(#goldShine)" textAnchor="middle" letterSpacing="3" filter="url(#glow)">STORE</text>
          </svg>
          <h2>Create Account</h2>
          <form onSubmit={handleLogin}>
            <input
              type="text"
              placeholder="Username"
              value={loginUsername}
              onChange={(e) => setLoginUsername(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Password"
              value={loginPassword}
              onChange={(e) => setLoginPassword(e.target.value)}
              required
            />
            <button type="submit">Create Account</button>
          </form>
        </div>
      </div>
    )
  }

  return (
    <div className="App">
      <div className="header">
        <div className="logo" onClick={() => setView('home')} style={{display: 'flex', alignItems: 'center', cursor: 'pointer'}}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140" width="45" height="45" style={{marginRight: '10px'}}>
            <defs>
              <linearGradient id="pinkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style={{stopColor:'#ff1493',stopOpacity:1}} />
                <stop offset="50%" style={{stopColor:'#ff69b4',stopOpacity:1}} />
                <stop offset="100%" style={{stopColor:'#ff1493',stopOpacity:1}} />
              </linearGradient>
            </defs>
            <circle cx="70" cy="70" r="65" fill="#fff" stroke="url(#pinkGrad)" strokeWidth="4"/>
            <path d="M 40,35 L 42,30 L 44,35 L 49,35 L 45,38 L 47,43 L 42,40 L 37,43 L 39,38 L 35,35 Z" fill="#ff69b4" opacity="0.7"/>
            <path d="M 96,35 L 98,30 L 100,35 L 105,35 L 101,38 L 103,43 L 98,40 L 93,43 L 95,38 L 91,35 Z" fill="#ff69b4" opacity="0.7"/>
            <circle cx="30" cy="70" r="4" fill="#ff1493" opacity="0.6"/>
            <circle cx="110" cy="70" r="4" fill="#ff1493" opacity="0.6"/>
            <text x="70" y="62" fontFamily="'Arial Black', Arial, sans-serif" fontSize="24" fontWeight="900" fill="#ff1493" textAnchor="middle" letterSpacing="1">BEAUTY</text>
            <text x="70" y="85" fontFamily="'Arial Black', Arial, sans-serif" fontSize="20" fontWeight="900" fill="#ff69b4" textAnchor="middle" letterSpacing="2">STORE</text>
          </svg>
          <span style={{fontFamily: 'Arial, sans-serif', fontWeight: '700', letterSpacing: '1px', color: '#ff1493'}}>Beauty Store</span>
        </div>
        <div className="username-display">Welcome, {username}!</div>
        <div className="nav">
          <button className={`nav-btn ${view === 'home' ? 'active' : ''}`} onClick={() => setView('home')}>Home</button>
          <button className={`nav-btn ${!selectedCategory ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter(null); }}>All</button>
          <button className={`nav-btn ${selectedCategory === 'Makeup' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Makeup'); }}>Makeup</button>
          <button className={`nav-btn ${selectedCategory === 'Skincare' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Skincare'); }}>Skincare</button>
          <button className={`nav-btn ${selectedCategory === 'Haircare' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Haircare'); }}>Haircare</button>
          <button className={`nav-btn ${selectedCategory === 'Fragrance' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Fragrance'); }}>Fragrance</button>
          <button className={`nav-btn ${selectedCategory === 'Bath and Body' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Bath and Body'); }}>Bath & Body</button>
          <button className={`nav-btn ${view === 'luxe' ? 'active' : ''}`} onClick={() => setView('luxe')}>Luxe</button>
          <button className={`nav-btn ${view === 'sale' ? 'active' : ''}`} onClick={() => setView('sale')}>Beauty Fashion</button>
          <button className={`nav-btn ${view === 'brands' ? 'active' : ''}`} onClick={() => setView('brands')}>Brands</button>
        </div>
        <div className="header-icons">
          <button className="icon-btn" onClick={() => setShowOrders(true)}>📦 Orders ({orders.length})</button>
          <button className="icon-btn" onClick={() => setShowWishlist(true)}>❤️ Wishlist ({wishlist.length})</button>
          <button className="icon-btn" onClick={() => setShowCart(true)}>🛒 Cart ({cart.length})</button>
        </div>
      </div>

      {view === 'home' && (
        <>
          <div className="banner">
            <h1>Welcome to Beauty Store</h1>
            <p>Discover premium beauty products for every need</p>
          </div>
          <div className="description-section">
            <h2>Description</h2>
            <p>Welcome to our premium beauty store, your one-stop destination for all your beauty needs. We offer a carefully curated collection of high-quality skincare, makeup, haircare, fragrances, and bath & body products from trusted brands.</p>
            <div className="product-categories-desc">
              <div className="category-desc">
                <h3>💄 Makeup</h3>
                <p>Discover our extensive range of makeup products including foundations, lipsticks, eyeshadow palettes, mascaras, and more. From everyday looks to glamorous evening styles.</p>
              </div>
              <div className="category-desc">
                <h3>✨ Skincare</h3>
                <p>Nourish your skin with our premium skincare collection featuring moisturizers, serums, face masks, cleansers, and sunscreens for all skin types.</p>
              </div>
              <div className="category-desc">
                <h3>💇 Haircare</h3>
                <p>Transform your hair with our professional haircare products including shampoos, conditioners, hair masks, serums, and styling treatments.</p>
              </div>
              <div className="category-desc">
                <h3>🌸 Fragrance</h3>
                <p>Explore our exquisite collection of perfumes and colognes with captivating scents from floral to musky, perfect for every occasion.</p>
              </div>
              <div className="category-desc">
                <h3>🛁 Bath & Body</h3>
                <p>Pamper yourself with our luxurious bath and body products including lotions, body butters, scrubs, and bath bombs for ultimate relaxation.</p>
              </div>
            </div>
          </div>
          <div className="search-container">
            <input className="search-bar" placeholder="Search products..." value={searchTerm} onChange={handleSearch} />
          </div>
          <div className="promo-section">
            <div className="promo-banner sale-promo" onClick={() => setView('sale')}>
              <h2>🎉 MEGA SALE</h2>
              <p>Up to 30% OFF on Selected Products</p>
              <button className="promo-btn">Shop Now</button>
            </div>
            <div className="promo-banner luxe-promo" onClick={() => setView('luxe')}>
              <h2>✨ LUXE COLLECTION</h2>
              <p>Premium Beauty Products</p>
              <button className="promo-btn">Explore Luxury</button>
            </div>
          </div>
          <div className="ads-section">
            <div className="ad-card video-ad">
              <video autoPlay loop muted playsInline poster="https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=600">
                <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4" type="video/mp4" />
              </video>
              <div className="ad-overlay" onClick={() => { setView('products'); handleCategoryFilter('Makeup'); }}>
                <h3>Makeup Essentials</h3>
                <p>Discover Your Perfect Look</p>
              </div>
            </div>
            <div className="ad-card video-ad">
              <video autoPlay loop muted playsInline poster="https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=600">
                <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4" type="video/mp4" />
              </video>
              <div className="ad-overlay" onClick={() => { setView('products'); handleCategoryFilter('Skincare'); }}>
                <h3>Skincare Routine</h3>
                <p>Glow From Within</p>
              </div>
            </div>
            <div className="ad-card">
              <img src="https://images.unsplash.com/photo-1541643600914-78b084683601?w=600" alt="Fragrance" />
              <div className="ad-overlay" onClick={() => { setView('products'); handleCategoryFilter('Fragrance'); }}>
                <h3>Signature Scents</h3>
                <p>Find Your Fragrance</p>
              </div>
            </div>
          </div>
        </>
      )}

      {view === 'products' && (
        <>
          <div className="search-container">
            <input className="search-bar" placeholder="Search products..." value={searchTerm} onChange={handleSearch} />
          </div>
          <div className="products-container">
            <div className="nav" style={{marginBottom: '2rem'}}>
              <button className={`nav-btn ${!selectedCategory ? 'active' : ''}`} onClick={() => handleCategoryFilter(null)}>All</button>
              {categories.map(cat => (
                <button key={cat} className={`nav-btn ${selectedCategory === cat ? 'active' : ''}`} onClick={() => handleCategoryFilter(cat)}>{cat}</button>
              ))}
            </div>
            <h2>{selectedCategory || 'All Products'} ({products.length})</h2>
            <div className="products-grid">
              {products.map(p => (
                <div key={p.id} className="product-card">
                  <div className="product-image" onClick={() => viewProductDetails(p.id)}>
                    <img src={p.image_url || 'https://via.placeholder.com/250'} alt={p.name} onError={(e) => e.target.src = 'https://via.placeholder.com/250/ff1493/ffffff?text=Beauty+Product'} />
                    <button className={`wishlist-btn ${wishlist.some(w => w.id === p.id) ? 'active' : ''}`} onClick={(e) => { e.stopPropagation(); toggleWishlist(p); }}>
                      {wishlist.some(w => w.id === p.id) ? '❤️' : '🤍'}
                    </button>
                  </div>
                  <div className="product-info">
                    <div className="product-brand">{p.brand}</div>
                    <div className="product-name">{p.name}</div>
                    <div className="product-category">{p.category}</div>
                    <div className="product-footer">
                      <div className="product-price">₹{p.price}</div>
                      <button className="add-to-cart-btn" onClick={(e) => { e.stopPropagation(); addToCart(p); }}>Add to Cart</button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}


      {view === 'luxe' && (
        <>
          <div className="banner">
            <h1>✨ Luxe Collection</h1>
            <p>Indulge in our premium luxury beauty products</p>
          </div>
          <div className="products-container">
            <h2>Luxury Products</h2>
            <div className="products-grid">
              {allProducts.filter(p => p.price > 900).map(p => (
                <div key={p.id} className="product-card luxe-card">
                  <div className="luxe-badge">LUXE</div>
                  <div className="product-image" onClick={() => viewProductDetails(p.id)}>
                    <img src={p.image_url} alt={p.name} onError={(e) => e.target.src = 'https://via.placeholder.com/250/ff1493/ffffff?text=Luxury'} />
                    <button className={`wishlist-btn ${wishlist.some(w => w.id === p.id) ? 'active' : ''}`} onClick={(e) => { e.stopPropagation(); toggleWishlist(p); }}>
                      {wishlist.some(w => w.id === p.id) ? '❤️' : '🤍'}
                    </button>
                  </div>
                  <div className="product-info">
                    <div className="product-brand">{p.brand}</div>
                    <div className="product-name">{p.name}</div>
                    <div className="product-category">{p.category}</div>
                    <div className="product-footer">
                      <div className="product-price">₹{p.price}</div>
                      <button className="add-to-cart-btn" onClick={(e) => { e.stopPropagation(); addToCart(p); }}>Add to Cart</button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}

      {view === 'sale' && (
        <>
          <div className="banner sale-banner">
            <h1>🎉 Beauty Fashion Sale</h1>
            <p>Amazing deals on trending beauty products</p>
          </div>
          <div className="products-container">
            <h2>Sale Products - Up to 30% Off</h2>
            <div className="products-grid">
              {allProducts.filter(p => p.price < 600).map(p => (
                <div key={p.id} className="product-card sale-card">
                  <div className="sale-badge">SALE 30% OFF</div>
                  <div className="product-image" onClick={() => viewProductDetails(p.id)}>
                    <img src={p.image_url} alt={p.name} onError={(e) => e.target.src = 'https://via.placeholder.com/250/ff1493/ffffff?text=Sale'} />
                    <button className={`wishlist-btn ${wishlist.some(w => w.id === p.id) ? 'active' : ''}`} onClick={(e) => { e.stopPropagation(); toggleWishlist(p); }}>
                      {wishlist.some(w => w.id === p.id) ? '❤️' : '🤍'}
                    </button>
                  </div>
                  <div className="product-info">
                    <div className="product-brand">{p.brand}</div>
                    <div className="product-name">{p.name}</div>
                    <div className="product-category">{p.category}</div>
                    <div className="product-footer">
                      <div className="product-price">₹{p.price}</div>
                      <button className="add-to-cart-btn" onClick={(e) => { e.stopPropagation(); addToCart(p); }}>Add to Cart</button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}

      {view === 'brands' && (
        <>
          <div className="banner">
            <h1>🏷️ Our Brands</h1>
            <p>Discover trusted beauty brands we carry</p>
          </div>
          <div className="brands-container">
            <div className="brands-grid">
              {[...new Set(allProducts.map(p => p.brand))].sort().map(brand => (
                <div key={brand} className="brand-card">
                  <h3>{brand}</h3>
                  <p>{allProducts.filter(p => p.brand === brand).length} Products</p>
                  <button className="view-brand-btn" onClick={() => { setView('products'); setProducts(allProducts.filter(p => p.brand === brand)); }}>View Products</button>
                </div>
              ))}
            </div>
          </div>
        </>
      )}

      {showCart && (
        <div className="modal" onClick={() => setShowCart(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2>Shopping Cart</h2>
            <div className="modal-items">
              {cart.length === 0 ? <p>Cart is empty</p> : cart.map(item => (
                <div key={item.id} className="modal-item">
                  <img src={item.image_url || 'https://via.placeholder.com/80'} alt={item.name} onError={(e) => e.target.src = 'https://via.placeholder.com/80/ff1493/ffffff?text=Product'} />
                  <div className="modal-item-info">
                    <h4>{item.name}</h4>
                    {item.isSale && <span className="sale-tag">30% OFF</span>}
                    {item.isSale ? (
                      <p>
                        <span className="original-price">₹{item.originalPrice}</span>
                        <span className="sale-price">₹{item.salePrice.toFixed(2)}</span>
                        <span> x {item.quantity}</span>
                      </p>
                    ) : (
                      <p>₹{item.price} x {item.quantity}</p>
                    )}
                    <div className="quantity-controls">
                      <button onClick={() => setCart(cart.map(i => i.id === item.id ? {...i, quantity: Math.max(1, i.quantity - 1)} : i))}>-</button>
                      <span>{item.quantity}</span>
                      <button onClick={() => setCart(cart.map(i => i.id === item.id ? {...i, quantity: i.quantity + 1} : i))}>+</button>
                    </div>
                  </div>
                  <button onClick={() => removeFromCart(item.id)}>Remove</button>
                </div>
              ))}
            </div>
            {cart.length > 0 && <div className="cart-total">Total: ₹{cartTotal.toFixed(2)}</div>}
            {cart.length > 0 && <button className="checkout-btn" onClick={handleCheckout}>Proceed to Checkout</button>}
            <button className="close-btn" onClick={() => setShowCart(false)}>Close</button>
          </div>
        </div>
      )}

      {showWishlist && (
        <div className="modal" onClick={() => setShowWishlist(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2>My Wishlist</h2>
            <div className="modal-items">
              {wishlist.length === 0 ? <p>Wishlist is empty</p> : wishlist.map(item => (
                <div key={item.id} className="modal-item">
                  <img src={item.image_url || 'https://via.placeholder.com/80'} alt={item.name} onError={(e) => e.target.src = 'https://via.placeholder.com/80/ff1493/ffffff?text=Product'} />
                  <div className="modal-item-info">
                    <h4>{item.name}</h4>
                    <p>₹{item.price}</p>
                  </div>
                  <button onClick={() => addToCart(item)}>Add to Cart</button>
                </div>
              ))}
            </div>
            <button className="close-btn" onClick={() => setShowWishlist(false)}>Close</button>
          </div>
        </div>
      )}

      {showOrders && (
        <div className="modal" onClick={() => setShowOrders(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2>My Orders</h2>
            <div className="modal-items">
              {orders.length === 0 ? <p>No orders yet</p> : orders.map(order => (
                <div key={order.id} className="order-card">
                  <div className="order-header">
                    <h3>Order #{order.id}</h3>
                    <span className="order-status">{order.status}</span>
                  </div>
                  <p><strong>Date:</strong> {order.date}</p>
                  <p><strong>Tracking ID:</strong> {order.trackingId}</p>
                  <p><strong>Payment:</strong> {order.paymentMethod}</p>
                  <p><strong>Total:</strong> ₹{order.total.toFixed(2)}</p>
                  <p><strong>Delivery to:</strong> {order.shippingDetails.name}, {order.shippingDetails.address}</p>
                  
                  <div className="tracking-timeline">
                    <h4>Order Tracking</h4>
                    {order.trackingHistory && order.trackingHistory.map((track, idx) => (
                      <div key={idx} className="tracking-step">
                        <div className="tracking-dot"></div>
                        <div className="tracking-info">
                          <strong>{track.status}</strong>
                          <p>{track.description}</p>
                          <small>{track.date}</small>
                        </div>
                      </div>
                    ))}
                  </div>
                  
                  <div className="order-items">
                    <strong>Items:</strong>
                    {order.items.map(item => (
                      <div key={item.id}>{item.name} x {item.quantity}</div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <button className="close-btn" onClick={() => setShowOrders(false)}>Close</button>
          </div>
        </div>
      )}

      {selectedProduct && (
        <div className="modal" onClick={() => setSelectedProduct(null)}>
          <div className="modal-content product-detail-modal" onClick={e => e.stopPropagation()}>
            <h2>{selectedProduct.name}</h2>
            <img src={selectedProduct.image_url} alt={selectedProduct.name} style={{width: '100%', maxHeight: '300px', objectFit: 'cover', borderRadius: '10px', marginBottom: '1rem'}} onError={(e) => e.target.src = 'https://via.placeholder.com/400/ff1493/ffffff?text=Product+Image'} />
            <div className="product-details">
              <p><strong>Brand:</strong> {selectedProduct.brand}</p>
              <p><strong>Category:</strong> {selectedProduct.category}</p>
              <p><strong>Price:</strong> ₹{selectedProduct.price}</p>
              <p><strong>Stock:</strong> {selectedProduct.stock} units</p>
              <div className="product-description">
                <strong>Description:</strong>
                <p>{selectedProduct.description || 'Premium quality beauty product designed to enhance your natural beauty. Suitable for all skin types.'}</p>
              </div>
              <div className="product-options">
                <div className="quantity-selector">
                  <strong>Quantity:</strong>
                  <div className="quantity-controls">
                    <button onClick={() => setSelectedProduct({...selectedProduct, selectedQty: Math.max(1, (selectedProduct.selectedQty || 1) - 1)})}>-</button>
                    <span>{selectedProduct.selectedQty || 1}</span>
                    <button onClick={() => setSelectedProduct({...selectedProduct, selectedQty: (selectedProduct.selectedQty || 1) + 1})}>+</button>
                  </div>
                </div>
                <div className="color-selector">
                  <strong>Color:</strong>
                  <div className="color-options">
                    <div className="color-option" style={{background: '#FFB6C1'}} onClick={() => setSelectedProduct({...selectedProduct, selectedColor: 'Pink'})} title="Pink"></div>
                    <div className="color-option" style={{background: '#FF6B9D'}} onClick={() => setSelectedProduct({...selectedProduct, selectedColor: 'Rose'})} title="Rose"></div>
                    <div className="color-option" style={{background: '#C8A2C8'}} onClick={() => setSelectedProduct({...selectedProduct, selectedColor: 'Lilac'})} title="Lilac"></div>
                    <div className="color-option" style={{background: '#DDA0DD'}} onClick={() => setSelectedProduct({...selectedProduct, selectedColor: 'Plum'})} title="Plum"></div>
                    <div className="color-option" style={{background: '#F5DEB3'}} onClick={() => setSelectedProduct({...selectedProduct, selectedColor: 'Nude'})} title="Nude"></div>
                  </div>
                  {selectedProduct.selectedColor && <p className="selected-color">Selected: {selectedProduct.selectedColor}</p>}
                </div>
              </div>
            </div>
            <button className="add-to-cart-btn" style={{width: '100%', marginTop: '1rem'}} onClick={() => { 
              const qty = selectedProduct.selectedQty || 1;
              for(let i = 0; i < qty; i++) {
                addToCart(selectedProduct);
              }
              setSelectedProduct(null); 
            }}>Add {selectedProduct.selectedQty || 1} to Cart</button>
            <button className="close-btn" onClick={() => setSelectedProduct(null)}>Close</button>
          </div>
        </div>
      )}

      {showCheckout && (
        <div className="modal" onClick={() => setShowCheckout(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2>Shipping Details</h2>
            <form onSubmit={handlePlaceOrder}>
              <input
                type="text"
                placeholder="Full Name"
                value={shippingDetails.name}
                onChange={(e) => setShippingDetails({...shippingDetails, name: e.target.value})}
                required
              />
              <textarea
                placeholder="Delivery Address"
                value={shippingDetails.address}
                onChange={(e) => setShippingDetails({...shippingDetails, address: e.target.value})}
                required
                rows="3"
              />
              <input
                type="tel"
                placeholder="Mobile Number"
                value={shippingDetails.mobile}
                onChange={(e) => setShippingDetails({...shippingDetails, mobile: e.target.value})}
                required
                pattern="[0-9]{10}"
              />
              <input
                type="text"
                placeholder="Pincode"
                value={shippingDetails.pincode}
                onChange={(e) => setShippingDetails({...shippingDetails, pincode: e.target.value})}
                required
                pattern="[0-9]{6}"
              />
              <div className="cart-total">Total Amount: ₹{cartTotal.toFixed(2)}</div>
              <button type="submit" className="checkout-btn">Proceed to Payment</button>
              <button type="button" className="close-btn" onClick={() => setShowCheckout(false)}>Cancel</button>
            </form>
          </div>
        </div>
      )}




    </div>
  )
}

export default App
