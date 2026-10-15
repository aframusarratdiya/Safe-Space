# Safe Space 🧠💚

Safe Space is a Flask-based web application designed to provide a supportive, compassionate, and anonymous environment for individuals seeking mental health assistance. It features real-time support channels, licensed listener matching, peer group chats, journaling, habit tracking, and an AI-powered empathetic chatbot companion.

## ✨ Key Features

* **Anonymous User Mode**: Allows normal users to toggle anonymity on or off so they can seek support without revealing their personal identity in chats and groups.
* **Peer Support Groups**: Create, join, and participate in community group chats focused on mutual wellness and recovery.
* **Verified Listeners & Rating System**: Users can apply to become listeners, connect with approved listeners, and rate their support sessions (1–5 stars).
* **Daily Mood Tracker & Streak Counter**: Log daily moods, track emotional trends over time, and build self-care streaks.
* **Habit Tracker**: Build positive wellness habits and monitor weekly progress visually.
* **Private Journaling**: A secure space for users to write down personal thoughts and reflections.
* **Emergency Helplines**: Quick access to localized and national emergency mental health hotlines and support organizations.
* **Dual Database Support**: Configured for local development using SQLite and production deployment using PostgreSQL (Render-ready).

## 📁 Project Structure

```text
safe-space-app/
├── app.py                      # Main Flask application, database models, and AI logic
├── make_admin.py               # Utility script to promote users to admin
├── migrate_sqlite_to_postgres.py # Helper script for database migration
├── render.yaml                 # Render cloud deployment blueprint
├── Procfile                    # Gunicorn production server configuration
├── requirements.txt            # Python dependencies (includes OpenAI & Flask)
├── README.md                   # Project documentation
├── templates/                  # HTML templates
│   ├── base.html               # Base layout template
│   ├── home.html               # Homepage with daily quotes & quick links
│   ├── login.html              # User login
│   ├── register.html           # User registration
│   ├── chat.html               # 1-on-1 chat interface (supports AI bot)
│   ├── group_chat.html         # Community group chat interface
│   ├── inbox.html              # Direct message inbox
│   ├── mood.html               # Mood tracking dashboard
│   ├── journal.html            # Personal journal
│   ├── habit_tracker.html      # Habit building dashboard
│   ├── select_listener.html    # Listener directory & rating interface
│   ├── anonymity.html          # Anonymity preference settings
│   ├── helpline.html           # Emergency mental health contacts
│   ├── profile.html            # User profile and password management
│   ├── admin_panel.html        # Admin management for listener applications
│   └── apply_listener.html     # Application page to become a listener
└── static/                     # Static assets (CSS, images)
    └── style.css               # Application stylesheet
```

🛠️ Local Setup & Installation

Follow these steps to run the application locally on your machine:

1. Clone the Repository

git clone <your-repository-url>
cd safe-space-app


2. Create and Activate a Virtual Environment

python -m venv venv
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate


3. Install Dependencies

pip install -r requirements.txt


4. Configure Environment Variables

Create a file named .env in the root directory of your project and add your OpenAI API key:

OPENAI_API_KEY=your_actual_openai_api_key_here


Note: If the OPENAI_API_KEY is missing or invalid, the app will gracefully fall back to a compassionate offline response message instead of crashing.

5. Run the Application

python app.py


When the app starts, it automatically initializes the database, creates tables, and seeds a special Bot user account into the system.

Open your web browser and navigate to: http://127.0.0.1:5000

🤖 How the AI Bot Works

Upon startup, the app creates a system user with the username Bot.

When logged in, users can click "Chat with Bot" from the navigation links.

Messages sent to the bot are processed via OpenAI's gpt-4o-mini model with a tailored system prompt designed to ensure compassionate, safe, and short mental-health-focused guidance.

👑 Managing Admin Access

To promote a registered user to an administrator:

Run the admin utility script:

python make_admin.py


Enter the target username when prompted.

🚀 Deployment

This project includes production configuration files (render.yaml and Procfile) for seamless deployment on platforms like Render. It automatically detects production environments via environment variables and switches from local SQLite to PostgreSQL.

🛡️ License

This project is open-source and available under the MIT License.
