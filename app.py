import os
import re
import sqlite3
import hmac
from contextlib import closing

from flask import (Flask, render_template, render_template_string, request,
                   redirect, url_for, flash, abort, Response)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-change-me")
DB = os.environ.get("DB_PATH", os.path.join(app.root_path, "messages.db"))

# ------------------------------------------------------------------
# EDIT YOUR DETAILS HERE (⚠️ = replace placeholder links)
# ------------------------------------------------------------------
COMMON = {
    "name": "Varshini J",
    "initials": "VJ",
    "profile_pic": "img/profile.png",
    "email": "varshinijatheshwaran@gmail.com",
    "location": "Coimbatore, India",
    "linkedin": "https://linkedin.com/in/varshini-j",          # ⚠️
    "github": "https://github.com/Varshini-2356",
    "leetcode": "https://leetcode.com/Varshini56",              # ⚠️
    "education": {
        "school": "Sri Shakthi Institute of Engineering and Technology, Coimbatore",
        "degree": "B.E. Computer Science Engineering (Cyber Security)",
        "years": "2023 – 2027",
        "cgpa": "8.15",
    },
    "experience": [
        {"org": "CodeAlpha", "role": "Internship",
         "desc": "Completed hands-on internship tasks applying programming and security fundamentals."},
    ],
    "achievements": [
        {"title": "CTF Participant — Kanam Event, NGP College",
         "desc": "Placed 4th in a cybersecurity Capture The Flag by finding and exploiting practical challenges."},
    ],
}

SDE = {
    "role": "Aspiring Software Developer",
    "role_sub": "Python · Flask · SQL · Web Development",
    "tagline": "I build clean, working web apps — and I think about security while I do.",
    "summary": ("Computer Science student who enjoys turning ideas into working software. "
                "I build backend logic in Python and Flask, design databases with SQL, and "
                "create responsive interfaces with HTML, CSS and JavaScript. Self-motivated "
                "team player who writes readable code and keeps learning by shipping projects."),
    "interests": ["Web Development", "Data Structures", "Problem Solving", "Databases"],
    "skill_groups": [
        {"label": "Languages", "skills": [
            {"name": "Python", "emoji": "🐍", "cert": "https://example.com/cert/python-oop"},
            {"name": "SQL", "emoji": "🗄️", "cert": "https://example.com/cert/sql"},
            {"name": "JavaScript"}]},
        {"label": "Web", "skills": [
            {"name": "HTML"}, {"name": "CSS"}, {"name": "Flask"}, {"name": "Jinja2"}]},
        {"label": "Databases", "skills": [
            {"name": "MySQL"}, {"name": "MongoDB"}, {"name": "SQLite"}]},
        {"label": "Fundamentals", "skills": [
            {"name": "OOP"}, {"name": "Data Structures"}, {"name": "Git & GitHub"}]},
    ],
    "projects": [
        {"title": "Portfolio Web App (this site)",
         "security_angle": "Full-stack Flask app with two role-based views served from one data source.",
         "dev_outcome": "Jinja2 templating, SQLite-backed contact form with validation, spam honeypot, "
                        "password-protected admin inbox, responsive UI, deployed live on Render.",
         "tech": ["Flask", "Jinja2", "SQLite", "HTML/CSS", "JavaScript"],
         "github": "https://github.com/Varshini-2356/portfolio", "demo": ""},     # ⚠️
        {"title": "Data Loss Prevention with File Integrity Monitoring",
         "security_angle": "Python tool that watches files in real time and detects changes.",
         "dev_outcome": "Built automated backups, structured logging and Twilio SMS alerts — "
                        "an event-driven pipeline from detection to notification.",
         "tech": ["Python", "Twilio API", "Logging"],
         "github": "https://github.com/Varshini-2356/DL_Prevention", "demo": ""},
        {"title": "Password Reset Token System",
         "security_angle": "Built a reset flow, then fixed it by replacing guessable tokens with secure ones.",
         "dev_outcome": "Implemented token generation and validation logic with cryptographically "
                        "secure randomness — a before/after of a real authentication feature.",
         "tech": ["Python", "Flask", "Auth Flow"],
         "github": "https://github.com/Varshini-2356/Forgot_password_system", "demo": ""},
        {"title": "Dataset Validation Framework",
         "security_angle": "Checks ML datasets before training for duplicates, label errors and tampering.",
         "dev_outcome": "Python data-processing tool using SHA-256 hashing and validation rules "
                        "to keep training data clean and reliable.",
         "tech": ["Python", "Data Validation", "SHA-256"],
         "github": "https://github.com/Varshini-2356/dataset_framework", "demo": ""},
    ],
    "certifications": [
        {"name": "LinkedIn Learning – Python OOP", "emoji": "🐍", "link": "https://example.com/cert/python-oop"},
        {"name": "Simplilearn – Introduction to SQL", "emoji": "🗄️", "link": "https://example.com/cert/sql"},
    ],
}

