# Talk2PDF: Ask Anything From Your Documents 💬

A beautiful and intuitive Streamlit application for analyzing PDF documents with AI-powered conversations.

## Features

- **Professional UI**: Modern design with gradient backgrounds and smooth animations
- **Multiple Modes**: Specialized interfaces for different document types:
  - 📚 **Student**: Academic papers, textbooks, study materials
  - ⚖️ **Legal**: Legal documents, contracts, regulations
  - 🔬 **Research**: Research papers, scientific documents
  - 📊 **NUM**: Numerical analysis, data reports, financial documents
- **File Management**: Automatic storage of uploaded PDFs in `data2/` folder
- **Responsive Design**: Works on desktop and mobile devices

## Setup

1. Install the required dependencies:
```bash
pip3 install --break-system-packages streamlit
# or if you prefer using requirements.txt:
# pip3 install --break-system-packages -r requirements.txt
```

2. Add the local bin directory to your PATH (if needed):
```bash
export PATH=$PATH:/home/ubuntu/.local/bin
```

3. Run the application:
```bash
streamlit run main.py
```

4. Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

### Quick Start

Alternatively, you can use the provided startup script:
```bash
./run_app.sh
```

This script will automatically install dependencies, set up the environment, and start the application.

## Usage

1. **Upload Documents**: Use the file uploader on the main page to upload your PDF files
2. **Choose Mode**: Click one of the four colored buttons to select the appropriate document analysis mode
3. **Ask Questions**: In each mode, you can ask specific questions about your uploaded documents
4. **Navigate**: Use the back button to return to the main page

## File Structure

```
├── main.py              # Main application page
├── pages/               # Sub-application pages
│   ├── student.py       # Student mode
│   ├── legal.py         # Legal mode
│   ├── research.py      # Research mode
│   └── num.py           # Numerical mode
├── data2/               # Uploaded PDF storage (created automatically)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Customization

The application uses custom CSS for styling. You can modify the colors, fonts, and layout by editing the CSS sections in each Python file.

## Future Enhancements

- AI-powered document analysis
- Chat functionality with document context
- Advanced search and filtering
- Document summarization
- Citation generation