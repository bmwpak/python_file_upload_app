"""
Script to generate guide.pdf for the File Upload Application
Run: python create_guide.py
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def create_guide():
    # Create PDF document
    doc = SimpleDocTemplate("guide.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2d3748'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#4a5568'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=10,
        fontName='Courier',
        leftIndent=20,
        rightIndent=20,
        spaceAfter=10,
        spaceBefore=10,
        backColor=colors.HexColor('#f7fafc'),
        borderColor=colors.HexColor('#e2e8f0'),
        borderWidth=1,
        borderPadding=10
    )
    
    normal_style = ParagraphStyle(
        'NormalCustom',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )
    
    # Title
    elements.append(Paragraph("File Upload Application", title_style))
    elements.append(Paragraph("Installation & Setup Guide", ParagraphStyle('Subtitle', parent=styles['Heading2'], fontSize=18, alignment=TA_CENTER, textColor=colors.HexColor('#718096'))))
    elements.append(Spacer(1, 0.3*inch))
    
    # Table of Contents
    elements.append(Paragraph("Table of Contents", heading_style))
    toc_data = [
        ['1. Introduction', '3'],
        ['2. Prerequisites', '3'],
        ['3. Project Structure', '4'],
        ['4. Installation Steps', '4'],
        ['5. Running the Server', '5'],
        ['6. Using the Application', '6'],
        ['7. Troubleshooting', '7'],
        ['8. Project Features', '8']
    ]
    toc_table = Table(toc_data, colWidths=[4.5*inch, 1*inch])
    toc_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#4a5568')),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('LINEABOVE', (0, 0), (-1, 0), 0.5, colors.HexColor('#e2e8f0')),
    ]))
    elements.append(toc_table)
    elements.append(PageBreak())
    
    # Section 1: Introduction
    elements.append(Paragraph("1. Introduction", heading_style))
    elements.append(Paragraph(
        "This is a Flask-based web application for uploading and managing documents. "
        "The application allows users to upload 5-10 files simultaneously, with each file "
        "not exceeding 500KB. Files are stored on the server and managed through a modern, "
        "user-friendly web interface.",
        normal_style
    ))
    elements.append(Spacer(1, 0.2*inch))
    
    # Section 2: Prerequisites
    elements.append(Paragraph("2. Prerequisites", heading_style))
    elements.append(Paragraph(
        "Before installing and running this application, ensure you have the following "
        "installed on your system:",
        normal_style
    ))
    
    prereq_data = [
        ['Python', '3.7 or higher'],
        ['pip', 'Python package manager'],
        ['Virtual Environment', 'Recommended (venv)'],
    ]
    prereq_table = Table(prereq_data, colWidths=[2*inch, 3.5*inch])
    prereq_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f7fafc')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2d3748')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(prereq_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Section 3: Project Structure
    elements.append(Paragraph("3. Project Structure", heading_style))
    elements.append(Paragraph(
        "The project has the following directory structure:",
        normal_style
    ))
    
    structure_text = """
    python_file_upload_app/
    ├── file_upload_app/
    │   ├── app.py                 # Main Flask application
    │   └── templates/
    │       └── index.html         # Web interface template
    ├── instance/
    │   └── database.db           # SQLite database (auto-created)
    ├── static/
    │   └── uploads/              # Uploaded files storage
    ├── venv/                     # Virtual environment (optional)
    └── guide.pdf                 # This guide
    """
    elements.append(Paragraph(structure_text.replace('\n', '<br/>'), code_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Section 4: Installation Steps
    elements.append(Paragraph("4. Installation Steps", heading_style))
    elements.append(Paragraph(
        "Follow these steps to set up the application on your system:",
        normal_style
    ))
    
    elements.append(Paragraph("Step 1: Navigate to Project Directory", subheading_style))
    elements.append(Paragraph(
        "Open your terminal or command prompt and navigate to the project directory.",
        normal_style
    ))
    elements.append(Paragraph(
        "<b>Windows:</b>",
        ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')
    ))
    elements.append(Paragraph("cd C:\\path\\to\\python_file_upload_app", code_style))
    elements.append(Paragraph(
        "<b>Linux/Mac:</b>",
        ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')
    ))
    elements.append(Paragraph("cd /path/to/python_file_upload_app", code_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("Step 2: Create Virtual Environment (Recommended)", subheading_style))
    elements.append(Paragraph(
        "It's recommended to use a virtual environment to isolate project dependencies:",
        normal_style
    ))
    elements.append(Paragraph("<b>Windows:</b>", ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')))
    elements.append(Paragraph("python -m venv venv", code_style))
    elements.append(Paragraph("venv\\Scripts\\activate", code_style))
    elements.append(Paragraph("<b>Linux/Mac:</b>", ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')))
    elements.append(Paragraph("python3 -m venv venv", code_style))
    elements.append(Paragraph("source venv/bin/activate", code_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("Step 3: Install Dependencies", subheading_style))
    elements.append(Paragraph(
        "Install the required Python packages using pip:",
        normal_style
    ))
    elements.append(Paragraph("pip install flask flask-sqlalchemy", code_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("Step 4: Verify Installation", subheading_style))
    elements.append(Paragraph(
        "Verify that Flask is installed correctly:",
        normal_style
    ))
    elements.append(Paragraph("python -c \"import flask; print(flask.__version__)\"", code_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Section 5: Running the Server
    elements.append(Paragraph("5. Running the Server", heading_style))
    elements.append(Paragraph(
        "To start the Flask development server, follow these steps:",
        normal_style
    ))
    
    elements.append(Paragraph("Method 1: Direct Python Execution", subheading_style))
    elements.append(Paragraph(
        "Navigate to the file_upload_app directory and run:",
        normal_style
    ))
    elements.append(Paragraph("cd file_upload_app", code_style))
    elements.append(Paragraph("python app.py", code_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("Method 2: Using Flask CLI", subheading_style))
    elements.append(Paragraph(
        "Alternatively, you can use Flask's built-in CLI:",
        normal_style
    ))
    elements.append(Paragraph("cd file_upload_app", code_style))
    elements.append(Paragraph("flask run", code_style))
    elements.append(Paragraph(
        "<i>Note: If using Flask CLI, you may need to set FLASK_APP=app.py</i>",
        ParagraphStyle('Italic', parent=normal_style, fontSize=10, textColor=colors.HexColor('#718096'))
    ))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("Server Information", subheading_style))
    elements.append(Paragraph(
        "Once the server starts, you should see output similar to:",
        normal_style
    ))
    server_output = """
    * Running on http://127.0.0.1:5000
    * Running on http://localhost:5000
    Press CTRL+C to quit
    """
    elements.append(Paragraph(server_output.replace('\n', '<br/>'), code_style))
    elements.append(Paragraph(
        "Open your web browser and navigate to: <b>http://localhost:5000</b> or "
        "<b>http://127.0.0.1:5000</b>",
        normal_style
    ))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("Stopping the Server", subheading_style))
    elements.append(Paragraph(
        "To stop the server, press <b>CTRL+C</b> in the terminal where the server is running.",
        normal_style
    ))
    elements.append(PageBreak())
    
    # Section 6: Using the Application
    elements.append(Paragraph("6. Using the Application", heading_style))
    elements.append(Paragraph(
        "Once the server is running and you've opened the application in your browser, "
        "you can use the following features:",
        normal_style
    ))
    
    elements.append(Paragraph("Uploading Files", subheading_style))
    upload_steps = [
        "1. Click the 'Choose Files (5-10 files)' button",
        "2. Select 5-10 files from your computer (each file must be ≤ 500KB)",
        "3. Review the selected files list showing file names and sizes",
        "4. Click 'Upload All Files' button",
        "5. Wait for the upload to complete (files upload sequentially)",
        "6. You'll see a success message when all files are uploaded"
    ]
    for step in upload_steps:
        elements.append(Paragraph(step, normal_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("Managing Files", subheading_style))
    elements.append(Paragraph(
        "Once files are uploaded, you can:",
        normal_style
    ))
    manage_data = [
        ['Edit', 'Select a new file and click Edit on an existing file to replace it'],
        ['Remove', 'Click Remove to delete a specific file from the server'],
        ['Final Submit', 'Mark all files as saved (requires 5-10 files)'],
        ['Cancel All', 'Delete all uploaded files and start over']
    ]
    manage_table = Table(manage_data, colWidths=[1.5*inch, 4*inch])
    manage_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#2d3748')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(manage_table)
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("File Requirements", subheading_style))
    requirements_data = [
        ['File Count', '5-10 files'],
        ['File Size', 'Maximum 500KB per file'],
        ['File Types', 'Any type (PDF, DOCX, images, etc.)']
    ]
    req_table = Table(requirements_data, colWidths=[2*inch, 3.5*inch])
    req_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f7fafc')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2d3748')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(req_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Section 7: Troubleshooting
    elements.append(Paragraph("7. Troubleshooting", heading_style))
    
    elements.append(Paragraph("Common Issues and Solutions", subheading_style))
    
    troubleshooting_data = [
        ['Issue', 'Solution'],
        ['Port 5000 already in use', 'Change port: app.run(debug=True, port=5001)'],
        ['ModuleNotFoundError: No module named flask', 'Install Flask: pip install flask flask-sqlalchemy'],
        ['Permission denied errors', 'Check file/folder permissions, especially for uploads directory'],
        ['Database errors', 'Delete instance/database.db and restart (database will be recreated)'],
        ['Files not uploading', 'Check file sizes (max 500KB) and ensure uploads folder exists'],
        ['Import errors', 'Ensure virtual environment is activated and dependencies installed']
    ]
    trouble_table = Table(troubleshooting_data, colWidths=[2.5*inch, 3*inch])
    trouble_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2d3748')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
    ]))
    elements.append(trouble_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Section 8: Project Features
    elements.append(Paragraph("8. Project Features", heading_style))
    elements.append(Paragraph(
        "This application includes the following features:",
        normal_style
    ))
    
    features_data = [
        ['✅', 'Modern, responsive web interface'],
        ['✅', 'Multiple file selection (5-10 files)'],
        ['✅', 'File size validation (max 500KB per file)'],
        ['✅', 'Sequential file upload with progress tracking'],
        ['✅', 'File management (edit, remove)'],
        ['✅', 'SQLite database for file metadata'],
        ['✅', 'RESTful API endpoints'],
        ['✅', 'Beautiful gradient UI design'],
    ]
    features_table = Table(features_data, colWidths=[0.5*inch, 4.5*inch])
    features_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2d3748')),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(features_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Footer
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph(
        "<i>For additional support or questions, refer to the project documentation or "
        "contact the development team.</i>",
        ParagraphStyle('Footer', parent=normal_style, fontSize=10, alignment=TA_CENTER, textColor=colors.HexColor('#718096'))
    ))
    
    # Build PDF
    doc.build(elements)
    print("Success! guide.pdf has been created successfully!")

if __name__ == "__main__":
    try:
        create_guide()
    except ImportError:
        print("Error: reportlab library is not installed.")
        print("Please install it using: pip install reportlab")
    except Exception as e:
        print(f"Error creating guide: {e}")

