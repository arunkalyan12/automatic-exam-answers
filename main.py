import os
import google.generativeai as genai

#Initialization of api
os.environ["GENERATIVE_AI_API_KEY"] = "Ente your pi key here"
genai.configure(api_key=os.getenv("GENERATIVE_AI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

#Geting file location and splitting the file into a list containing the different questions.
inFile = input("Enter file path of question file: ")

with open(inFile, "r") as questions:
    data = questions.read()
    questionList = data.splitlines()



#Making the final prompt used to enter into gemini
print("Enter the other instructions from the context in the brackets (question (already given) + other instructions)")
otherInst = input("Other Instructions: ")

outputFile = input("What is the file path of the output from the questions: ")

with open(outputFile, "w", encoding="utf-8") as answers:
    for i in range(len(questionList)):

        print("\n\n\n" + questionList[i])
        otherInst1 = input("Are there any other specific instructions for this question: ")

        prompt = questionList[i] + " " + otherInst + otherInst1
        print(prompt)
        answers.write(prompt + "\n\n\n")

        # Generating answers and remove the * from the response
        response = model.generate_content(prompt)
        cleaned_text = response.text.replace('**', '')

        answers.write(cleaned_text + "\n\n\n\n")
