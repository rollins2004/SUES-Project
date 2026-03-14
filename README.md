# 🗳️ VoteX — Student Union Election System

A futuristic, secure, and feature-rich online voting platform built with Django. Designed with a 2060 cyberpunk aesthetic.

---

## 🚀 Features

- **Cyberpunk 2060 UI** — Dark neon design with particle animations, holographic cards, and glowing elements
- **Secure Voting** — Registration-number-based authentication, one vote per position per student
- **Election Phase Management** — Admin controls: Nomination → Voting → Results
- **Live Results** — Animated charts, winner podium with confetti effect
- **Profile Management** — Photo upload, course/year editing
- **Production-Ready** — PostgreSQL, WhiteNoise static files, Gunicorn WSGI

---

## 🛠️ Local Development Setup

### Prerequisites
- Python 3.11+
- pip

### Steps

```bash
# 1. Clone or extract the project
cd Online_Voting_System

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r ../requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and set your SECRET_KEY

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (admin)
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

Visit `http://localhost:8000` to see the app!

---

## ☁️ Deploy to Render (Recommended — Free Tier)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "VoteX - Initial commit"
git remote add origin https://github.com/yourusername/votex.git
git push -u origin main
```

### Step 2: Create Render Account
1. Go to [render.com](https://render.com) and sign up (free)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository

### Step 3: Configure Render Settings
| Setting | Value |
|---------|-------|
| **Environment** | Python 3 |
| **Build Command** | `cd Online_Voting_System && pip install -r ../requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate` |
| **Start Command** | `cd Online_Voting_System && gunicorn onlineVotingSystem.wsgi` |
| **Root Directory** | *(leave empty)* |

### Step 4: Add Environment Variables on Render
In the Render dashboard → Environment tab, add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate with: `python -c "import secrets; print(secrets.token_urlsafe(50))"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
| `DATABASE_URL` | *(Auto-set if you create a Render PostgreSQL database)* |

### Step 5: Add PostgreSQL Database (Optional but Recommended)
1. Click **New +** → **PostgreSQL**
2. Create a free PostgreSQL instance
3. Copy the **Internal Database URL**
4. Add it as `DATABASE_URL` in your web service's environment variables

### Step 6: Deploy!
Click **Deploy** — Render will build and launch your app automatically. 🎉

---

## 👑 Admin Setup After Deployment

1. Visit `https://your-app.onrender.com/admin/`
2. Login with your superuser credentials
3. Add **Election Phases** (Nomination → Voting → Result)
4. Add **Candidates** with photos and manifestos
5. Students register and vote!

---

## 📁 Project Structure

```
Online_Voting_System/
├── onlineVotingSystem/      # Django project settings
│   ├── settings.py          # Production-ready settings
│   └── urls.py
├── poll/                    # Main voting app
│   ├── models.py            # StudentProfile, Candidate, Vote, ElectionPhase
│   ├── views.py             # All views (home, login, dashboard, vote, results)
│   ├── forms.py             # Registration, login, profile forms
│   ├── auth_backend.py      # Custom reg-number authentication
│   ├── templates/poll/      # All HTML templates
│   │   ├── base.html        # Base layout with cyberpunk navbar
│   │   ├── home.html        # Landing page with particle animation
│   │   ├── login.html       # Secure login form
│   │   ├── register.html    # Student registration
│   │   ├── dashboard.html   # Vote interface
│   │   ├── results.html     # Results with confetti & charts
│   │   ├── edit_profile.html
│   │   └── password.html
│   └── static/poll/         # Static assets
├── media/                   # User-uploaded files
├── Procfile                 # Render/Heroku process file
├── runtime.txt              # Python version
├── build.sh                 # Render build script
└── .env.example             # Environment variable template
```

---

## 🎨 Design System

| Token | Value | Usage |
|-------|-------|-------|
| `--neon-blue` | `#00d4ff` | Primary actions, links |
| `--neon-violet` | `#bf5fff` | Secondary accents |
| `--neon-gold` | `#ffd700` | Nomination phase, winners |
| `--neon-green` | `#00ff88` | Success, voting active |
| `--neon-red` | `#ff3366` | Errors, logout |
| `--bg-dark` | `#030712` | Background |

---

## 🔧 Common Issues

**Static files not loading in production?**
→ Make sure `whitenoise` is in MIDDLEWARE and `STATIC_ROOT` is set.

**Database errors on first deploy?**
→ Run `python manage.py migrate` as part of your build command.

**Media files not showing?**
→ For production, use a cloud storage service like AWS S3 or Cloudinary.

---

## 📄 License
Built as a Final Year Project. Free to use and modify.
