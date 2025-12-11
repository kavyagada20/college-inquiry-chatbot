HOW TO RUN: College Enquiry Chatbot

Overview
- This document describes how to create/activate the project's virtual environment, install dependencies, run the Flask chatbot app, test the API, and push the code to GitHub.

Prerequisites
- Python 3.8+ installed
- Git installed
- (Optional) SSH keys set up for GitHub if you plan to push over SSH

1) Create or activate the virtual environment
- If a virtual environment already exists at `.venv`, activate it:

```bash
# macOS / Linux (zsh)
source .venv/bin/activate

# or equivalently
. .venv/bin/activate
```

- If `.venv` does not exist, create and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Run the Flask app

```bash
python app.py
```

- By default the app listens on `http://127.0.0.1:5000/` when run locally.
- Open the URL in your browser and use the UI to chat.

4) Quick API test (optional)
- You can POST directly to the `/get_response` endpoint to test the chatbot from the command line:

```bash
curl -s -X POST http://127.0.0.1:5000/get_response \
  -H "Content-Type: application/json" \
  -d '{"message":"What are the admission requirements for undergraduate programs?"}' | jq
```

5) Sample questions to ask the chatbot
- These are ready-to-use prompts for users evaluating the system.

Core/High-priority (5 provided):
1. What are the admission requirements for undergraduate programs?
2. How do I apply for scholarships or financial aid?
3. What is the course structure and duration for the Computer Science degree?
4. Are there on-campus housing options available for new students?
5. How can I contact academic advisors or schedule a campus tour?

Additional useful questions (extra suggestions):
6. What documents do I need to attach to my application?
7. When are the application deadlines for fall and spring intake?
8. Are there any entrance exams or minimum test scores required?
9. How much is the tuition fee for international students?
10. Do you offer online or part-time study options?
11. What career services are available for graduates?
12. Are internships or industry placements supported by the college?
13. What student clubs and extracurricular activities exist?
14. Is there support for students with disabilities?
15. How do I reset my student portal password?

6) Pushing this project to GitHub (basic)

- If this directory is not yet a git repo, run:

```bash
cd /path/to/nlp_mini
git init
```

- Add a sensible `.gitignore` before committing. Example entries:

```
.venv/
__pycache__/
*.pyc
models/
.env
```

- Commit and push:

```bash
git add .
git commit -m "Add college enquiry chatbot and run instructions"
# create a main branch and push to remote (replace with your repo URL)
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

- If using HTTPS instead of SSH, use the HTTPS remote URL and authenticate as required:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

7) Professional polish tips
- Add a concise `README.md` (project overview, quick run), and keep `HOW_TO_RUN.md` for operational steps.
- Include a `.gitignore` that excludes `.venv`, model binaries, and secrets.
- Add a `LICENSE` file (MIT or BSD are common for academic code).
- Keep `requirements.txt` up to date; pin versions where appropriate.
- Provide sample intents/data and a small script to re-train or validate the model.
- Use clear commit messages and a single commit per feature/change when possible.
- Optionally add a brief `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` for open-source friendliness.

8) Notes & troubleshooting
- If Flask reports "Address already in use", stop the other process or change the port: `app.run(debug=True, port=5001)` in `app.py`.
- If imports fail, ensure the virtualenv is activated and `pip install -r requirements.txt` completed successfully.
- Large model files in `models/` may be better stored in a release or LFS rather than directly in the repo.

---
If you'd like, I can:
- Add a `.gitignore` and `LICENSE` file for you.
- Commit and push these instructions to GitHub (you'll need to provide the remote URL or set up credentials).
- Run the app locally in the workspace and verify the endpoints.

