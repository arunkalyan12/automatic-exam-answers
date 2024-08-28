from flask import Flask, render_template, request, redirect, url_for
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key for Generative AI
os.environ["GENERATIVE_AI_API_KEY"] = "Enter your API key here"
genai.configure(api_key=os.getenv("GENERATIVE_AI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get file and additional instructions from the form
        question_file = request.files['question_file']
        other_instructions = request.form.get('other_instructions')
        output_file = request.form.get('output_file')

        # Read the questions from the uploaded file
        question_list = question_file.read().decode('utf-8').splitlines()

        # Process each question and generate the answers
        with open(output_file, "w", encoding="utf-8") as answers:
            for question in question_list:
                # Get specific instructions for each question
                specific_instructions = request.form.get(f'instructions_{question_list.index(question)}')

                prompt = question + " " + other_instructions + (specific_instructions or "")
                response = model.generate_content(prompt)
                cleaned_text = response.text.replace('**', '')

                answers.write(f"{prompt}\n\n{cleaned_text}\n\n\n")

        return redirect(url_for('index', success=True))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
