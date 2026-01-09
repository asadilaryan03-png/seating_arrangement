# Streamlit Version - Seating Arrangement System

## 🎓 Complete Streamlit Implementation

This is a modern Streamlit-based version of the Seating Arrangement System with the same features as the Flask version.

### What is Streamlit?

Streamlit is a Python library that turns data scripts into shareable web apps instantly. It's perfect for:
- Rapid development
- Interactive dashboards
- Data processing applications
- Easy deployment

---

## 🚀 Quick Start

### Installation

```powershell
# Run installation
.\install_streamlit.bat

# Or manually:
pip install -r requirements.txt
```

### Running the App

```powershell
# Method 1: Use batch file (Easiest)
.\run_streamlit.bat

# Method 2: Manual command
streamlit run streamlit_app.py

# Method 3: Without browser opening
streamlit run streamlit_app.py --logger.level=error
```

The app will open at: **http://localhost:8501**

---

## ✨ Features

### Upload & Processing
- ✅ Drag & drop CSV file upload
- ✅ Automatic branch code extraction
- ✅ Student sorting by branch
- ✅ Real-time processing feedback
- ✅ Error handling with helpful messages

### Data Display
- ✅ Statistics dashboard (total students, blocks, etc.)
- ✅ Tabbed interface (one tab per block)
- ✅ Collapsible student list per block
- ✅ Professional table formatting
- ✅ Branch and class information

### Export Options
- ✅ PDF export (full or per-block)
- ✅ Excel export (full or per-block)
- ✅ Download buttons with date/time stamp
- ✅ Both full report and individual block exports

### User Interface
- ✅ Responsive design
- ✅ Sidebar with system information
- ✅ Usage instructions
- ✅ Status indicators and feedback
- ✅ Professional styling

---

## 📁 Project Structure - Streamlit Version

```
seating_arrangement/
├── streamlit_app.py              ← Main Streamlit application
├── seating_processor.py          ← CSV processing (same as Flask)
├── export_manager.py             ← PDF/Excel export (same as Flask)
├── config.py                     ← Configuration settings
├── requirements.txt              ← Python dependencies (updated)
├── install_streamlit.bat         ← Installation script
├── run_streamlit.bat             ← Run script
├── Sample_seating_plan.csv       ← Reference data
├── app.py                        ← Original Flask app (still available)
├── install.bat                   ← Flask installer (still available)
├── run.bat                       ← Flask runner (still available)
└── templates/                    ← Flask templates (still available)
    └── index.html
```

---

## 🎯 How to Use

### Step 1: Upload CSV File

```
1. Click on "Select CSV file" box
2. Choose your CSV file from your computer
3. Or drag & drop the file
```

**CSV Format Required:**
```csv
Sr No.,PRN,Name,Branch,Year ,College Code
1,2506321111242018,STUDENT NAME,CSE,2,6321-VVPIET
```

### Step 2: Process File

```
1. Click "🔄 Process File" button
2. Wait for processing (shows spinner)
3. See success message and balloons
```

### Step 3: Review Results

```
1. See statistics at top (Total Students, Blocks, etc.)
2. Click on Block tabs to view each block
3. Check "Show students" to see full student list
4. Verify desk assignments and PRN ranges
```

### Step 4: Download Reports

**Individual Block Export:**
```
In each block tab:
- Click "📄 PDF - Block-X" button
- Or click "📊 Excel - Block-X" button
- Click download button in confirmation
```

**Full Report Export:**
```
At bottom of page:
- Click "📄 Generate Full PDF" button
- Or click "📊 Generate Full Excel" button
- Click download button
- Files saved with timestamp
```

---

## 📊 Comparison: Flask vs Streamlit

| Aspect | Flask | Streamlit |
|--------|-------|-----------|
| Setup | More code | Simpler |
| UI Development | Manual HTML/CSS | Automatic |
| Deployment | More complex | Easier |
| Performance | Faster | Slightly slower |
| Learning Curve | Steeper | Easier |
| Customization | More options | Limited |
| State Management | Manual | Automatic (session_state) |
| Real-time Updates | Polling/WebSocket | Built-in |

**Choose Flask if:** You need high performance or custom UI
**Choose Streamlit if:** You want rapid development and easy deployment

---

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Number of students per block
STUDENTS_PER_BLOCK = 30

# Institution name
INSTITUTION_NAME = "V. V. P. Institute of Engineering & Technology, Solapur"

# Center code
CENTER_CODE = "6321"

# Branch codes
BRANCH_CODES = {
    '11995': 'AI & DS',
    '11191': 'Civil',
    '11242': 'CSE',
    '11293': 'Elect',
    '11372': 'ENTC',
    '11612': 'Mech'
}
```

---

## 🌐 Streamlit Features Used

### Page Configuration
```python
st.set_page_config(
    page_title="...",
    page_icon="🎓",
    layout="wide"
)
```

### Session State
```python
st.session_state.processed_data  # Persist data between reruns
st.session_state.filename
```

### Columns Layout
```python
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Title", value)
```

### Tabs
```python
tabs = st.tabs([f"Block {i+1}" for i in range(len(blocks))])
for tab, block in zip(tabs, blocks):
    with tab:
        st.write(block)
```

### File Upload
```python
uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
```

### Download Button
```python
st.download_button(
    label="Download",
    data=file_buffer,
    file_name="report.pdf",
    mime="application/pdf"
)
```

### Feedback
```python
st.success("Success!")
st.error("Error!")
st.warning("Warning!")
st.info("Information")
st.spinner("Loading...")
st.balloons()
```

---

## 📈 Performance Characteristics

**Streamlit Benefits:**
- No need to write HTML/CSS/JavaScript
- Automatic reruns on input changes
- Built-in caching with @st.cache_data
- Real-time interactivity

**Considerations:**
- Full page reruns on interaction
- Can be slower for large datasets
- Limited customization of UI
- Different state management than traditional web apps

---

## 🔒 Session State in Streamlit

```python
# Initialize
if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None

