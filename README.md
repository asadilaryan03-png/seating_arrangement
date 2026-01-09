# Seating Arrangement System
## V. V. P. Institute of Engineering & Technology, Solapur

A comprehensive web-based system for managing examination seating arrangements with automatic student allocation based on branch codes.

### Features

- ✅ **CSV File Upload**: Upload student data in CSV format
- ✅ **Automatic Branch Sorting**: Extract branch codes from PRN and sort accordingly
- ✅ **Block Management**: Automatically creates examination blocks with 30 students each
- ✅ **Desk Assignment**: Assigns desk numbers for each student
- ✅ **PDF Export**: Generate professional PDF reports with formatted tables
- ✅ **Excel Export**: Generate Excel files with styled tables and borders
- ✅ **Responsive Design**: Works on desktop and mobile devices

### Branch Codes

The system recognizes the following branch codes from PRN numbers:

| Code  | Branch       |
|-------|--------------|
| 11995 | AI & DS      |
| 11191 | Civil        |
| 11242 | CSE          |
| 11293 | Elect        |
| 11372 | ENTC         |
| 11612 | Mech         |

### Installation

1. **Clone or download the project**
   ```bash
   cd seating_arrangement
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to: `http://localhost:5000`

3. **Upload CSV file**
   - Click on the upload area or drag and drop your CSV file
   - Click "Upload & Process" button
   - The system will process the file and display results

4. **View seating arrangement**
   - Review blocks and students in the displayed interface
   - Click "Show Students" to view detailed student information

5. **Download reports**
   - Click "Download as PDF" for formatted PDF report
   - Click "Download as Excel" for Excel spreadsheet

### CSV File Format

Your CSV file should have the following columns:

| Column          | Description                |
|-----------------|---------------------------|
| Sr No.          | Serial number             |
| PRN             | 16-digit PRN number       |
| Name            | Student name              |
| Branch          | Branch name (auto-filled) |
| Year            | Academic year             |
| College Code    | Institution code          |

**Example:**
```csv
Sr No.,PRN,Name,Branch,Year ,College Code
1,2506321111242018,CHAVAN MAYURI SHAMRAO,CSE,1,6321-VVPIET
```

### File Structure

```
seating_arrangement/
├── app.py                    # Main Flask application
├── seating_processor.py      # CSV processing logic
├── export_manager.py         # PDF/Excel export functionality
├── requirements.txt          # Python dependencies
├── Sample_seating_plan.csv   # Sample CSV file
├── templates/
│   └── index.html           # Web interface
└── uploads/                  # Temporary upload storage
```

### How It Works

1. **Upload**: User uploads a CSV file containing student data
2. **Processing**: System extracts branch codes from PRN numbers (5-digit code at position 10-15)
3. **Sorting**: Students are sorted by branch code
4. **Block Creation**: Creates blocks with maximum 30 students each
5. **Export**: Generates PDF/Excel with formatted examination seating layout

### Output Format

The exported documents include:

- **Institute Name** (Bold)
- **Exam Type** (Winter/Summer) (Bold)
- **Center Code**: 6321
- **Date**: Blank space for manual entry
- **Block Name**: Block-1, Block-2, etc.
- **Total Students**: Count of students in block
- **PRN Range**: From and To PRN numbers
- **Class**: Academic year
- **Branch**: Department code
- **Seating Table**: Desk numbers with corresponding PRN numbers

### System Requirements

- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- 100MB disk space for dependencies

### Troubleshooting

**Problem**: "File is not valid CSV"
- Solution: Ensure your CSV file is properly formatted and uses comma as delimiter

**Problem**: "No valid students found"
- Solution: Check that PRN numbers contain valid branch codes (11995, 11191, 11242, 11293, 11372, 11612)

**Problem**: "Port 5000 already in use"
- Solution: Modify the port in `app.py` line: `app.run(debug=True, port=5001)`

### License

This system is designed for educational purposes at V. V. P. Institute of Engineering & Technology, Solapur.

### Support

For issues or feature requests, please contact the administration office.
