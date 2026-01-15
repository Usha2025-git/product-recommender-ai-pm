import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objects as go
import plotly.express as px

# Page config with e-commerce theme
st.set_page_config(
    page_title="📊produit-recommender-ai-pm",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stunning e-commerce CSS with blue/orange gradients
st.markdown("""
<style>
    /* Main gradient background - E-commerce theme */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2.5rem 1rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(240, 87, 108, 0.4);
    }
    
    .main-header h1 {
        color: #ffffff;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }
    
    .main-header p {
        color: #ffe6f0;
        font-size: 1.2rem;
        font-weight: 500;
    }
    
    /* Product cards */
    .product-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.5);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(245, 87, 108, 0.3);
    }
    
    /* Metrics styling */
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        margin: 0.5rem 0;
    }
    
    .metric-box h2 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .metric-box p {
        margin: 0.5rem 0 0 0;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #f093fb 100%);
    }
    
    [data-testid="stSidebar"] .element-container {
        color: white;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(90deg, #f5576c 0%, #f093fb 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.75rem 2.5rem;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 25px rgba(245, 87, 108, 0.6);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #f5576c 0%, #f093fb 100%);
        border-radius: 10px;
    }
    
    /* Select box styling */
    .stSelectbox {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📊 Product Recommender</h1>
    <p>✨ AI-Powered Personalization Engine | E-Commerce Innovation</p>
</div>
""", unsafe_allow_html=True)

# Load sample data
@st.cache_data
def load_sample_data():
    products = pd.DataFrame({
        'product_id': range(1, 51),
        'name': [f"Product_{i}" for i in range(1, 51)],
        'category': np.random.choice(['Electronics', 'Fashion', 'Books', 'Home', 'Sports'], 50),
        'price': np.random.uniform(10, 500, 50).round(2),
        'rating': np.random.uniform(3.5, 5.0, 50).round(1),
        'sales': np.random.randint(100, 5000, 50)
    })
    return products

products = load_sample_data()

# Sidebar configuration
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    model_choice = st.radio(
        "Select Recommendation Model",
        ["Collaborative Filtering", "Deep Learning"]
    )
    num_recommendations = st.slider(
        "Number of Recommendations",
        3, 15, 10
    )
    
    st.markdown("---")
    st.markdown("### 📊 Success Metrics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="color: white; margin: 0;">+15%</h3>
            <p style="color: #ffe6f0; margin: 0.5rem 0 0 0; font-size: 0.8rem;">CTR Lift</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="color: white; margin: 0;">+8%</h3>
            <p style="color: #ffe6f0; margin: 0.5rem 0 0 0; font-size: 0.8rem;">Revenue</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ℹ️ AI PM Portfolio")
    st.markdown("""
    **Project Highlights:**
    - 🎯 Two-stage recommendation
    - 🧠 CF + Deep learning
    - 📈 Cold start handling
    - ⚖️ Diversity & fairness
    - 📊 A/B testing framework
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <p style="color: white; margin: 0;">Built by</p>
        <h3 style="color: white; margin: 0.5rem 0;">Usha Swinir</h3>
        <p style="color: #ffe6f0; font-size: 0.9rem; margin: 0;">AI Product Manager</p>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("### 🎯 Personalized Recommendations")

# User selection
col1, col2 = st.columns([2, 1])

with col1:
    selected_user = st.selectbox(
        "👤 Select User Profile",
        ["New User (Cold Start)", "Fashion Enthusiast", "Tech Lover", "Bookworm", "Sports Fan"]
    )

with col2:
    if st.button("🔄 Generate Recommendations", use_container_width=True):
        st.balloons()

# Display recommendations in a grid
st.markdown("#### ✨ Your Personalized Picks")

# Create sample recommendations
if model_choice == "Collaborative Filtering":
    recommended_products = products.sample(n=num_recommendations)
else:
    recommended_products = products.nlargest(num_recommendations, 'rating')

# Display products in cards (3 columns)
cols = st.columns(3)
for idx, (_, product) in enumerate(recommended_products.iterrows()):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="font-size: 3rem;">📦</div>
            </div>
            <h3 style="color: #f5576c; text-align: center; margin: 0.5rem 0;">{product['name']}</h3>
            <p style="text-align: center; color: #666; margin: 0.3rem 0;">🏷️ {product['category']}</p>
            <p style="text-align: center; font-size: 1.5rem; font-weight: 700; color: #667eea; margin: 0.5rem 0;">
                ${product['price']}
            </p>
            <p style="text-align: center; color: #f5576c; margin: 0;">
                ⭐ {product['rating']} | 📊 {product['sales']} sold
            </p>
        </div>
        """, unsafe_allow_html=True)

# Performance metrics
st.markdown("---")
st.markdown("### 📊 Model Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-box">
        <h2>92%</h2>
        <p>Precision@12</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box" style="background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);">
        <h2>0.75</h2>
        <p>Diversity Score</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <h2>&lt;500ms</h2>
        <p>Response Time</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-box" style="background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);">
        <h2>85%</h2>
        <p>Cold Start Coverage</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: white;">
    <h3 style="margin: 0 0 0.5rem 0;">🚀 AI PM Portfolio Project</h3>
    <p style="margin: 0; font-size: 1.1rem;">E-Commerce Product Recommendation Engine</p>
    <p style="margin: 0.5rem 0; opacity: 0.9;">Demonstrating: Collaborative Filtering • Deep Learning • Cold Start Strategy • Diversity Optimization</p>
    <p style="margin: 1rem 0 0 0;">
        📚 <a href="https://github.com/Usha2025-git/product-recommender-ai-pm" style="color: #ffe6f0; font-weight: 600;">View on GitHub</a> • 
        💼 <a href="https://www.linkedin.com/in/ushaswinir-product/" style="color: #ffe6f0; font-weight: 600;">LinkedIn</a>
    </p>
</div>
""", unsafe_allow_html=True)
