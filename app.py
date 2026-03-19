
import os
from dotenv import load_dotenv #  Import the loader
from flask import Flask, render_template, request, Response
from pypdf import PdfReader
from google import genai
from google.genai import types
from fpdf import FPDF
load_dotenv() # Loading the .env file
app = Flask(__name__)
MY_API_KEY = os.getenv("GEMINI_API_KEY") #Pullingkey from the environment 


client = genai.Client( #Client with the secret key
    api_key=MY_API_KEY,
    http_options=types.HttpOptions(api_version='v1alpha')
)

def get_resume_text(file):
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content: text += content
        return text
    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/", methods=["GET", "POST"])# Web routes
def index():
    result = None
    user_name = None 
    if request.method == "POST":
        user_name = request.form.get("user_name") 
        resume_file = request.files.get("resume")
        job_description = request.form.get("job_desc")
        
        if resume_file and job_description:
            resume_text = get_resume_text(resume_file)
            prompt = f"""
            You are an expert Technical Recruiter. 
            Analyze this RESUME against this JOB DESCRIPTION.
            
            RESUME: {resume_text}
            JOB: {job_description}
            

            [INSTRUCTIONS]
            Provide the following analysis exactly in this format:
            1. ⭐ OVERALL RATING: [Score out of 10, e.g., 8.5/10]
            2. 🔍 KEYWORD ALIGNMENT: [List 5-7 core technical keywords found in both the resume and the job description]
            3. ✅ TOP 3 STRENGTHS: [Provide 3 specific bullet points on why this candidate is a good fit]
            4. 🚩 CRITICAL GAPS: [List the top 3 missing requirements or certifications]
            5. 🗣️ ELEVATOR PITCH: [A compelling 3-sentence pitch for this candidate]
            """
            
            
            try:
                response = client.models.generate_content(
                    model='gemini-3.1-flash-lite-preview', 
                    contents=prompt
                )
                result = response.text
            except Exception as e:
                result = f"AI Error: {str(e)}"
    return render_template("index.html", result=result, user_name=user_name)

@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    content = request.form.get("content")
    user_name = request.form.get("user_name")
    
    
    content = content.replace('—', '-').replace('–', '-').replace('“', '"').replace('”', '"') # cleaning text
    clean_text = content.encode('latin-1', 'ignore').decode('latin-1')

    #Creating PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 20)
    pdf.cell(0, 10, f"Analysis for: {user_name}", new_x="LMARGIN", new_y="NEXT", align='L')
    pdf.set_font("Helvetica", 'I', 10)
    pdf.cell(0, 10, "AI Talent Scout - Professional Alignment Report", new_x="LMARGIN", new_y="NEXT", align='L')
    pdf.ln(10)
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 8, clean_text)
    
    #Fix for the assertion error
    pdf_output = pdf.output()
    if not isinstance(pdf_output, bytes):
        pdf_output = bytes(pdf_output)

    return Response(
        pdf_output,
        mimetype="application/pdf",
        headers={"Content-disposition": "attachment; filename=AI_Analysis.pdf"}
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)