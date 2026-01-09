# Technical Architecture & Developer Guide

## 🏗️ System Architecture

### Layers

```
┌─────────────────────────────────────────────┐
│         User Interface Layer                │
│  (HTML/CSS/JavaScript - index.html)         │
└────────────────┬──────────────────────────┘
                 │
┌─────────────────▼──────────────────────────┐
│       Flask Web Server (app.py)             │
│  - Routes & HTTP Handlers                   │
│  - File Upload Management                   │
│  - Export Coordination                      │
└────────────────┬──────────────────────────┘
                 │
     ┌───────────┼────────────┐
     │           │            │
     ▼           ▼            ▼
┌─────────┐ ┌─────────┐ ┌──────────┐
│ Process │ │ Process │ │ Export   │
│ Module  │ │ Block   │ │ Manager  │
│(CSV)    │ │ Creator │ │(PDF/XLS) │
└─────────┘ └─────────┘ └──────────┘
```

### Key Components

#### 1. **app.py** - Main Application
- Flask server and routes
- File upload handling
- Request processing
- Response management

**Key Routes:**
- `GET /` - Main page
- `POST /upload` - File upload
- `POST /export/<format>` - Export handler

#### 2. **seating_processor.py** - Data Processing
- CSV file parsing
- Branch code extraction
- Student sorting
- Block creation logic

**Key Methods:**
- `extract_branch_code(prn)` - Extract 5-digit code
- `process()` - Main processing pipeline
- `create_blocks()` - Block allocation

#### 3. **export_manager.py** - Report Generation
- PDF document creation
- Excel workbook generation
- Table formatting
- Style management

**Key Methods:**
- `generate_pdf(data)` - Create PDF
- `generate_excel(data)` - Create Excel

#### 4. **index.html** - Web Interface
- File upload UI
- Result display
- Export buttons
- JavaScript processing

---

## 🔄 Data Flow

### Upload Process

```
1. User selects CSV file
   ↓
2. File sent to server (POST /upload)
   ↓
3. SeatingProcessor reads CSV
   ↓
4. Extract branch codes from PRN
   ↓
5. Validate branch codes
   ↓
6. Sort students by branch
   ↓
7. Create blocks (30 students each)
   ↓
8. Assign desk numbers
   ↓
9. Return processed data as JSON
   ↓
10. Display results in UI
```

### Export Process

```
1. User clicks Export button
   ↓
2. Processed data sent to server (POST /export/pdf or /export/excel)
   ↓
3. ExportManager generates document
   ↓
4. Format data into tables
   ↓
5. Apply styling and formatting
   ↓
6. Create binary file buffer
   ↓
7. Send as download to browser
   ↓
8. User saves file
```

---

## 📐 Algorithm Details

### Branch Code Extraction

**Source:** PRN (16 digits)
**Format:** `2506321111242018`

**Position Calculation:**
```
Position:  0-7        8-9    10-14  15
Value:     2506321    11     11242  018
           -------    --     -----  ---
           Date       Yr     Code   Seq
```

**Branch Code:** Positions 10-14 (5 digits) = `11242` → CSE

**Code in seating_processor.py:**
```python
def extract_branch_code(self, prn):
    if len(str(prn)) >= 12:
        return str(prn)[10:15]
    return None
```

### Block Creation Algorithm

**Input:** Sorted student list, block size (30)
**Process:**
```
Total Students: 95
Block Size: 30

Calculation:
num_blocks = ceil(95 / 30) = 4

Blocks:
  Block 1: Students 0-29   (30 students)
  Block 2: Students 30-59  (30 students)
  Block 3: Students 60-89  (30 students)
  Block 4: Students 90-94  (5 students)
```

**Code:**
```python
def create_blocks(self):
    students_per_block = 30
    total_students = len(self.df)
    num_blocks = (total_students + students_per_block - 1) // students_per_block
    
    for block_num in range(num_blocks):
        start_idx = block_num * students_per_block
        end_idx = min(start_idx + students_per_block, total_students)
        block_students = self.df.iloc[start_idx:end_idx]
```

