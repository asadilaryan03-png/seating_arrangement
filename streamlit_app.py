import streamlit as st
import pandas as pd
import os
import sys
import signal
from datetime import datetime
from seating_processor import SeatingProcessor
from export_manager import ExportManager

# Prevent signal handler errors in non-main threads
if sys.platform != 'win32':
    try:
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except Exception:
        pass

# Page configuration
st.set_page_config(page_title="Seating Arrangement System", layout="wide")

# Initialize session state
if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None

# Title
st.title("Seating Arrangement System")

# Sidebar
with st.sidebar:
    st.header("Supported Branches")
    st.write("""
    - AI & DS (11995)
    - BCA (11101)
    - Civil (11191)
    - CSE (11242)
    - Electrical (11293)
    - ENTC (11372)
    - MCA (22241)
    - Mechanical (11612)
    """)

# File upload
st.subheader("Upload CSV File")
uploaded_file = st.file_uploader("Select CSV file", type=['csv'])

if uploaded_file is not None:
    if st.button("Process File"):
        try:
            with st.spinner("Processing..."):
                # Save temporarily
                temp_file = "temp_upload.csv"
                with open(temp_file, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Process data
                branch_codes = {
                    '11995': 'AI & DS',
                    '11101': 'BCA',
                    '11191': 'Civil',
                    '11242': 'CSE',
                    '11293': 'Elect',
                    '11372': 'ENTC',
                    '22241': 'MCA',
                    '11612': 'Mech'
                }
                
                processor = SeatingProcessor(temp_file, branch_codes)
                st.session_state.processed_data = processor.process()
                
                # Clean up temp file
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                
                st.success("File processed successfully!")
        
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display results
if st.session_state.processed_data:
    data = st.session_state.processed_data
    
    st.subheader("Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", data['totalStudents'])
    with col2:
        st.metric("Total Blocks", len(data['blocks']))
    with col3:
        st.metric("Students per Block", 30)
    
    st.divider()
    
    # Display blocks
    st.subheader("Seating Blocks")
    
    if data.get('blocks') and len(data['blocks']) > 0:
        tabs = st.tabs([f"Block {block['blockName']}" for block in data['blocks']])
        
        for tab_idx, tab in enumerate(tabs):
            with tab:
                block = data['blocks'][tab_idx]
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Students:** {block['totalStudents']}")
                    st.write(f"**Branch:** {block['branch']}")
                with col2:
                    st.write(f"**Year:** {block['year']}")
                    st.write(f"**PRN Range:** {block['prnFrom']} → {block['prnTo']}")
                
                # Student table
                students_data = []
                for student in block['students']:
                    students_data.append({
                        'Desk No.': student['deskNo'],
                        'PRN': student['prn'],
                        'Name': student['name'],
                        'Branch': student['branch'],
                        'Year': student['year']
                    })
                
                st.dataframe(pd.DataFrame(students_data), use_container_width=True, hide_index=True)
                
                # Export options
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"PDF - {block['blockName']}", key=f"pdf_{tab_idx}"):
                        pdf_buffer = ExportManager.generate_pdf({'blocks': [block]})
                        st.download_button(
                            label=f"Download {block['blockName']}.pdf",
                            data=pdf_buffer,
                            file_name=f"block_{block['blockName']}.pdf",
                            mime="application/pdf",
                            key=f"pdf_dl_{tab_idx}"
                        )
                
                with col2:
                    if st.button(f"Excel - {block['blockName']}", key=f"excel_{tab_idx}"):
                        excel_buffer = ExportManager.generate_excel({'blocks': [block]})
                        st.download_button(
                            label=f"Download {block['blockName']}.xlsx",
                            data=excel_buffer,
                            file_name=f"block_{block['blockName']}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            key=f"excel_dl_{tab_idx}"
                        )
else:
    st.warning("No seating blocks generated. Check CSV format and branch codes.")
    if st.session_state.processed_data:
        debug = st.session_state.processed_data.get('debug', {})
        with st.expander("📋 Debug Information"):
            st.write(f"**Rows before filtering:** {debug.get('rows_before_filter', 'N/A')}")
            st.write(f"**Rows after filtering:** {debug.get('rows_after_filter', 'N/A')}")
            st.write(f"**Recognized branch codes:** {', '.join(debug.get('recognized_branch_codes', []))}")
            st.info("If 'Rows after filtering' is much lower than expected, your PRN values might not contain the branch codes listed above. Please verify the PRN format in your CSV file.")
    
    st.divider()
    
    # Full export
    st.subheader("Export All Blocks")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Generate Full PDF"):
            pdf_buffer = ExportManager.generate_pdf(data)
            st.download_button(
                label="Download Full Report (PDF)",
                data=pdf_buffer,
                file_name=f"seating_arrangement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf",
                key="full_pdf_download"
            )
    
    with col2:
        if st.button("Generate Full Excel"):
            excel_buffer = ExportManager.generate_excel(data)
            st.download_button(
                label="Download Full Report (Excel)",
                data=excel_buffer,
                file_name=f"seating_arrangement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="full_excel_download"
            )
else:
    st.info("Upload a CSV file to get started")
