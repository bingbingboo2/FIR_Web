from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as palm
#import pdfkit
#import os

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

            return redirect(url_for('fir_page'))

    return render_template('index.html', questions=crime_description_questions[:question_index + 1], answers=answers, final=False)

@app.route('/fir_page')
def fir_page():
    global ipc_section, ai_crime_description
    return render_template('fir.html', ipc_section=ipc_section, ai_crime_description=ai_crime_description)

if __name__ == '__main__':
    app.run(debug=True)