### Desk Assignment

**Logic:**
```
For each block:
  For each student in block:
    DeskNo = (student_position_in_block) + 1

Example:
  Student 1 in Block 1 → Desk 1
  Student 2 in Block 1 → Desk 2
  ...
  Student 30 in Block 1 → Desk 30
  Student 1 in Block 2 → Desk 1
```

---

## 📦 Data Structures

### Input CSV Structure

```python
DataFrame columns:
  - Sr No.: int
  - PRN: str (16 digits)
  - Name: str
  - Branch: str
  - Year: int
  - College Code: str
  - BranchCode: str (extracted)
  - Branch: str (mapped)
  - DeskNo: int (assigned)
```

### Processed Data Structure (JSON)

```json
{
  "totalStudents": 95,
  "blocks": [
    {
      "blockNumber": 1,
      "blockName": "Block-1",
      "totalStudents": 30,
      "prnFrom": "2506321111242018",
      "prnTo": "2506321111242054",
      "year": 2,
      "branch": "CSE",
      "branchCode": "11242",
      "centerCode": "6321",
      "examType": "Winter Examination 2025",
      "date": "",
      "students": [
        {
          "deskNo": 1,
          "prn": "2506321111242018",
          "name": "STUDENT NAME",
          "branch": "CSE",
          "year": 2
        }
      ]
    }
  ],
  "timestamp": "2025-11-26T10:30:45.123456"
}
```

---

## 🎨 PDF Generation Details

### Using ReportLab

**Flow:**
```
1. Create SimpleDocTemplate with A4 size
2. Create styles (title, subtitle, normal)
3. For each block:
   a. Add block header
   b. Add student info
   c. Create desk table (3 columns)
   d. Add page break (if not last)
4. Build document
```

**Table Format:**
```
┌────────┬─────────┬────────┬─────────┬────────┬─────────┐
│Desk No.│ PRN No. │Desk No.│ PRN No. │Desk No.│ PRN No. │
├────────┼─────────┼────────┼─────────┼────────┼─────────┤
│   1    │ ...2018 │   11   │ ...2028 │   21   │ ...2038 │
│   2    │ ...2019 │   12   │ ...2029 │   22   │ ...2039 │
│  ...   │  ...    │  ...   │  ...    │  ...   │  ...    │
└────────┴─────────┴────────┴─────────┴────────┴─────────┘
```

### PDF Styling

```python
# Header formatting
- Font: Helvetica-Bold
- Size: 12pt
- Color: Black
- Alignment: Center

# Table header
- Background: Light Gray
- Font: Bold
- Color: Black

# Table cells
- Border: 1pt black
- Padding: 6pt
- Font: 8pt
```

---

## 📊 Excel Generation Details

### Using OpenPyXL

**Features:**
```
1. Create workbook
2. Create sheet per block (named "Block-1", "Block-2")
3. Merge cells for titles
4. Apply formatting:
   - Bold titles
   - Colored headers
   - Borders on all cells
   - Column widths
5. Fill data in tables
```

**Sheet Structure:**
```
Row 1:  [Institution Name (merged A1:F1)]
Row 2:  [Blank]
Row 3:  [Exam Type (merged A3:F3)]
Row 4:  [Blank]
Row 5:  [Center Code | Date | Block Name]
Row 6:  [Total Students | PRN Range]
Row 7:  [Class | Branch]
Row 8:  [Blank]
Row 9:  [Desk No. | PRN No. | (3 columns)]
Row 10+:[Student data...]
```

---

## 🔌 API Endpoints

### POST /upload

**Request:**
```
Form-data:
  file: <csv_file>

Content-Type: multipart/form-data
```

**Response Success (200):**
```json
{
  "success": true,
  "data": { /* Processed data structure */ },
  "filename": "seating_plan.csv"
}
```

**Response Error (400/500):**
```json
{
  "error": "Error message"
}
```

### POST /export/<format_type>