CYBER = {
    "role": "Aspiring SOC Analyst",
    "role_sub": "Cybersecurity Engineering Student",
    "tagline": "Finding weaknesses, understanding attacks, and watching alerts so systems stay safe.",
    "summary": ("Cybersecurity Engineering student with hands-on experience in vulnerability "
                "assessment, basic penetration testing and malware analysis. Familiar with "
                "monitoring security alerts and investigating incidents. Self-motivated team "
                "player eager to support real SOC operations."),
    "interests": ["Cybersecurity", "Networking", "Operating Systems", "Threat Detection"],
    "skill_groups": [
        {"label": "Security Tools", "skills": [
            {"name": "Nmap"}, {"name": "Burp Suite"}, {"name": "Wireshark"}, {"name": "Metasploit"}]},
        {"label": "Security Skills", "skills": [
            {"name": "Cybersecurity", "emoji": "🛡️", "cert": "https://example.com/cert/cisco-cybersecurity"},
            {"name": "Web App Security", "emoji": "🕸️", "cert": "https://example.com/cert/owasp-top-10"},
            {"name": "Vulnerability Assessment"}, {"name": "Malware Analysis"}]},
        {"label": "Networking & OS", "skills": [
            {"name": "Networking", "emoji": "🌐", "cert": "https://example.com/cert/networking-basics"},
            {"name": "Kali Linux", "emoji": "💀", "cert": "https://example.com/cert/kali-linux"},
            {"name": "Linux"}, {"name": "Windows"}]},
        {"label": "Scripting", "skills": [{"name": "Python"}, {"name": "SQL"}]},
    ],
    "projects": [
        {"title": "Data Loss Prevention with File Integrity Monitoring",
         "security_angle": "Real-time FIM system that detects unauthorized access and suspicious file changes.",
         "dev_outcome": "Sends Twilio SMS alerts, keeps automated backups and security logs to support data protection.",
         "tech": ["Python", "Twilio API", "Logging"],
         "github": "https://github.com/Varshini-2356/DL_Prevention", "demo": ""},
        {"title": "Predictable Password Reset Token Vulnerability Lab",
         "security_angle": "Lab showing how guessable reset tokens lead to account takeover.",
         "dev_outcome": "Then fixed it with secure random token generation — attack and defence side by side.",
         "tech": ["Python", "Flask", "Cryptography"],
         "github": "https://github.com/Varshini-2356/Forgot_password_system", "demo": ""},
        {"title": "Evaluating the Unseen: Risk-Calibrated Framework",
         "security_angle": "Detects unsafe or tampered ML data (duplicates, label errors, unusual patterns).",
         "dev_outcome": "Uses SHA-256 hashing to catch unauthorized changes before training.",
         "tech": ["Python", "SHA-256", "Data Validation"],
         "github": "https://github.com/Varshini-2356/dataset_framework", "demo": ""},
    ],
    "certifications": [
        {"name": "Cisco – Introduction to Cybersecurity", "emoji": "🛡️", "link": "https://example.com/cert/cisco-cybersecurity"},
        {"name": "Infosys – OWASP Top 10", "emoji": "🕸️", "link": "https://example.com/cert/owasp-top-10"},
        {"name": "Networking Basics", "emoji": "🌐", "link": "https://example.com/cert/networking-basics"},   # ⚠️ rename
        {"name": "Kali Linux", "emoji": "💀", "link": "https://example.com/cert/kali-linux"},                # ⚠️ rename
    ],
}

ROLES = {"sde": SDE, "cyber": CYBER}


# ------------------------------------------------------------------
# Database (SQLite) for the contact form
# ------------------------------------------------------------------
def init_db():
    with closing(sqlite3.connect(DB)) as con, con:
        con.execute("""CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, email TEXT, message TEXT,
            created TEXT DEFAULT CURRENT_TIMESTAMP)""")


init_db()


# ------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("landing.html", data=COMMON)


@app.route("/<role>")
def portfolio(role):
    if role not in ROLES:
        abort(404)
    return render_template("portfolio.html", role=role, data={**COMMON, **ROLES[role]})


@app.route("/contact", methods=["POST"])
def contact():
    role = request.form.get("role", "sde")
    role = role if role in ROLES else "sde"
    if request.form.get("website"):              # honeypot: bots fill this hidden field
        return redirect(url_for("portfolio", role=role))

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    msg = request.form.get("message", "").strip()
    valid = (1 <= len(name) <= 80 and 1 <= len(msg) <= 1000 and len(email) <= 120
             and re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))
    if not valid:
        flash("Please fill every field with a valid email.", "error")
    else:
        with closing(sqlite3.connect(DB)) as con, con:
            con.execute("INSERT INTO messages(name,email,message) VALUES (?,?,?)",
                        (name, email, msg))
        flash("Thanks! Your message was sent.", "ok")
    return redirect(url_for("portfolio", role=role) + "#contact")


ADMIN_HTML = """<!doctype html><title>Inbox</title>
<body style="font-family:sans-serif;max-width:720px;margin:30px auto;padding:0 16px">
<h2>Messages ({{ rows|length }})</h2>
{% for r in rows %}<div style="border:1px solid #cfeffb;border-radius:10px;padding:12px;margin:10px 0">
<b>{{ r[1] }}</b> &lt;{{ r[2] }}&gt; <small>{{ r[4] }}</small><p>{{ r[3] }}</p></div>
{% else %}<p>No messages yet.</p>{% endfor %}</body>"""


@app.route("/admin")
def admin():
    password = os.environ.get("ADMIN_PASSWORD")
    if not password:
        abort(404)                                # admin stays off until you set a password
    auth = request.authorization
    given = (auth.password or "") if auth else ""
    if not auth or not hmac.compare_digest(given.encode(), password.encode()):
        return Response("Login required", 401, {"WWW-Authenticate": 'Basic realm="admin"'})
    with closing(sqlite3.connect(DB)) as con:
        rows = con.execute("SELECT * FROM messages ORDER BY id DESC").fetchall()
    return render_template_string(ADMIN_HTML, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
