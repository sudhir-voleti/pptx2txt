import streamlit as st
from markdownify import markdownify as md
import os

st.title("HTML to Markdown Converter")

# File uploader for HTML files
uploaded_file = st.file_uploader("Upload an HTML file", type=["html", "htm"])

if uploaded_file is not None:
    # Read the uploaded HTML file
    html_content = uploaded_file.read().decode("utf-8")
    
    # Convert HTML to Markdown
    markdown = md(
        html_content,
        heading_style="ATX",  # Use # for headings
        table_infer_header=True,  # Auto-detect table headers
        bullets="*",  # Use * for lists
        strong_em_symbol="*",  # Use * for bold/italic
        escape_asterisks=False,  # Preserve Markdown syntax
        convert=["h1", "h2", "h3", "h4", "h5", "h6", "p", "table", "ul", "ol", "a", "strong", "em"]  # Handle common HTML tags
    )
    
    # Display the converted Markdown
    st.subheader("Converted Markdown")
    st.text_area("Markdown Output", markdown, height=300)
    
    # Allow user to choose file format for download
    file_format = st.selectbox("Download as", ["Markdown (.md)", "Text (.txt)"])
    file_extension = ".md" if file_format == "Markdown (.md)" else ".txt"
    
    # Use uploaded file's base name
    base_name = os.path.splitext(uploaded_file.name)[0]  # Get filename without extension
    file_name = f"{base_name}_{'md' if file_extension == '.md' else 'txt'}{file_extension}"
    
    # Provide download button
    st.download_button(
        label=f"Download as {file_extension}",
        data=markdown,
        file_name=file_name,
        mime="text/markdown" if file_extension == ".md" else "text/plain"
    )
    
    # Inform user about download location
    st.info(
        f"The file will download to your browser's default download folder (e.g., Downloads). "
        f"To save it in the same directory as your uploaded file ({uploaded_file.name}), "
        f"move the downloaded file ({file_name}) manually to that location."
    )
