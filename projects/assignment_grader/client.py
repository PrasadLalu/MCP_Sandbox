import streamlit as st

import os
import tempfile


st.set_page_config(
    layout="wide",
    page_icon="📝",
    page_title="Assignment Grader",
)

# Main title
st.title("📝 Assignment Grader")
st.markdown("Upload assignment and grade them automatically using AI.")

# Sidebar setup
st.sidebar.header("About")
st.sidebar.info(
    """This is a demo of the Assignment Grader using FastMCP and OpenAI.
    Upload assignments in PDF or DOCX format, set your grading rubric, 
    and get instant AI-powered grades with detailed feedback."""
)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Upload Assignment", "Grade Assignment", "Results"])

# Tab 1: Upload Assignment
with tab1:
    st.header("Upload Assignment")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])

    if uploaded_file is not None:
        # Display file information
        file_size = len(uploaded_file.getvalue()) / 1024  # KB
        st.info(f"File: {uploaded_file.name} ({file_size:.1f} KB)")

        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            file_path = tmp_file.name

        st.session_state["file_path"] = file_path
        st.session_state["file_name"] = uploaded_file.name

        # Parse the document
        if st.button("Process Document"):
            with st.spinner("Processing document..."):
                print("document processing...")
