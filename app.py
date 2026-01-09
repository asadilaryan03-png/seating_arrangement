from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd
from datetime import datetime
from seating_processor import SeatingProcessor
from export_manager import ExportManager
import io

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

BRANCH_CODES = {
    '11995': 'AI & DS',
    '11191': 'Civil',
    '11242': 'CSE',
    '11293': 'Elect',
    '11372': 'ENTC',
    '11612': 'Mech'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Only CSV files are allowed'}), 400
    
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the CSV file
        processor = SeatingProcessor(filepath, BRANCH_CODES)
        seating_data = processor.process()
        
        return jsonify({
            'success': True,
            'data': seating_data,
            'filename': filename
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/export/<format_type>', methods=['POST'])
def export_seating(format_type):
    try:
        data = request.get_json()
        
        if format_type == 'pdf':
            pdf_buffer = ExportManager.generate_pdf(data)
            return send_file(
                pdf_buffer,
                mimetype='application/pdf',
                as_attachment=True,
                download_name=f'seating_arrangement_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
            )
        
        elif format_type == 'excel':
            excel_buffer = ExportManager.generate_excel(data)
            return send_file(
                excel_buffer,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                as_attachment=True,
                download_name=f'seating_arrangement_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
            )
        
        else:
            return jsonify({'error': 'Invalid format type'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
