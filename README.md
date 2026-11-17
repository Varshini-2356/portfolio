# Varshini J — Two-Role Portfolio (Flask)

Routes: `/` (choose role) · `/sde` · `/cyber` · `/contact` (POST) · `/admin` (inbox)

Run: `pip install -r requirements.txt` then `python app.py` → http://127.0.0.1:5000

- Put your photo at `static/img/profile.png`
- Edit all content in `app.py` (look for ⚠️ placeholders and example.com links)
- Inbox: set env var `ADMIN_PASSWORD` (and `SECRET_KEY`), then open `/admin` (any username)
- Deploy on Render: Build `pip install -r requirements.txt`, Start `gunicorn app:app`
  (free tier disk resets on redeploy, so saved messages may be cleared)
