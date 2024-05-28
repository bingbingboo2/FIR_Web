from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError
from flask import send_file
from io import BytesIO
import google.generativeai as palm
import os

app = Flask(__name__)

# Set your PaLM API key and model ID
palm.configure(api_key="AIzaSyC5iqIChPW9mKJmexmtDbrmjj7_AjBbAYw")
model_id = "models/chat-bison-001"

# Define IPC examples
examples = [
    ('I stole a car', 'IPC 379: Theft'),
    ('I killed someone', 'IPC 302: Murder'),
    ('I assaulted someone', 'IPC 323: Punishment for voluntarily causing hurt'),
]

# Define IPC section and question index
ipc_section = None
question_index = 0

# Define IPC questions
crime_description_questions = [
    "When did the crime occur?",
    "Where did the crime occur?",
    "Who was the victim?",
    "Who was the perpetrator?",
    "What was the motive for the crime?"
]

# Initialize answers and ai_crime_description
answers = []
ai_crime_description = None

# AWS S3 credentials


AWS_ACCESS_KEY_ID = 'AKIAVRUVSLJM53JK2IPG'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'edibuck'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Function to upload file to S3

def upload_to_s3(file_data, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    try:
        response = s3.put_object(Body=file_data, Bucket=bucket, Key=s3_file)
        print("Upload Successful")
        print("S3 response:", response)
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except Exception as e:
        print(f"Error uploading to S3: {e}")
        return False


@app.route('/', methods=['GET', 'POST'])
def index():
    global question_index, ipc_section, ai_crime_description

    if request.method == 'POST':
        user_answer = request.form['user_answer']
        answers.append(user_answer)

        # Ask the next question or predict IPC if all questions are answered
        question_index += 1
        if question_index < len(crime_description_questions):
            return render_template('index.html', questions=crime_description_questions[:question_index + 1], answers=answers, final=False)
        else:
            # Generate crime description
            crime_description = ", ".join(answers)

            # Predict IPC section
            response = palm.chat(messages=f"The crime description is: {crime_description}", temperature=0.2, context="give indian penal codes with punishments on basis of question answered by user.", examples=examples)
            ipc_section = response.last

            # Generate AI-generated crime description
            ai_crime_description_response = palm.chat(messages=f"The IPC section is: {ipc_section}", temperature=0.2, context="Generate a crime description based on the answers given by the user")
            ai_crime_description = ai_crime_description_response.last

            return redirect(url_for('generate_pdf'))

    return render_template('index.html', questions=crime_description_questions[:question_index + 1], answers=answers, final=False)

@app.route('/generate_pdf', methods=['GET', 'POST'])
def generate_pdf():
    global ipc_section, ai_crime_description

    # Construct HTML content for the PDF
    html_content = "<h1>FIRST INFORMATION REPORT</h1>"
    
    # Check if ipc_section is not None before concatenating
    if ipc_section:
        html_content += "<p><strong>IPC Section:</strong> " + ipc_section + "</p>"
    else:
        html_content += "<p><strong>IPC Section:</strong> Not specified</p>"

    # Add crime description
    if ai_crime_description:
        html_content += "<p><strong>Crime Description:</strong> " + ai_crime_description + "</p>"
    else:
        html_content += "<p><strong>Crime Description:</strong> Not specified</p>"

    # Generate PDF using xhtml2pdf
    pdf = create_pdf(html_content)

    # Upload PDF to S3
    if pdf:
        upload_to_s3(pdf, AWS_STORAGE_BUCKET_NAME, 'fir_report.pdf')

    return redirect(url_for('fir_page'))

@app.route('/fir_page')
def fir_page():
    global ipc_section, ai_crime_description
    return render_template('fir.html', ipc_section=ipc_section, ai_crime_description=ai_crime_description)


def create_pdf(html_content):
    from xhtml2pdf import pisa

    pdf_data = BytesIO()
    pisa.CreatePDF(BytesIO(html_content.encode('utf-8')), pdf_data)

    return pdf_data.getvalue()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
