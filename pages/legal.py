import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Talk2PDF - Legal Mode",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS for legal theme
st.markdown("""
<style>
    .legal-header {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .legal-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .legal-subtitle {
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
    <div class="legal-header">
        <h1 class="legal-title">⚖️ Legal Mode</h1>
        <p class="legal-subtitle">Analyze legal documents, contracts, and regulations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📜 Legal Document Analysis")
        st.markdown("""
        Upload your legal documents and get assistance with:
        - **Contract Review**: Identify key terms and potential issues
        - **Legal Research**: Find relevant clauses and precedents
        - **Compliance Check**: Ensure regulatory compliance
        - **Risk Assessment**: Identify potential legal risks
        """)
        
        # Chat interface placeholder
        st.markdown("### 💬 Legal Consultation")
        question = st.text_area("What legal questions do you have about your documents?", 
                               placeholder="e.g., What are the termination clauses in this contract?")
        
        if st.button("Ask Question", type="primary"):
            if question:
                st.info("This feature will be implemented to process your legal question with the uploaded documents.")
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
        
        st.markdown("### ⚖️ Legal Tools")
        st.markdown("""
        - **Contract Analyzer**
        - **Clause Finder**  
        - **Risk Assessor**
        - **Compliance Checker**
        """)
        
        st.warning("⚠️ **Legal Disclaimer**: This tool is for informational purposes only and does not constitute legal advice.")

if __name__ == "__main__":
    main()