# SEATING ARRANGEMENT SYSTEM - COMPLETE SETUP GUIDE

## 📋 System Overview

This is a complete web-based seating arrangement management system for **V. V. P. Institute of Engineering & Technology, Solapur**.

### ✨ Key Features

1. **CSV File Upload** - Upload student data in CSV format
2. **Automatic Branch Detection** - Extract and validate branch codes from PRN
3. **Smart Block Creation** - Automatically creates blocks with 30 students each
4. **Desk Assignment** - Assigns unique desk numbers (1-30 per block)
5. **PDF Export** - Professional formatted PDF reports with:
   - Bold titles and headers
   - Formatted tables
   - Institution details
   - Exam information
   - Student seating arrangement

6. **Excel Export** - Spreadsheet export with:
   - Styled headers and borders
   - Multiple sheets (one per block)
   - Professional formatting
   - Easy sharing and editing

---

## 🔧 System Architecture

```
User Interface (HTML/CSS/JavaScript)
          ↓
   Flask Web Server
          ↓
CSV Processing Engine
  ├── Branch Detection
  ├── Student Sorting
  └── Block Creation
          ↓
Export Managers
  ├── PDF Generator
  └── Excel Generator
```

---

## 📁 File Structure

```
seating_arrangement/
│
├── Core Application Files
│   ├── app.py                      # Main Flask application
│   ├── seating_processor.py        # CSV processing & block creation
│   ├── export_manager.py           # PDF & Excel export
│   └── config.py                   # Configuration settings
│
├── Web Interface
│   └── templates/
│       └── index.html              # Web UI (responsive design)
│
├── Data & Configuration
│   ├── requirements.txt            # Python dependencies
│   ├── Sample_seating_plan.csv    # Reference CSV format
│   └── uploads/                    # Temporary file storage
│
├── Setup & Running
│   ├── install.bat                 # Windows installation script
│   ├── run.bat                     # Windows run script
│   ├── QUICKSTART.md              # Quick setup guide
│   ├── README.md                   # Full documentation
│   ├── SETUP.md                    # This file
│   └── LICENSE                     # License info
│
└── Runtime Files
    └── .gitignore                  # Git ignore file
```

---

## 🚀 Installation Steps

### Step 1: Prerequisites Check

Verify you have:
- Windows OS (XP/7/8/10/11)
- Python 3.7 or higher installed
- Internet connection (for first installation)
- ~200MB free disk space

**Check Python Installation:**
```powershell
python --version
```

Should show: `Python 3.x.x`

---

### Step 2: Automatic Installation (Recommended)

1. Navigate to the project folder
2. Double-click `install.bat`
3. Wait for installation to complete
4. Press any key to close

**What it does:**
- Verifies Python installation
- Installs all required packages
- Creates necessary directories
- Validates package imports

---

### Step 3: Manual Installation (If needed)

If `install.bat` doesn't work:

```powershell
# Open PowerShell in project folder

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import flask, pandas, reportlab, openpyxl; print('OK')"
```

---

## ▶️ Running the Application

### Method 1: Batch File (Easy)
Double-click `run.bat` and wait for the browser to open.

### Method 2: Manual Start
```powershell
python app.py
```

### Method 3: Background Service
```powershell
Start-Process python app.py -WindowStyle Hidden
```

---

## 🌐 Accessing the Application

Once running, open your browser and go to:

```
http://localhost:5000
```

or

```
http://127.0.0.1:5000
```

---

## 📖 Using the System

### Step-by-Step Guide

#### 1. Upload CSV File

**Location:** Main upload section on the web page

**Options:**
- Click the upload area
- Drag and drop a CSV file
- File must be in correct format

**Supported Formats:**
```
Sr No., PRN, Name, Branch, Year, College Code
1, 2506321111242018, STUDENT NAME, CSE, 1, 6321-VVPIET
```

#### 2. Process File

Click "Upload & Process" button

**System checks:**
- File is valid CSV
- Has required columns
- Contains valid PRN numbers
- Branch codes are recognized

**Results shown:**
- Total students count
- Number of blocks created
- Students per block

#### 3. Review Seating Arrangement

- View block-wise breakdown
- Click "Show Students" to see details
- Check desk assignments
- Verify PRN ranges

#### 4. Download Report

**PDF Download:**
- Contains formatted tables
- Professional appearance
- Print-ready format
- All student details included

**Excel Download:**
- Spreadsheet format
- Separate sheet per block
- Styled tables with borders
- Easy to edit and share

---

## 📊 Branch Code Reference

System recognizes 6 engineering branches based on PRN:

| PRN Codes | Branch Name     | Code |
|-----------|-----------------|------|
| 11995     | AI & DS         | CSE  |
| 11191     | Civil           | CIVIL|
| 11242     | CSE             | CSE  |
| 11293     | Electrical      | ELEC |
| 11372     | ENTC            | ENTC |
| 11612     | Mechanical      | MECH |

**How Branch is Detected:**
```
PRN: 2506321111242018
    └─────┬─────┘
Position 10-15 = 111242 → CSE Branch
```

---

## 📋 CSV File Requirements

### Required Columns

| Column Name  | Description                    | Example           |
|--------------|--------------------------------|-------------------|
| Sr No.       | Serial number                  | 1, 2, 3...        |
| PRN          | 16-digit PRN (must be valid)   | 2506321111242018  |
| Name         | Student full name              | JOHN DOE          |
| Branch       | Branch name                    | CSE, MECH, etc.   |
| Year         | Academic year                  | 1, 2, 3, 4        |
| College Code | Institution code               | 6321-VVPIET       |

