import streamlit as st
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Talk2PDF",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 3rem 0;
        flex-wrap: wrap;
    }
    
    .custom-button {
        background: linear-gradient(145deg, #f0f0f0, #cacaca);
        border: none;
        border-radius: 20px;
        padding: 2rem 3rem;
        min-width: 200px;
        min-height: 150px;
        box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .custom-button:hover {
        transform: translateY(-5px);
        box-shadow: 25px 25px 80px #bebebe, -25px -25px 80px #ffffff;
    }
    
    .btn-student {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .btn-legal {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .btn-research {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .btn-num {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    }
    
    .upload-section {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 3rem auto;
        max-width: 600px;
        text-align: center;
    }
    
    .upload-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 15px;
        border: none;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #666;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header section
    st.markdown('<h1 class="main-title">Talk2PDF: Ask Anything From Your Documents 💬</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Unlock the power of your documents with AI-powered conversations</p>', unsafe_allow_html=True)
    
    # Navigation buttons
    st.markdown("### Choose Your Document Type")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📚 STUDENT", key="student", help="Academic papers, textbooks, study materials"):
            st.switch_page("pages/student.py")
    
    with col2:
        if st.button("⚖️ LEGAL", key="legal", help="Legal documents, contracts, regulations"):
            st.switch_page("pages/legal.py")
    
    with col3:
        if st.button("🔬 RESEARCH", key="research", help="Research papers, scientific documents"):
            st.switch_page("pages/research.py")
    
    with col4:
        if st.button("📊 NUM", key="num", help="Numerical analysis, data reports"):
            st.switch_page("pages/num.py")
    
    # File uploader section
    st.markdown("---")
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown('<h3 class="upload-title">📄 Upload Your PDF Documents</h3>', unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=['pdf'],
        accept_multiple_files=True,
        help="Upload one or more PDF files to get started"
    )
    
    if uploaded_files:
        # Create data2 directory if it doesn't exist
        data_dir = Path("data2")
        data_dir.mkdir(exist_ok=True)
        
        st.success(f"✅ Successfully uploaded {len(uploaded_files)} file(s)!")
        
        # Save uploaded files
        for uploaded_file in uploaded_files:
            file_path = data_dir / uploaded_file.name
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        
        # Display uploaded files
        st.markdown("**Uploaded Files:**")
        for file in uploaded_files:
            st.markdown(f"• {file.name} ({file.size} bytes)")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Features section
    st.markdown("---")
    st.markdown("### Why Choose Talk2PDF?")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered</div>
            <div class="feature-desc">Advanced AI understands context and provides accurate answers</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Lightning Fast</div>
            <div class="feature-desc">Get instant responses to your document queries</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Secure</div>
            <div class="feature-desc">Your documents are processed securely and privately</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Specialized</div>
            <div class="feature-desc">Tailored experiences for different document types</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()