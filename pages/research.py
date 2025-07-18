import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Talk2PDF - Research Mode",
    page_icon="🔬",
    layout="wide"
)

# Custom CSS for research theme
st.markdown("""
<style>
    .research-header {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .research-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .research-subtitle {
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
    <div class="research-header">
        <h1 class="research-title">🔬 Research Mode</h1>
        <p class="research-subtitle">Analyze research papers and scientific documents</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🧪 Research Document Analysis")
        st.markdown("""
        Upload your research documents and get help with:
        - **Literature Review**: Summarize key findings and methodologies
        - **Data Analysis**: Understand statistical results and interpretations
        - **Methodology Review**: Analyze research methods and approaches
        - **Citation Tracking**: Find relevant references and citations
        """)
        
        # Chat interface placeholder
        st.markdown("### 💬 Research Assistant")
        question = st.text_area("What research questions do you have?", 
                               placeholder="e.g., What methodology was used in this study?")
        
        if st.button("Ask Question", type="primary"):
            if question:
                st.info("This feature will be implemented to process your research question with the uploaded documents.")
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
        
        st.markdown("### 🔬 Research Tools")
        st.markdown("""
        - **Abstract Extractor**
        - **Methodology Analyzer**  
        - **Data Interpreter**
        - **Reference Finder**
        """)

if __name__ == "__main__":
    main()