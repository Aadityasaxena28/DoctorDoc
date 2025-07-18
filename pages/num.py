import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Talk2PDF - Numerical Mode",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for numerical theme
st.markdown("""
<style>
    .num-header {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .num-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .num-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Back button
    if st.button("← Back to Home", key="back_home"):
        st.switch_page("main.py")
    
    # Header
    st.markdown("""
    <div class="num-header">
        <h1 class="num-title">📊 Numerical Mode</h1>
        <p class="num-subtitle">Analyze numerical data, reports, and statistical documents</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📈 Numerical Document Analysis")
        st.markdown("""
        Upload your numerical documents and get assistance with:
        - **Data Interpretation**: Understand charts, graphs, and tables
        - **Statistical Analysis**: Analyze statistical reports and findings
        - **Financial Reports**: Review financial statements and metrics
        - **Performance Metrics**: Extract and analyze KPIs and indicators
        """)
        
        # Chat interface placeholder
        st.markdown("### 💬 Data Analyst")
        question = st.text_area("What numerical questions do you have?", 
                               placeholder="e.g., What are the key trends shown in this financial report?")
        
        if st.button("Ask Question", type="primary"):
            if question:
                st.info("This feature will be implemented to process your numerical question with the uploaded documents.")
            else:
                st.warning("Please enter a question first.")
    
    with col2:
        st.markdown("### 📁 Your Documents")
        
        # Check for uploaded files in data2 directory
        data_dir = Path("data2")
        if data_dir.exists():
            pdf_files = list(data_dir.glob("*.pdf"))
            if pdf_files:
                st.success(f"Found {len(pdf_files)} PDF file(s)")
                for pdf_file in pdf_files:
                    st.markdown(f"• {pdf_file.name}")
            else:
                st.info("No PDF files uploaded yet. Go back to upload some documents!")
        else:
            st.info("No documents uploaded yet. Go back to upload some documents!")
        
        st.markdown("### 📊 Numerical Tools")
        st.markdown("""
        - **Chart Interpreter**
        - **Trend Analyzer**  
        - **Statistical Summary**
        - **Data Extractor**
        """)

if __name__ == "__main__":
    main()