# Use
st.session_state.processed_data = data

# Access
if st.session_state.processed_data:
    data = st.session_state.processed_data
```

This persists data across button clicks and user interactions.

---

## 🚀 Running the Application

### Option 1: Batch File (Windows)
```
Double-click: run_streamlit.bat
```

### Option 2: Command Line
```powershell
streamlit run streamlit_app.py
```

### Option 3: From Python Directory
```powershell
python -m streamlit run streamlit_app.py
```

### Option 4: Without Opening Browser
```powershell
streamlit run streamlit_app.py --logger.level=error
```

---

## 🌍 Accessing the App

**Local Machine:**
```
http://localhost:8501
```

**On Network (if configured):**
```
http://<your-ip>:8501
```

**In VS Code:**
```
Port 8501 will be detected and button provided
```

---

## 📦 Required Libraries

All included in `requirements.txt`:

```
streamlit==1.28.1        # Web framework
pandas==2.0.3            # Data processing
reportlab==4.0.4         # PDF generation
openpyxl==3.1.2          # Excel generation
Flask==2.3.2             # Optional (for Flask version)
Werkzeug==2.3.6          # Flask dependency
```

---

## 🔄 App Flow

```
1. User loads http://localhost:8501
2. Sidebar displays system info
3. Main area shows file upload
4. User uploads CSV
5. Click "Process File"
6. App processes and displays results
7. Results persist in session_state
8. User clicks tabs to view blocks
9. User can toggle student list visibility
10. User clicks export buttons
11. Files download to computer
```

---

## ✅ Development Advantages

### Quick Development
- Write Python, get web app instantly
- No HTML/CSS/JavaScript needed
- Automatic layout management

### Easy Debugging
```python
st.write(variable)  # Debug output
st.dataframe(df)    # Pretty table display
st.json(dict)       # JSON viewer
```

### Interactive Testing
- Change code, save file
- App reloads automatically
- Test immediately

---

## 🎨 Styling in Streamlit

### Markdown
```python
st.markdown("# Title")
st.markdown("**Bold text**")
st.markdown("- Bullet 1")
```

### HTML
```python
st.markdown("""
    <style>
    .container { color: blue; }
    </style>
    """, unsafe_allow_html=True)
```

### Columns
```python
col1, col2 = st.columns(2)
with col1:
    st.write("Left")
with col2:
    st.write("Right")
```

---

## 📊 Data Display Options

### Table
```python
st.dataframe(df)           # Interactive
st.table(df)               # Static
```

### Metrics
```python
st.metric("Label", 100, "+5")
```

### Charts
```python
st.bar_chart(data)
st.line_chart(data)
```

### Columns
```python
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total", 100)
```

---

## 🔧 Troubleshooting Streamlit

### Issue: "streamlit command not found"
```
Solution: pip install streamlit
```

### Issue: "Port 8501 already in use"
```
streamlit run app.py --server.port=8502
```

### Issue: "App keeps rerunning"
```
Use @st.cache_data for expensive operations
Or use st.session_state for state management
```

### Issue: "Can't find module"
```
pip install -r requirements.txt
```

---

## 🌐 Deployment Options

### Local
```
streamlit run streamlit_app.py
```

### Server
```bash
nohup streamlit run streamlit_app.py &
```

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD streamlit run streamlit_app.py --server.port=8501
```

### Streamlit Cloud
```
1. Push to GitHub
2. Deploy on Streamlit Cloud
3. App runs automatically
```

---

## 📚 Key Differences from Flask Version

| Feature | Flask | Streamlit |
|---------|-------|-----------|
| File Routes | @app.route() | st.file_uploader() |
| Display Data | JSON → HTML | st.write() |
| User Input | Forms | Widgets (st.button, etc) |
| State | Request/Session | st.session_state |
| CSS | Custom | Built-in theming |
| Deploy | Server needed | Streamlit Cloud |

---

## 💡 Tips for Using Streamlit

1. **Use Caching for Speed**
```python
@st.cache_data
def load_data():
    return expensive_operation()
```

2. **Use Session State for Persistence**
```python
if 'data' not in st.session_state:
    st.session_state.data = None
```

3. **Organize with Containers**
```python
with st.container():
    st.write("Organized content")
```

4. **Use Columns for Layout**
```python
col1, col2 = st.columns(2)
```

5. **Add Interactivity with Widgets**
```python
if st.button("Click me"):
    st.write("Button clicked!")
```

---

## 🎓 Running Both Versions

You can run **both Flask and Streamlit** simultaneously:

```powershell
# Terminal 1: Flask
python app.py                # http://localhost:5000

# Terminal 2: Streamlit  
streamlit run streamlit_app.py  # http://localhost:8501
```

Different ports prevent conflicts!

---

## 📞 Support

Refer to:
- `QUICKSTART.md` - Quick start guide
- `README.md` - Complete documentation
- `TECHNICAL.md` - Technical details
- Streamlit docs: https://docs.streamlit.io

---

## ✨ Summary

**Streamlit Version Advantages:**
✅ Simpler to develop
✅ Faster to deploy
✅ Easier to maintain
✅ Perfect for data apps
✅ No HTML/CSS needed

**When to Use:**
- Internal tools
- Data dashboards
- Rapid prototyping
- Team collaboration
- Quick deployments

---

**Ready to use! Run: `run_streamlit.bat`**
