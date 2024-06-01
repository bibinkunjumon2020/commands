#============= Zipping Documents (application pdf generated)==========#
import io
import zipfile
from flask import send_file,url_for
import pdfkit
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
    files_to_zip = {
        'pdf_appln':pdf_path if pdf_path else None,
        'sslc_file': os.path.join(os.environ['SSLC_FILE'], student_application['sslc_file']) if student_application['sslc_file'] else None,
        'upi_file': os.path.join(os.environ['UPI_FILE'], student_application['upi_file']) if student_application['upi_file'] else None,
        'plus_two_file': os.path.join(os.environ['PLUS_TWO_FILE'], student_application['plus_two_file']) if student_application['plus_two_file'] else None,
        'degree_file': os.path.join(os.environ['DEGREE_FILE'], student_application['degree_file']) if student_application['degree_file'] else None,
        'cmat_score_file': os.path.join(os.environ['CMAT_SCORE_FILE'], student_application['cmat_score_file']) if student_application['cmat_score_file'] else None,
        'migration_file': os.path.join(os.environ['MIGRATION_FILE'], student_application['migration_file']) if student_application['migration_file'] else None,
        'income_file': os.path.join(os.environ['INCOME_FILE'], student_application['income_file']) if student_application['income_file'] else None,
        'community_file': os.path.join(os.environ['COMMUNITY_FILE'], student_application['community_file']) if student_application['community_file'] else None,
    }
    
    # Create a BytesIO object to hold the zip file in memory
    zip_buffer = io.BytesIO()
    
    # Create a ZipFile object
    with zipfile.ZipFile(zip_buffer, 'w') as zf:
        for file_key, file_path in files_to_zip.items():
            if file_path:
                file_name = os.path.basename(file_path)
                zf.write(file_path, arcname=file_name)
    
    # Rewind the buffer
    zip_buffer.seek(0)
    
    # Send the zip file as a download
    return send_file(path_or_file=zip_buffer, as_attachment=True, download_name=f'{applicationId}_certificates.zip', mimetype='application/zip')

#============= Zipping Documents END ==========#
