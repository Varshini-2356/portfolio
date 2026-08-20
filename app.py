from flask import Flask, render_template

app = Flask(__name__)

# ------------------------------------------------------------------
# EDIT YOUR DATA HERE. Everything on the site is driven from this
# dictionary, so you never need to touch the HTML to update content.
# ------------------------------------------------------------------
PORTFOLIO = {
    "name": "Varshini J",
    "role": "Aspiring SOC Analyst",
    "role_sub": "Cybersecurity Engineering Student",
    "initials": "VJ",
    "tagline": "Securing systems by day",
    "summary": (
        "Cybersecurity Engineering student with hands-on experience in vulnerability "
        "assessment, basic penetration testing, and malware analysis. Comfortable across "
        "the stack too — I build the applications I learn to secure. Self-motivated team "
        "player, eager to contribute to real-world SOC operations."
    ),

    "email": "varshinijatheshwaran@gmail.com",
    "location": "Coimbatore, India",

    # ⚠️ Replace these with your real profile URLs
    "linkedin": "https://www.linkedin.com/in/varshini-jagatheshwaran-9893b0293/",
    "github": "https://github.com/Varshini-2356",
    "leetcode": "https://leetcode.com/u/Varshini56/",

    "education": {
        "school": "Sri Shakthi Institute of Engineering and Technology, Coimbatore",
        "degree": "B.E. Computer Science Engineering (Cyber Security)",
        "years": "2023 – 2027",
        "cgpa": "8.15",
    },

    # Each skill can optionally carry a "cert" — an emoji + link that
    # opens the certificate proving that skill.
    "skill_groups": [
        {
            "label": "Security Tools",
            "skills": [
                {"name": "Nmap"},
                {"name": "Burp Suite"},
                {"name": "Wireshark"},
                {"name": "Metasploit"},
            ],
        },
        {
            "label": "Programming",
            "skills": [
                {"name": "Python"},
                {"name": "SQL"},
                {"name": "OOPs"},
                {"name": "JavaScript"},
            ],
        },
        {
            "label": "Security & Networking",
            "skills": [
                {"name": "Cybersecurity"},
                {"name": "Networking"},
                {"name": "Web App Security"},
                {"name": "Linux"},
            ],
        },
        {
            "label": "Web & Data",
            "skills": [
                {"name": "HTML"},
                {"name": "CSS"},
                {"name": "MySQL"},
                {"name": "MongoDB"},
            ],
        },
    ],

    "projects": [
        {
            "title": "File Integrity Monitoring with SMS ",
            "security_angle": "Real-time File Integrity Monitoring (FIM) system that flags unauthorized "
                               "access and suspicious file changes the moment they happen.",
            "dev_outcome": "Built in Python with automated backups, security logging, and live Twilio "
                            "SMS alerts — a working demo of monitoring + notification pipelines end to end.",
            "tech": ["Python", "Twilio API", "Logging", "File Systems"],
            "github": "https://github.com/Varshini-2356/DL_Prevention",
            "demo": "",
        },
        {
            "title": "Predictable Password Reset Token Vulnerability Lab",
            "security_angle": "A hands-on lab demonstrating how weak, guessable reset tokens let attackers "
                               "take over accounts — built to show the exploit, not just describe it.",
            "dev_outcome": "Implemented the full reset-token flow, then hardened it with cryptographically "
                            "secure random token generation — a before/after look at secure auth design.",
            "tech": ["Python", "Flask", "Cryptography", "Auth Flows"],
            "github": "https://github.com/Varshini-2356/Forgot_password_system",
            "demo": "",
        },
        {
            "title": "Evaluating the Unseen: A Risk-Calibrated Framework",
            "security_angle": "A dataset validation framework that screens ML training data for tampering "
                               "using SHA-256 hashing before it ever reaches a model.",
            "dev_outcome": "Detects duplicates, label errors, and unusual patterns in datasets — a Python "
                            "tool that bridges data engineering with data-integrity security.",
            "tech": ["Python", "SHA-256", "Data Validation", "ML Pipelines"],
            "github": "https://github.com/Varshini-2356/dataset_framework",
            "demo": "",
        },
    ],

    "certifications": [
        {"name": "Cisco – Introduction to Cybersecurity", "emoji": "🛡️", "link": "https://drive.google.com/file/d/1RXzcRG9BThX3_Nr_Bo_qEWhTBzC_VHiF/view?usp=sharing"},
        {"name": "Infosys – OWASP Top 10: Web Application Security", "emoji": "🕸️", "link": "https://drive.google.com/file/d/1zSeqZafqJdHHr-sbymUtQ0WGZSipoJQC/view?usp=sharing"},
        {"name": "LinkedIn Learning – Python OOP", "emoji": "🐍", "link": "https://drive.google.com/file/d/17LReOlfNyaHnh-0oJssei9LNQuH0lzwv/view?usp=sharing"},
        {"name": "Simplilearn – Introduction to SQL", "emoji": "🗄️", "link": "https://drive.google.com/file/d/1tSRTuaF1WQF-ca6O5lQF4YKQkFgRNP6J/view?usp=sharing"},
        {"name": "Infosis Springboard – Digital Forensics Using Kali Linux","emoji": "💀", "link": "https://drive.google.com/file/d/1zkWBrRi3FJv5-NZJ0Q74VcoIYXiKjNqN/view?usp=sharing"},
        {"name": "Cisco Networking Basics","emoji":"🌐","link":"https://drive.google.com/file/d/12teFm78wzUmEaJqVSjxQlKRVCp9hF6HG/view?usp=sharing"}
    ],

    "experience": [
        {
            "org": "CodeAlpha",
            "role": "Internship",
            "period": "",
            "desc": "Applied cybersecurity and programming fundamentals to real assigned tasks as part "
                    "of a remote internship program.",
        },
    ],

    "achievements": [
        {
            "title": "CTF Participant — Kanam Event, NGP College",
            "desc": "Placed 4th in a cybersecurity Capture The Flag competition, identifying and "
                    "exploiting practical security challenges under time pressure.",
        },
    ],

    "interests": ["Cybersecurity", "Networking", "Operating Systems", "Data Structures"],
}


@app.route("/")
def index():
    return render_template("index.html", data=PORTFOLIO)


if __name__ == "__main__":
    app.run(debug=True)
