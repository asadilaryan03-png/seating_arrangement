# Quick Start Guide - Seating Arrangement System

## 🚀 Quick Setup (2 minutes)

### Step 1: Install Dependencies
Open PowerShell in the project folder and run:
```powershell
pip install -r requirements.txt
```

### Step 2: Start the Application
```powershell
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser
Visit: **http://localhost:5000**

---

## 📋 How to Use

### 1. Upload CSV File
- Click the upload area or drag and drop your CSV file
- Supported format: CSV with student data
- Use `Sample_seating_plan.csv` as reference

### 2. Process Students
- Click "Upload & Process" button
- System will:
  - Extract branch codes from PRN
  - Sort students by branch
  - Create blocks of 30 students each
  - Assign desk numbers

### 3. Review Arrangement
- View total students and blocks created
- Click "Show Students" to see detailed list
- Verify desk assignments and PRN ranges

### 4. Download Report
Choose format:
- **PDF**: Professional formatted report with all details
- **Excel**: Spreadsheet with styled tables

---

## 📊 What Gets Generated

### PDF Report Includes:
- Institution name (bold)
- Exam type and year
- Center code: 6321
- Block information
- Student count
- PRN ranges
- Branch details
- Seating table (Desk No. & PRN pairs)

### Excel Report Includes:
- Separate sheets for each block
- Formatted headers (bold)
- Bordered tables
- Center code and dates
- Student seating arrangement

---

## 🔧 File Structure

```
project/
├── app.py                    ← Main Flask application
├── seating_processor.py      ← Student processing logic
├── export_manager.py         ← PDF/Excel generation
├── requirements.txt          ← Dependencies
├── Sample_seating_plan.csv   ← Reference CSV
├── README.md                 ← Full documentation
└── templates/
    └── index.html           ← Web interface
```

---

## 🌿 Branch Code Reference

| PRN Digits 10-15 | Branch   |
|------------------|----------|
| 11995            | AI & DS  |
| 11191            | Civil    |
| 11242            | CSE      |
| 11293            | Elect    |
| 11372            | ENTC     |
| 11612            | Mech     |

**Note**: PRN format: `2506321111242018`
- Positions 10-15: `111242` → CSE branch

---

## ✅ Features

✓ Drag & drop file upload
✓ Automatic branch detection
✓ 30 students per block
✓ Automatic desk numbering (1-30)
✓ PDF export with formatting
✓ Excel export with styling
✓ Responsive web interface
✓ Real-time processing
✓ Error handling & validation

---

## 🆘 Troubleshooting

### Issue: Python not found
**Solution**: Ensure Python is installed and in PATH
```powershell
python --version
```

### Issue: Module not found errors
**Solution**: Reinstall dependencies
```powershell
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Issue: Port 5000 already in use
**Solution**: Edit `app.py` last line and change port:
```python
app.run(debug=True, port=5001)
```

### Issue: CSV processing error
**Solution**: Verify CSV has required columns:
- Sr No.
- PRN
- Name
- Branch
- Year
- College Code

---

## 📝 Example CSV Format

```
Sr No.,PRN,Name,Branch,Year ,College Code
1,2506321111242018,CHAVAN MAYURI SHAMRAO,CSE,1,6321-VVPIET
2,2506321111242033,KADAM KOMAL KHANDU,CSE,1,6321-VVPIET
3,2506321111191043,STUDENT NAME,Civil,1,6321-VVPIET
```

---

## 💡 Tips

1. **Always use sample CSV as reference** for proper formatting
2. **Verify branch codes** in PRN before uploading
3. **Check internet** (not needed for local use)
4. **Keep CSV file under 5MB** for optimal performance
5. **Invalid branch codes are automatically filtered** - check logs if students are missing

---

## 📞 Support

For issues:
1. Check README.md for detailed documentation
2. Verify CSV file format matches example
3. Ensure all required columns are present
4. Check Python and module versions

---

**System Ready!** You can now start creating seating arrangements. 🎓
