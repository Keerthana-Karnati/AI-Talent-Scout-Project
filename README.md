🚀 AI Talent Scout: Resume-Job Matcher
An AI-powered recruitment tool that analyzes professional resumes against job descriptions using Google Gemini 3.1 Flash. This project demonstrates a full-stack integration of Generative AI with a focus on secure API handling and automated document reporting.

🌟 Key Features
Intelligent Analysis: Deep-dive scoring (out of 10), keyword alignment, and candidate strengths/gaps.
Secure Architecture: Zero-exposure API key management using .env and environment variables.
Professional PDF Export: Generates downloadable, sanitized reports using FPDF2.
Modern UI: Responsive "Glassmorphism" dashboard with real-time loading states and session resets.
🛠️ Technical Stack
Backend: Python (Flask)
AI Engine: Google Gemini 3.1
PDF Engine: FPDF2 & PyPDF
Frontend: HTML5, CSS3 (Glassmorphism UI), JavaScript
📂 Project Structure
├── app.py # Flask Backend & AI Logic
├── templates/
│ └── index.html # Frontend Dashboard
├── .env # Private API Keys (Ignored by Git)
├── .gitignore # Security rules for Git
└── requirements.txt # Project dependencies

## 🔧 Installation & Setup

1. **Clone the repository:**
   git clone [https://github.com/Keerthana-Karnati/AI-Talent-Scout-Project.git](https://github.com/Keerthana-Karnati/AI-Talent-Scout-Project.git)
   cd AI-Talent-Scout-Project

2. **Create a Virtual Environment:**
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Configure Environment Variables:**
   Create a .env file in the root directory and add your API key:
   GEMINI_API_KEY=your_actual_api_key_here (text)

5. **Run the Application:**
   python3 app.py
   Access the tool at http://127.0.0.1:5001.

## Security Best Practices

This project follows professional engineering standards by ensuring that the venv/ folder and sensitive .env files are excluded from version control via .gitignore,
preventing credential leaks and keeping the repository lightweight and professional.

🎓 **by Keerthana | MS in Computer Science | University of Central Missouri | GPA: 3.9**
