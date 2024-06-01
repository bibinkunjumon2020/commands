#============= Merging Documents (application pdf generated)==========#
import io
from flask import send_file
import pdfkit
from PyPDF2 import PdfMerger
path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
@webapp.route('/download_zip/<applicationId>')
def download_zip(applicationId):
    student_application = models.view_application(applicationId)
    #
    applicant_photo_url = url_for('static', filename='images/applicant_photo/'+student_application["applicant_photo"],_external=True)
    applicant_sign_url = url_for('static', filename='images/applicant_sign/'+student_application["applicant_sign"],_external=True)
    rendered= render_template(
        "admin/download_application_template.html", student_application=student_application,applicant_photo_url=applicant_photo_url,applicant_sign_url=applicant_sign_url
    )
    pdf_path = os.path.join(os.environ['APPLICATION_PDF'], f'application_{applicationId}.pdf')
   # Generate PDF from the rendered HTML
    options = {
            'enable-local-file-access': "",
        }
    pdfkit.from_string(rendered, pdf_path, configuration=config, options=options)
    #
 # List of files to merge
    files_to_merge = [
        pdf_path,
        os.path.join(os.environ['SSLC_FILE'], student_application['sslc_file']) if student_application['sslc_file'] else None,
        os.path.join(os.environ['UPI_FILE'], student_application['upi_file']) if student_application['upi_file'] else None,
        os.path.join(os.environ['PLUS_TWO_FILE'], student_application['plus_two_file']) if student_application['plus_two_file'] else None,
        os.path.join(os.environ['DEGREE_FILE'], student_application['degree_file']) if student_application['degree_file'] else None,
        os.path.join(os.environ['CMAT_SCORE_FILE'], student_application['cmat_score_file']) if student_application['cmat_score_file'] else None,
        os.path.join(os.environ['MIGRATION_FILE'], student_application['migration_file']) if student_application['migration_file'] else None,
        os.path.join(os.environ['INCOME_FILE'], student_application['income_file']) if student_application['income_file'] else None,
        os.path.join(os.environ['COMMUNITY_FILE'], student_application['community_file']) if student_application['community_file'] else None,
    ]

    # Create a PDF merger object
    merger = PdfMerger()
    
    # Merge the PDFs
    for file_path in files_to_merge:
        if file_path:
            merger.append(file_path)
    
    # Create a BytesIO object to hold the merged PDF
    merged_pdf_buffer = io.BytesIO()
    
    # Write the merged PDF to the BytesIO object
    merger.write(merged_pdf_buffer)
    
    # Close the merger
    merger.close()
    
    # Rewind the buffer
    merged_pdf_buffer.seek(0)
    
    # Send the merged PDF as a download
    return send_file(merged_pdf_buffer, as_attachment=True, download_name=f'{applicationId}_application.pdf', mimetype='application/pdf')


#============= Merging Documents END ==========#
