# Varshini J — Portfolio

Flask + HTML/CSS portfolio site, light sky-blue & pink theme with a
radar/scan signature motif (fits the cybersecurity angle) and
emoji-linked certificate buttons.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000

## Edit your content

Everything — name, bio, links, skills, projects, certifications — lives
in one place: **`app.py`**, inside the `PORTFOLIO` dictionary. Change
text or links there; the HTML never needs to be touched.

Things to update first:
- `linkedin`, `github`, `leetcode` URLs (placeholders right now)
- `cert` links inside `skill_groups` and the `certifications` list —
  point these at your real certificate files/links
- Add a `demo` link to any project dict if it's deployed somewhere

## Deploy for free — Render.com

1. Push this folder to a GitHub repo.
2. Go to https://render.com → New → Web Service → connect the repo.
3. Settings:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
   - **Instance type:** Free
4. Deploy. Render gives you a free `.onrender.com` URL.

(Free tier sleeps after inactivity — first load after idle takes ~30s
to wake up, that's normal.)

## Alternative: PythonAnywhere (also free)

1. Upload the project files.
2. Create a new web app → Flask → point to `app.py`.
3. Reload the web app from the dashboard.

Both options need no credit card for the free tier.
