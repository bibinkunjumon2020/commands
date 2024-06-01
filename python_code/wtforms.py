from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, DateField,FileField,BooleanField,IntegerField,EmailField
from wtforms.validators import InputRequired,NumberRange,DataRequired,Optional
from flask_wtf.file import FileAllowed

class ApplicationForm(FlaskForm):
    fullname = StringField('Full Name', validators=[InputRequired()])
    dob = DateField('Date of Birth', validators=[InputRequired()], format='%Y-%m-%d')
    age_years = StringField('Years', validators=[InputRequired(),DataRequired()],render_kw={'readonly': 'readonly'})
    age_months = StringField('Months', validators=[InputRequired()],render_kw={'readonly': 'readonly'})
    age_days = StringField('Days', validators=[InputRequired()],render_kw={'readonly': 'readonly'})
    nationality = SelectField('Nationality', choices=[('India', 'India'), ('Other', 'Other')], validators=[InputRequired()])
    state = StringField('State', validators=[InputRequired()])
    religion = StringField('Religion', validators=[InputRequired()])
    community = StringField('Community', validators=[InputRequired()])
    caste = SelectField('Caste', choices=[('SC', 'SC'), ('ST', 'ST'), ('GEN', 'GEN'), ('OBC', 'OBC'),('EWS','EWS'), ('SEBC', 'SEBC'), ('Others', 'Others')], validators=[InputRequired()])
    gender = RadioField('Gender', choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], validators=[InputRequired()])
    #additional
    await_degree = RadioField('Await Degree', choices=[('YES', 'YES'), ('NO', 'NO')], validators=[InputRequired()])
    outside_degree = RadioField('Outside Degree', choices=[('YES', 'YES'), ('NO', 'NO')], validators=[InputRequired()])
    written_mat = RadioField('CMAT/KMAT/CAT', choices=[('YES', 'YES'), ('NO', 'NO')], validators=[InputRequired()])
    # MAT DEtails
    exam_name1 = SelectField('Exam Name', choices=[('CMAT', 'CMAT'),("KMAT","KMAT") ,("CAT","CAT"),('Other', 'Other')], validators=[])
    reg_num1 = StringField('Register Number', validators=[])
    composite_score1 = StringField('Composite Score', validators=[])
    date_of_test1 = DateField('Date of Test', validators=[Optional()], format='%Y-%m-%d')
    # MAT DEtails
    exam_name2 = SelectField('Exam Name', choices=[("KMAT","KMAT") ,("CAT","CAT"),('Other', 'Other'),('CMAT', 'CMAT')], validators=[])
    reg_num2 = StringField('Register Number', validators=[])
    composite_score2 = StringField('Composite Score', validators=[])
    date_of_test2 = DateField('Date of Test', validators=[Optional()], format='%Y-%m-%d')
    # MAT DEtails
    exam_name3 = SelectField('Exam Name', choices=[("CAT","CAT"),('CMAT', 'CMAT'),("KMAT","KMAT") ,('Other', 'Other')], validators=[])
    reg_num3 = StringField('Register Number', validators=[])
    composite_score3 = StringField('Composite Score', validators=[])
    date_of_test3 = DateField('Date of Test', validators=[Optional()], format='%Y-%m-%d')
    # MAT DEtails
    exam_name4 = SelectField('Exam Name', choices=[('Other', 'Other'),('CMAT', 'CMAT'),("KMAT","KMAT") ,("CAT","CAT"),], validators=[])
    reg_num4 = StringField('Register Number', validators=[])
    composite_score4 = StringField('Composite Score', validators=[])
    date_of_test4 = DateField('Date of Test', validators=[Optional()], format='%Y-%m-%d')

    #Qualification Degree
    qualification = RadioField('Qualification', choices=[('BSC', 'BSC'), ('BCOM', 'BCOM'),('BA', 'BA'),('BBA', 'BBA'),('B.Tech', 'B.Tech'),('Other', 'Other')], validators=[InputRequired()])
    branch = StringField('Branch', validators=[InputRequired()])
    university = StringField('University', validators=[InputRequired()])
    passdate = StringField('Passyear', validators=[InputRequired()])
    #
    sem_mark_total = StringField('Total Secured Mark', validators=[])
    sem_mark_max = StringField('Total Max Mark', validators=[])
    sem_mark_percentage = StringField('Percentage of Marks', validators=[])
    
    #address-permanent
    permanent_address_housename = TextAreaField('House Name', validators=[InputRequired()])
    permanent_address_street = TextAreaField('Street', validators=[InputRequired()])
    permanent_address_postoffice = TextAreaField('Post Office', validators=[InputRequired()])
    permanent_address_district = TextAreaField('District', validators=[InputRequired()])
    permanent_address_pincode = IntegerField('Pincode', validators=[InputRequired()])

    communication_address_same_as_above = BooleanField('same as above', validators=[])

    communication_address_housename = TextAreaField('House Name', validators=[InputRequired()])
    communication_address_street = TextAreaField('Street', validators=[InputRequired()])
    communication_address_postoffice = TextAreaField('Post Office', validators=[InputRequired()])
    communication_address_district = TextAreaField('District', validators=[InputRequired()])
    communication_address_pincode = IntegerField('Pincode', validators=[InputRequired()])
    #contacts
    std_code = StringField('STD Code', validators=[])
    telephone = StringField('Telephone', validators=[])
    mobile = IntegerField('Mobile Phone', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    #Parent
    parent_guardian_name = StringField('Parent/Guardian Name', validators=[InputRequired()])
    parent_guardian_occupation = StringField('Occupation', validators=[InputRequired()])
    parent_guardian_official_address = StringField('Official Address', validators=[InputRequired()])
    parent_guardian_pincode = IntegerField('Pincode', validators=[InputRequired()])
    parent_guardian_std_code = StringField('STD Code', validators=[])
    parent_guardian_telephone = StringField('Telephone', validators=[])
    parent_guardian_mobile_phone = IntegerField('Mobile Phone', validators=[InputRequired()])
    parent_guardian_email = EmailField('Email', validators=[InputRequired()])
    annual_income = IntegerField('Annual Income (Rs)', validators=[InputRequired(),NumberRange(min=0)])

    # user_signature = StringField('User Signature', validators=[InputRequired()])
    utr_upi_transaction_details = TextAreaField('UTR/UPI Transaction Details', validators=[InputRequired()])
    accept_declaration = BooleanField('I hereby declare that information furnished above is true and correct', validators=[InputRequired()])
        # For image upload
    
    applicant_photo = FileField('Upload Image', validators=[
        # InputRequired(),  # Image upload is required
        FileAllowed(['png', 'jpeg','jpg'], 'Images only!'),  # Only allow specific file extensions
          # Custom validator to check file extension
    ])
    applicant_sign = FileField('Upload Sign', validators=[
        # InputRequired(),  # Image upload is required
        FileAllowed(['png', 'jpeg','jpg'], 'Images only!'),  # Only allow specific file extensions
          # Custom validator to check file extension
    ])
        # For file upload
    upi_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])
        # SSLC
    sslc_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])
        # Plus Two
    plus_two_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])
        # Degree
    degree_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])
        # KMAT SCORE CARD
    cmat_score_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])
        # MIGRATION CARD
    migration_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])
        # INCOME CERTIFICATE
    income_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])
        # COMMUNITY CERTIFICATE
    community_file = FileField('Upload File', validators=[
        # InputRequired(),  # File upload is required
        FileAllowed(['pdf'], 'PDF documents only!')  # Only allow specific file extensions
    ])



