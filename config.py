"""
Configuration file for Seating Arrangement System
Modify these settings to customize the application
"""

# Institution Information
INSTITUTION_NAME = "V. V. P. Institute of Engineering & Technology, Solapur"
CENTER_CODE = "6321"

# Seating Configuration
STUDENTS_PER_BLOCK = 30  # Number of students in each examination block
DESK_START_NUMBER = 1    # Starting desk number (1-based)

# Flask Configuration
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
FLASK_DEBUG = True

# File Upload Settings
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"csv"}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Branch Code Mapping
# Format: 'branch_code': 'branch_name'
BRANCH_CODES = {
    '11995': 'AI & DS',
    '11191': 'Civil',
    '11242': 'CSE',
    '11293': 'Elect',
    '11372': 'ENTC',
    '11612': 'Mech'
}

# PRN Analysis Settings
PRN_BRANCH_CODE_START = 10  # Position where branch code starts in PRN
PRN_BRANCH_CODE_LENGTH = 5  # Length of branch code (5 digits)

# Export Settings
EXPORT_FORMATS = ['pdf', 'excel']
PDF_PAPER_SIZE = 'A4'
EXCEL_SHEET_NAME = 'Seating_Block'

# Exam Type Settings
WINTER_MONTHS = [12, 1, 2]  # December, January, February
SUMMER_MONTHS = [5, 6, 7, 8]  # May, June, July, August

# Column Names in CSV
CSV_COLUMNS = {
    'serial': 'Sr No.',
    'prn': 'PRN',
    'name': 'Name',
    'branch': 'Branch',
    'year': 'Year ',  # Note: There's a space in the sample CSV
    'college_code': 'College Code'
}

# Output Format Settings
BOLD_TITLES = True
TABLE_BORDER_WIDTH = 1
TABLE_HEADER_COLOR = (128, 128, 128)  # RGB for gray
TABLE_HEADER_TEXT_COLOR = (255, 255, 255)  # RGB for white

# Validation Settings
MIN_STUDENTS_REQUIRED = 1
MAX_STUDENTS_IN_BLOCK = 40
VALIDATE_PRN_FORMAT = True

# Display Settings
SHOW_BLOCK_DETAILS = True
SHOW_STUDENT_NAMES = True
SHOW_BRANCH_INFO = True
TRUNCATE_PRN_DISPLAY = 8  # Show last 8 digits of PRN in display
