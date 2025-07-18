import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Talk2PDF - Student Mode",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for student theme
st.markdown("""
<style>
    .student-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .student-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .student-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .back-button {
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Back button
    if st.button("← Back to Home", key="back_home"):
        st.switch_page("main.py")
    
    # Header
    st.markdown("""
    <div class="student-header">
        <h1 class="student-title">📚 Student Mode</h1>
        <p class="student-subtitle">Analyze academic papers, textbooks, and study materials</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎓 Academic Document Analysis")
        st.markdown("""
        Upload your academic documents and get help with:
        - **Study Notes**: Extract key concepts and summaries
        - **Research Papers**: Understand complex theories and methodologies
        - **Textbooks**: Get explanations of difficult topics
        - **Assignment Help**: Find relevant information for your papers
        """)
        
        # Chat interface placeholder
        st.markdown("### 💬 Ask Your Questions")
        question = st.text_area("What would you like to know about your documents?", 
                               placeholder="e.g., Summarize the main concepts in chapter 3...")
        
        if st.button("Ask Question", type="primary"):
            if question:
                st.info("This feature will be implemented to process your question with the uploaded documents.")
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
        
        st.markdown("### 🔧 Student Tools")
        st.markdown("""
        - **Summary Generator**
        - **Key Concepts Extractor**  
        - **Question Generator**
        - **Citation Helper**
        """)

if __name__ == "__main__":
    main()