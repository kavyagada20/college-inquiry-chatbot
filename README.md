College Enquiry Chatbot
=======================

A lightweight Flask-based chatbot for answering common college enquiries. The app serves a minimal web UI and a `/get_response` API endpoint that delegates to `chatbot_core.py` for generating replies. This repository contains training utilities, example data, and the trained model files (in `models/`).

Contents
- `app.py` — Flask application and web UI (single-file template)
- `chatbot_core.py` — chatbot response logic
- `train_intent_model.py` — training script for intents (if applicable)
- `data/` — example data (e.g., `faq_data.csv`)
- `models/` — stored model artifacts (excluded from Git by default)
- `HOW_TO_RUN.md` — detailed run instructions and sample questions

Quick Start
1. Change into the project directory:

```bash
cd /path/to/nlp_mini
```

2. Create and activate the virtual environment (Linux/macOS zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app locally:

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser and try the chat UI.

See `HOW_TO_RUN.md` for more details, API test commands, and sample prompts to try.

Deployment Notes

Netlify (frontend-only)
- Netlify is optimized for static sites and serverless functions. A plain Flask app isn't directly deployable to Netlify as a persistent server.
- Recommended pattern: deploy the frontend (static site) to Netlify and host the Flask backend elsewhere (Render, Railway, Heroku, or a small VPS). The frontend can call the backend API URL.
- To host just the UI on Netlify:
  1. Extract the HTML from `app.py` (`HTML_TEMPLATE`) into a static `index.html` and host it in a separate repo or `dist/` folder.
  2. Configure Netlify to build/deploy the static site (or drag-and-drop `index.html`).
  3. Point the frontend's fetch calls to the deployed backend endpoint.

Deploying the Flask backend (recommended alternatives)
- Render (recommended for Flask):
  1. Create a Render Web Service, connect your GitHub repo.
  2. Set the start command to `gunicorn app:app` and the environment to `Python 3.x`.
  3. Add environment variables (if any) and deploy.

- Railway / Fly / Heroku: these platforms also support quick Flask deploys; set the Procfile or start command accordingly.

Example `Procfile` for production (gunicorn):

```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

Security & repo tips
- Keep `models/` or large binary artifacts out of Git; use releases or Git LFS if you must version them.
- Do not commit secrets; use environment variables for API keys and credentials.
- Add a `.gitignore` (present in this repo) that excludes `.venv`, model files, and `.env`.

Sample questions
- See `HOW_TO_RUN.md` for 5 core prompts and 10 additional suggestions useful for testing.

Pushing to GitHub
If you want me to commit and push these new files for you, provide the remote repo URL (SSH or HTTPS) or tell me to make a local commit only.

Commands I'll run (you can run them yourself):

```bash
# create repo and initial commit (if not already a git repo)
git init
git add .
git commit -m "Add run instructions, README, LICENSE and gitignore"
# set main and add remote
git branch -M main
git remote add origin <REPO_URL>
git push -u origin main
```

License
- This repository includes an MIT `LICENSE` file. Replace `YOUR_NAME` in `LICENSE` with your name.

Need help?
- I can:
  - Create a separate static `index.html` for Netlify and wire it to a hosted backend.
  - Commit and push these files to your GitHub repo (please provide the repo URL).
  - Deploy the backend to Render/Railway and show the live endpoint.

