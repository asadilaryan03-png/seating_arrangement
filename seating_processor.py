import pandas as pd
import re
from datetime import datetime

class SeatingProcessor:
    """Process CSV files and create seating arrangements"""
    
    def __init__(self, filepath, branch_codes):
        self.filepath = filepath
        self.branch_codes = branch_codes
        self.df = None
        self.blocks = []
    
    def extract_branch_code(self, prn):
        """Robustly extract a branch code (one of the keys in self.branch_codes) from PRN.

        Strategy:
        - Normalize to string and keep only digits
        - Search for any configured branch code substring inside the digits
        - If no exact match, use last 5 digits as fallback (don't filter out)
        - Always return something to keep the row
        """
        try:
            if prn is None:
                return None
            s = str(prn)
            digits = re.sub(r"\D", "", s)
            if not digits:
                return None

            # Search for any known branch code inside the digits string
            for code in self.branch_codes.keys():
                if code in digits:
                    return code

            # Fallback: if digits length >= 5, return last 5 digits as is
            # This keeps the row instead of filtering it out
            if len(digits) >= 5:
                return digits[-5:]

            # If very short, return as is (still keeps row)
            return digits if len(digits) > 0 else None
        except Exception:
            return None
    
    def process(self):
        """Main processing function"""
        # Read CSV
        self.df = pd.read_csv(self.filepath)

        # Normalize column names (strip whitespace)
        self.df.columns = [c.strip() for c in self.df.columns]

        # Find PRN column (case-insensitive)
        prn_col = None
        for c in self.df.columns:
            if c.strip().lower() == 'prn':
                prn_col = c
                break
        if prn_col is None:
            raise ValueError('Could not find a `PRN` column in the uploaded CSV.')

        # Clean PRN values
        self.df['PRN'] = self.df[prn_col].astype(str).str.strip()

        # Extract branch code and branch name
        self.df['BranchCode'] = self.df['PRN'].apply(self.extract_branch_code)
        self.df['Branch'] = self.df['BranchCode'].map(self.branch_codes)

        # Remove rows with completely empty branch codes (but keep fallback codes)
        before_count = len(self.df)
        self.df = self.df[self.df['BranchCode'].notna()].copy()
        after_count = len(self.df)
        
        # For rows without recognized branch codes, assign a generic "Other" label
        self.df['Branch'] = self.df.apply(
            lambda row: self.branch_codes.get(row['BranchCode'], 'Other'),
            axis=1
        )
        
        # Sort by branch name, branch code and then by PRN so output groups by branch (alphabetical)
        # Ensure Branch column has no NA for sorting
        self.df['Branch'] = self.df['Branch'].fillna('')
        self.df = self.df.sort_values(['Branch', 'BranchCode', 'PRN']).reset_index(drop=True)
        
        # Create blocks of 30 students (if any remain after filtering)
        self.create_blocks()
        
        # Prepare output data
        output_data = {
            'totalStudents': len(self.df),
            'blocks': self.blocks,
            'timestamp': datetime.now().isoformat(),
            'debug': {
                'rows_before_filter': before_count,
                'rows_after_filter': after_count,
                'recognized_branch_codes': list(self.branch_codes.keys())
            }
        }
        
        return output_data
    
    def create_blocks(self):
        """Create blocks of 30 students each"""
        students_per_block = 30
        total_students = len(self.df)
        num_blocks = (total_students + students_per_block - 1) // students_per_block
        
        def _num_to_letters(n):
            """Convert 1-based integer n to letters: 1->A, 26->Z, 27->AA"""
            letters = ''
            while n > 0:
                n, rem = divmod(n - 1, 26)
                letters = chr(65 + rem) + letters
            return letters
        
        for block_num in range(num_blocks):
            start_idx = block_num * students_per_block
            end_idx = min(start_idx + students_per_block, total_students)
            
            block_students = self.df.iloc[start_idx:end_idx].copy()
            
            # Assign desk numbers
            block_students['DeskNo'] = range(1, len(block_students) + 1)
            
            # Determine year and name columns (handle different CSV column names)
            year_col = next((c for c in block_students.columns if 'year' in c.lower()), None)
            name_col = next((c for c in block_students.columns if c.strip().lower() in ('name', 'student name')), 'Name')

            # Get block details
            try:
                block_year = int(block_students.iloc[0][year_col]) if year_col and not pd.isna(block_students.iloc[0][year_col]) else 2
            except Exception:
                block_year = 2

            # Compute branches present in this block (sorted, unique)
            unique_branches = [b for b in sorted(block_students['Branch'].dropna().unique())]
            branch_label = unique_branches[0] if len(unique_branches) == 1 else ', '.join(unique_branches)
            branch_code_label = block_students.iloc[0]['BranchCode'] if 'BranchCode' in block_students.columns else ''

            block_letter = _num_to_letters(block_num + 1)
            block_data = {
                'blockNumber': block_num + 1,
                'blockName': f'Block-{block_letter}',
                'totalStudents': len(block_students),
                'prnFrom': block_students.iloc[0]['PRN'],
                'prnTo': block_students.iloc[-1]['PRN'],
                'year': block_year,
                'branch': branch_label,
                'branches': unique_branches,
                'branchCode': branch_code_label,
                'centerCode': '6321',
                'examType': self.get_exam_type(),
                'date': '',
                'students': []
            }
            
            # Add student details
            for idx, row in block_students.iterrows():
                try:
                    student_year = int(row[year_col]) if year_col and not pd.isna(row[year_col]) else block_year
                except Exception:
                    student_year = block_year

                block_data['students'].append({
                    'deskNo': int(row['DeskNo']),
                    'prn': str(row['PRN']),
                    'name': row.get(name_col, '') if name_col in row.index else row.get('Name', ''),
                    'branch': row.get('Branch', ''),
                    'year': student_year
                })
            
            self.blocks.append(block_data)
    
    def get_exam_type(self):
        """Determine if it's Winter or Summer based on current date"""
        month = datetime.now().month
        year = datetime.now().year
        # Use institution's season mapping:
        # - Winter: November, December, January (11,12,1)
        # - Summer: April, May, June, July (4,5,6,7)
        if month in [11, 12, 1]:
            return f"Winter Examination {year}"
        if month in [4, 5, 6, 7]:
            return f"Summer Examination {year}"
        # For other months, return a generic label with year
        return f"Examination {year}"