### Sample CSV Content

```csv
Sr No.,PRN,Name,Branch,Year ,College Code
1,2506321111242018,CHAVAN MAYURI SHAMRAO,CSE,1,6321-VVPIET
2,2506321111242033,KADAM KOMAL KHANDU,CSE,1,6321-VVPIET
3,2506321111191043,SAMPLE STUDENT,Civil,2,6321-VVPIET
4,2506321111612019,ANOTHER STUDENT,Mech,1,6321-VVPIET
```

---

## 🎯 Configuration

Edit `config.py` to customize:

```python
# Number of students per block
STUDENTS_PER_BLOCK = 30

# Institution name (shown in reports)
INSTITUTION_NAME = "V. V. P. Institute of Engineering & Technology, Solapur"

# Center code (shown in reports)
CENTER_CODE = "6321"

# Flask server settings
FLASK_PORT = 5000
FLASK_DEBUG = True
```

---

## 📥 Output Format

### PDF Report Structure

```
V. V. P. Institute of Engineering & Technology, Solapur

Winter Examination 2025

Center Code: 6321                    Date: ___________     Block Name: Block-1
Total Students in Block: 30          PRN No.: From 2018 to 2054
Class: 2nd Year                      Branch: CSE

[Seating Table with Desk Numbers and PRN Numbers]
```

### Excel Report Structure

**Sheet per Block:**
- Row 1: Institution Name (Bold, Centered)
- Row 2: Exam Type and Year (Bold, Centered)
- Row 3: Header Information (Center Code, Date, Block Name)
- Row 4: Student Count and PRN Range
- Row 5: Class and Branch Info
- Rows 6+: Seating Table with Desk No. and PRN

---

## 🔍 Troubleshooting

### Issue: "Python is not installed"

**Solution:**
1. Download Python from python.org
2. Run installer
3. **✓ Check "Add Python to PATH"**
4. Restart computer
5. Try again

### Issue: "ModuleNotFoundError"

**Solution:**
```powershell
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Issue: "Port 5000 already in use"

**Solution - Option 1:**
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Solution - Option 2:**
Edit `app.py`, change:
```python
app.run(debug=True, port=5001)  # Change 5000 to 5001
```

### Issue: "CSV file not accepted"

**Checklist:**
- [ ] File is .csv format
- [ ] Has all required columns
- [ ] No special characters in column names
- [ ] PRN has 16 digits
- [ ] Branch codes are valid (11995, 11191, 11242, etc.)

### Issue: "No students shown in results"

**Possible Causes:**
1. All PRN branch codes are invalid
2. CSV has wrong branch code positions
3. Column names don't match exactly

**Solution:**
- Check sample CSV format
- Verify PRN format (16 digits)
- Ensure branch codes are at positions 10-15

---

## 🆘 Getting Help

### Check Documentation
1. README.md - Full system documentation
2. QUICKSTART.md - Quick setup guide
3. config.py - Configuration options
4. This file - Complete setup guide

### Common Issues Resolution

**Q: Browser shows "Connection refused"**
A: Flask server is not running. Execute `python app.py`

**Q: Upload button doesn't work**
A: Check browser console (F12) for JavaScript errors

**Q: Downloaded file is empty**
A: Ensure seating data is processed before export

**Q: PRN codes not recognized**
A: Verify branch codes are valid (see reference table)

---

## 🔐 Security Notes

- Application runs locally (not on internet by default)
- Uploaded files are temporary (in `uploads/` folder)
- No data is stored permanently
- Remove sensitive data from CSV before sharing

---

## 📝 Best Practices

1. **Always backup** original CSV files
2. **Test** with sample CSV first
3. **Verify** output before printing
4. **Use unique PRN numbers** (no duplicates)
5. **Keep CSV format consistent**
6. **Run latest Python version**
7. **Clear uploads folder** regularly

---

## 🚀 Advanced Usage

### Custom Branch Codes

Edit `config.py`:
```python
BRANCH_CODES = {
    '11995': 'AI & DS',
    '11191': 'Civil',
    '11242': 'CSE',
    # Add more as needed
}
```

### Change Block Size

Edit `config.py`:
```python
STUDENTS_PER_BLOCK = 25  # Change from 30 to 25
```

### Modify Port

Edit `app.py` last line:
```python
app.run(debug=True, port=8000)  # Change from 5000
```

---

## 📞 Support & Contact

For technical issues:
1. Check this setup guide
2. Review README.md
3. Check application logs
4. Verify Python installation
5. Reinstall dependencies

---

## ✅ Verification Checklist

Before using in production:

- [ ] Python 3.7+ installed
- [ ] All packages from requirements.txt installed
- [ ] `uploads/` folder exists
- [ ] Sample CSV processed successfully
- [ ] PDF export works
- [ ] Excel export works
- [ ] Web interface displays correctly
- [ ] Browser compatibility tested
- [ ] Network access configured (if needed)

---

## 📄 License & Credits

**System:** Seating Arrangement Management System
**Institution:** V. V. P. Institute of Engineering & Technology, Solapur
**Version:** 1.0
**Last Updated:** November 2025

---

## 🎓 Educational Use

This system is designed for:
- Managing examination seating arrangements
- Allocating desks based on branch
- Generating professional reports
- Maintaining exam records

---

**System Setup Complete!** 🎉

You are now ready to create seating arrangements for your examination.

For quick start, see: `QUICKSTART.md`
For detailed info, see: `README.md`
