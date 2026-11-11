import React, { useState, useEffect } from 'react'
import './App.css'

const API = window.location.hostname === 'localhost' ? '/api' : 'http://localhost:8000/api'

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [username, setUsername] = useState('')
  const [showLoginForm, setShowLoginForm] = useState(true)
  const [loginUsername, setLoginUsername] = useState('')
  const [loginPassword, setLoginPassword] = useState('')
  const [view, setView] = useState('home')
  const [products, setProducts] = useState([
    {id: 1, name: 'Moisturizing Face Cream', brand: 'GlowSkin', price: 933.76, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400', stock: 100},
    {id: 2, name: 'Vitamin C Serum', brand: 'RadiantGlow', price: 914.78, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400', stock: 100},
    {id: 3, name: 'Matte Lipstick', brand: 'ColorPop', price: 904.73, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400', stock: 100},
    {id: 4, name: 'Eyeshadow Palette', brand: 'GlamourEyes', price: 678.86, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400', stock: 100},
    {id: 5, name: 'Hydrating Shampoo', brand: 'SilkHair', price: 812.67, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400', stock: 100},
    {id: 6, name: 'Hair Conditioner', brand: 'SilkHair', price: 799.86, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400', stock: 100},
    {id: 7, name: 'Floral Perfume', brand: 'Essence', price: 338.3, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=400', stock: 100},
    {id: 8, name: 'Body Lotion', brand: 'SoftTouch', price: 946.21, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
    {id: 9, name: 'Face Mask Set', brand: 'PureGlow', price: 931.35, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?w=400', stock: 100},
    {id: 10, name: 'Nail Polish Set', brand: 'ColorNails', price: 507.9, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1519823551278-64ac92734fb1?w=400', stock: 100},
    {id: 11, name: 'Hyaluronic Acid Serum', brand: 'HydraBoost', price: 405.07, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400', stock: 100},
    {id: 12, name: 'Clay Face Mask', brand: 'PureGlow', price: 936.04, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?w=400', stock: 100},
    {id: 13, name: 'Eye Cream', brand: 'YouthEyes', price: 720.41, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400', stock: 100},
    {id: 14, name: 'Sunscreen SPF 50', brand: 'SunGuard', price: 745.02, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
    {id: 15, name: 'Liquid Foundation', brand: 'FlawlessBeauty', price: 984.45, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400', stock: 100},
    {id: 16, name: 'Lip Gloss Set', brand: 'GlossyLips', price: 508.06, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400', stock: 100},
    {id: 17, name: 'Contour Kit', brand: 'SculptPro', price: 997.04, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1596704017254-9b121068ec31?w=400', stock: 100},
    {id: 18, name: 'Brow Pencil', brand: 'BrowPerfect', price: 333.37, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400', stock: 100},
    {id: 19, name: 'Setting Spray', brand: 'StayOn', price: 776.2, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400', stock: 100},
    {id: 20, name: 'Hair Mask', brand: 'SilkHair', price: 513.87, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400', stock: 100},
    {id: 21, name: 'Dry Shampoo', brand: 'QuickFresh', price: 967.54, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400', stock: 100},
    {id: 22, name: 'Hair Serum', brand: 'SmoothLocks', price: 314.88, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400', stock: 100},
    {id: 23, name: 'Scalp Treatment', brand: 'HealthyRoots', price: 389.3, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400', stock: 100},
    {id: 24, name: 'Lavender Perfume', brand: 'Serenity', price: 744.8, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=400', stock: 100},
    {id: 25, name: 'Musk Cologne', brand: 'Timeless', price: 741.2, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400', stock: 100},
    {id: 26, name: 'Jasmine Eau de Parfum', brand: 'Exotic', price: 894.84, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=400', stock: 100},
    {id: 27, name: 'Bath Bombs Set', brand: 'RelaxSpa', price: 900.52, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
    {id: 28, name: 'Body Butter', brand: 'SoftTouch', price: 592.06, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
    {id: 29, name: 'Foot Cream', brand: 'SmoothFeet', price: 739.8, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
    {id: 30, name: 'Body Oil', brand: 'GlowBody', price: 565.26, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100}
  ])
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
    const initialProducts = [
      {id: 1, name: 'Moisturizing Face Cream', brand: 'GlowSkin', price: 933.76, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400', stock: 100},
      {id: 2, name: 'Vitamin C Serum', brand: 'RadiantGlow', price: 914.78, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400', stock: 100},
      {id: 3, name: 'Matte Lipstick', brand: 'ColorPop', price: 904.73, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400', stock: 100},
      {id: 4, name: 'Eyeshadow Palette', brand: 'GlamourEyes', price: 678.86, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400', stock: 100},
      {id: 5, name: 'Hydrating Shampoo', brand: 'SilkHair', price: 812.67, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400', stock: 100},
      {id: 6, name: 'Hair Conditioner', brand: 'SilkHair', price: 812.67, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400', stock: 100},
      {id: 7, name: 'Floral Perfume', brand: 'Essence', price: 338.3, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=400', stock: 100},
      {id: 8, name: 'Body Lotion', brand: 'SoftTouch', price: 946.21, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
      {id: 9, name: 'Face Mask Set', brand: 'PureGlow', price: 931.35, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?w=400', stock: 100},
      {id: 10, name: 'Nail Polish Set', brand: 'ColorNails', price: 507.9, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1519823551278-64ac92734fb1?w=400', stock: 100},
      {id: 11, name: 'Hyaluronic Acid Serum', brand: 'HydraBoost', price: 405.07, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400', stock: 100},
      {id: 12, name: 'Clay Face Mask', brand: 'PureGlow', price: 946.21, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?w=400', stock: 100},
      {id: 13, name: 'Eye Cream', brand: 'YouthEyes', price: 720.41, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400', stock: 100},
      {id: 14, name: 'Sunscreen SPF 50', brand: 'SunGuard', price: 745.02, category: 'Skincare', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
      {id: 15, name: 'Liquid Foundation', brand: 'FlawlessBeauty', price: 984.45, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400', stock: 100},
      {id: 16, name: 'Lip Gloss Set', brand: 'GlossyLips', price: 812.67, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400', stock: 100},
      {id: 17, name: 'Contour Kit', brand: 'SculptPro', price: 997.04, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1596704017254-9b121068ec31?w=400', stock: 100},
      {id: 18, name: 'Brow Pencil', brand: 'BrowPerfect', price: 333.37, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400', stock: 100},
      {id: 19, name: 'Setting Spray', brand: 'StayOn', price: 507.9, category: 'Makeup', image_url: 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400', stock: 100},
      {id: 20, name: 'Hair Mask', brand: 'SilkHair', price: 513.87, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400', stock: 100},
      {id: 21, name: 'Dry Shampoo', brand: 'QuickFresh', price: 967.54, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400', stock: 100},
      {id: 22, name: 'Hair Serum', brand: 'SmoothLocks', price: 314.88, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400', stock: 100},
      {id: 23, name: 'Scalp Treatment', brand: 'HealthyRoots', price: 933.76, category: 'Haircare', image_url: 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400', stock: 100},
      {id: 24, name: 'Lavender Perfume', brand: 'Serenity', price: 744.8, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=400', stock: 100},
      {id: 25, name: 'Musk Cologne', brand: 'Timeless', price: 741.2, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400', stock: 100},
      {id: 26, name: 'Jasmine Eau de Parfum', brand: 'Exotic', price: 894.84, category: 'Fragrance', image_url: 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=400', stock: 100},
      {id: 27, name: 'Bath Bombs Set', brand: 'RelaxSpa', price: 997.04, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
      {id: 28, name: 'Body Butter', brand: 'SoftTouch', price: 592.06, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
      {id: 29, name: 'Foot Cream', brand: 'SmoothFeet', price: 904.73, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100},
      {id: 30, name: 'Body Oil', brand: 'GlowBody', price: 931.35, category: 'Bath and Body', image_url: 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400', stock: 100}
    ]
    setAllProducts(initialProducts)
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
        setProducts([])
      }
    } catch (e) { 
      console.error('Fetch error:', e)
      setProducts([])
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
    const existing = cart.find(item => item.id === product.id)
    if (existing) {
      setCart(cart.map(item => item.id === product.id ? {...item, quantity: item.quantity + 1} : item))
    } else {
      setCart([...cart, {...product, quantity: 1}])
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

  const cartTotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0)

  const handleCheckout = () => {
    if (cart.length > 0) {
      setShowCart(false)
      setShowCheckout(true)
    }
  }

  const handlePlaceOrder = (e) => {
    e.preventDefault()
    setShowCheckout(false)
    setShowPayment(true)
  }

  const handlePayment = () => {
    if (selectedPayment) {
      setShowPayment(false)
      setShowQRCode(true)
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
    if (loginUsername && loginPassword) {
      setUsername(loginUsername)
      setIsLoggedIn(true)
      setShowLoginForm(false)
    }
  }

  if (!isLoggedIn) {
    return (
      <div className="login-container">
        <div className="login-box">
          <h1>🌸 Beauty Store</h1>
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
        <div className="logo" onClick={() => setView('home')}>🌸 Beauty Store</div>
        <div className="username-display">Welcome, {username}!</div>
        <div className="nav">
          <button className={`nav-btn ${view === 'home' ? 'active' : ''}`} onClick={() => setView('home')}>Home</button>
          <button className={`nav-btn ${!selectedCategory ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter(null); }}>All</button>
          <button className={`nav-btn ${selectedCategory === 'Makeup' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Makeup'); }}>Makeup</button>
          <button className={`nav-btn ${selectedCategory === 'Skincare' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Skincare'); }}>Skincare</button>
          <button className={`nav-btn ${selectedCategory === 'Haircare' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Haircare'); }}>Haircare</button>
          <button className={`nav-btn ${selectedCategory === 'Fragrance' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Fragrance'); }}>Fragrance</button>
          <button className={`nav-btn ${selectedCategory === 'Bath and Body' ? 'active' : ''}`} onClick={() => { setView('products'); handleCategoryFilter('Bath and Body'); }}>Bath & Body</button>
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
            <p>Welcome to our premium beauty store, your one-stop destination for all your beauty needs. We offer a carefully curated collection of high-quality skincare, makeup, haircare, fragrances, and bath & body products from trusted brands. Whether you're looking for the perfect lipstick, a nourishing face serum, or a luxurious fragrance, we have everything you need to look and feel your best. Shop with confidence and discover products that enhance your natural beauty.</p>
          </div>
          <div className="search-container">
            <input className="search-bar" placeholder="Search products..." value={searchTerm} onChange={handleSearch} />
          </div>
          <div className="products-container">
            <h2>Featured Products</h2>
            {products.length === 0 ? (
              <div className="no-products">Loading products...</div>
            ) : (
            <div className="products-grid">
              {products.slice(0, 12).map(p => (
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
            )}
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
                    <p>₹{item.price} x {item.quantity}</p>
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
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2>{selectedProduct.name}</h2>
            <img src={selectedProduct.image_url} alt={selectedProduct.name} style={{width: '100%', maxHeight: '300px', objectFit: 'cover', borderRadius: '10px', marginBottom: '1rem'}} onError={(e) => e.target.src = 'https://via.placeholder.com/400/ff1493/ffffff?text=Product+Image'} />
            <p><strong>Brand:</strong> {selectedProduct.brand}</p>
            <p><strong>Category:</strong> {selectedProduct.category}</p>
            <p><strong>Price:</strong> ₹{selectedProduct.price}</p>
            <p><strong>Stock:</strong> {selectedProduct.stock} units</p>
            <p>{selectedProduct.description}</p>
            <button className="add-to-cart-btn" style={{width: '100%', marginTop: '1rem'}} onClick={() => { addToCart(selectedProduct); setSelectedProduct(null); }}>Add to Cart</button>
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

      {showPayment && (
        <div className="modal" onClick={() => setShowPayment(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2>Select Payment Method</h2>
            <div className="payment-options">
              <div className={`payment-option ${selectedPayment === 'GPay' ? 'selected' : ''}`} onClick={() => setSelectedPayment('GPay')}>
                <div className="payment-icon">💳</div>
                <div>Google Pay</div>
              </div>
              <div className={`payment-option ${selectedPayment === 'PhonePe' ? 'selected' : ''}`} onClick={() => setSelectedPayment('PhonePe')}>
                <div className="payment-icon">💳</div>
                <div>PhonePe</div>
              </div>
              <div className={`payment-option ${selectedPayment === 'Paytm' ? 'selected' : ''}`} onClick={() => setSelectedPayment('Paytm')}>
                <div className="payment-icon">💳</div>
                <div>Paytm</div>
              </div>
            </div>
            <div className="cart-total">Total Amount: ₹{cartTotal.toFixed(2)}</div>
            <button className="checkout-btn" onClick={handlePayment} disabled={!selectedPayment}>Pay Now</button>
            <button className="close-btn" onClick={() => setShowPayment(false)}>Cancel</button>
          </div>
        </div>
      )}

      {showQRCode && (
        <div className="modal" onClick={() => setShowQRCode(false)}>
          <div className="modal-content qr-modal" onClick={e => e.stopPropagation()}>
            <h2>Scan QR Code to Pay</h2>
            <p>Payment Method: <strong>{selectedPayment}</strong></p>
            <div className="qr-code">
              <img src="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=upi://pay?pa=merchant@upi&pn=BeautyStore&am={cartTotal.toFixed(2)}&cu=INR" alt="QR Code" />
            </div>
            <div className="cart-total">Amount: ₹{cartTotal.toFixed(2)}</div>
            <p className="qr-instruction">Scan this QR code with your {selectedPayment} app to complete payment</p>
            <button className="checkout-btn" onClick={handlePaymentComplete}>Payment Done</button>
            <button className="close-btn" onClick={() => setShowQRCode(false)}>Cancel</button>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