**Request:**
```
Body (JSON):
{
  "totalStudents": 95,
  "blocks": [ /* Block data */ ],
  "timestamp": "..."
}

Content-Type: application/json
Format: pdf or excel
```

**Response (200):**
```
Binary file (PDF or XLSX)
Headers:
  Content-Type: application/pdf or application/vnd.openxmlformats...
  Content-Disposition: attachment; filename="seating_arrangement_..."
```

---

## 🧪 Testing Guide

### Unit Test Example

```python
def test_branch_code_extraction():
    processor = SeatingProcessor('test.csv', BRANCH_CODES)
    prn = '2506321111242018'
    code = processor.extract_branch_code(prn)
    assert code == '11242'
    
def test_block_creation():
    # Create mock data
    mock_data = [ /* 95 students */ ]
    processor = SeatingProcessor('test.csv', BRANCH_CODES)
    processor.create_blocks()
    assert len(processor.blocks) == 4
    assert processor.blocks[0]['totalStudents'] == 30
```

### Integration Test Example

```python
def test_full_pipeline():
    # Upload CSV
    response = client.post('/upload', data={'file': open('test.csv')})
    assert response.status_code == 200
    
    # Export PDF
    response = client.post('/export/pdf', json=response.json['data'])
    assert response.status_code == 200
    assert response.content_type == 'application/pdf'
```

---

## 🔒 Error Handling

### Input Validation

```python
# CSV validation
- Check file exists
- Check file is CSV
- Check file size < 16MB
- Check required columns
- Check PRN format

# Data validation
- PRN has 16 digits
- Branch code valid
- Year is numeric
- No duplicate PRNs
```

### Error Messages

```
"File is not valid CSV" - Wrong format
"No file part" - File not provided
"Invalid branch codes" - No valid students
"Export failed" - Generation error
```

---

## 📈 Performance Considerations

### Optimization Tips

```python
# Use pandas for large datasets (1000+ rows)
# Vectorize operations where possible
# Cache processed data in session
# Limit concurrent uploads
# Use streaming for large exports
```

### Scalability

```
Current limits:
- File size: 16MB
- Students per block: 30
- Blocks per export: Unlimited

Improvements for scale:
- Database storage
- Queue system for exports
- Caching layer
- Pagination for UI
```

---

## 🚀 Deployment Guide

### Production Checklist

- [ ] Set `FLASK_DEBUG = False`
- [ ] Use production WSGI server (Gunicorn, uWSGI)
- [ ] Enable HTTPS
- [ ] Configure proper logging
- [ ] Add rate limiting
- [ ] Set up error monitoring
- [ ] Configure upload security
- [ ] Regular backups

### Docker Example

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "app:app"]
```

---

## 📝 Code Style & Conventions

### Python

```python
# Use PEP 8
# Class names: PascalCase
# Functions/vars: snake_case
# Constants: UPPERCASE
# Docstrings: Required for classes/functions
```

### JavaScript

```javascript
// Use camelCase for variables/functions
// Use const for constants
// Use arrow functions where appropriate
// Add comments for complex logic
```

---

## 🔗 Dependencies

### Python Libraries

| Library    | Version | Purpose               |
|------------|---------|----------------------|
| Flask      | 2.3.2   | Web framework         |
| pandas     | 2.0.3   | Data processing       |
| reportlab  | 4.0.4   | PDF generation        |
| openpyxl   | 3.1.2   | Excel generation      |
| Werkzeug   | 2.3.6   | WSGI utilities        |

### JavaScript Libraries

- Built-in: No external dependencies
- Uses Fetch API for AJAX
- Vanilla CSS for styling

---

## 🎓 Learning Resources

### For Developers

1. **Flask Documentation:** flask.palletsprojects.com
2. **Pandas Guide:** pandas.pydata.org
3. **ReportLab Manual:** reportlab.com/docs
4. **OpenPyXL Docs:** openpyxl.readthedocs.io

---

**End of Technical Documentation**

For updates and support, refer to README.md and SETUP.md
