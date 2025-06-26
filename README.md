# MoeGPT

Welcome to **MoeGPT** – an interactive, user-friendly AI chatbot web application powered by Google's Gemini API and built with Django! MoeGPT is designed to provide an engaging conversational experience, allowing users to ask questions, receive rich HTML-formatted answers, and manage their chat history with ease.

---

## 🚀 Features

- **Modern Chatbot Interface:**  
  Clean, responsive UI for seamless conversations with MoeGPT.

- **Rich HTML Responses:**  
  Answers are formatted with HTML, including tables, code blocks, and styled text for enhanced readability.

- **Code Highlighting:**  
  Code responses are beautifully colored and formatted, preserving indentation and syntax.

- **User Authentication:**  
  Secure registration, login, and logout flows with real-time validation for usernames and emails.

- **Chat History Management:**  
  Organize conversations into modules, view previous chats, and delete history as needed.

- **Profile Dashboard:**  
  View your profile, chat statistics, and account details in a stylish card layout. (Not available in this version)

- **Error Handling:**  
  Friendly error pages for invalid locations or API issues, ensuring a smooth user experience.

---

## 🛠️ Technology Stack

- **Backend:** Django 5.1.x
- **Frontend:** Bootstrap 5, HTML5, CSS3, FontAwesome
- **AI Integration:** Google Gemini API (via `google-generativeai`)
- **Database:** SQLite (default, can be swapped for PostgreSQL/MySQL)
- **Authentication:** Django's built-in user system

---

## 📦 Project Structure

```
moegpt/
├── authorization/         # User authentication app
│   ├── templates/
│   ├── views.py
│   └── ...
├── chatbot/               # Chatbot logic and UI
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── ...
├── moegpt/                # Project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3             # SQLite database (default)
├── requirements.md        # This README file
└── ...
```

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/VasudevAdhikari/moegpt.git
cd moegpt
```

### 2. Install Dependencies

Make sure you have Python 3.10+ and pip installed.

```bash
pip install -r requirements.txt
```

**Required packages include:**
- Django >= 5.1
- google-generativeai
- google-api-core

### 3. Set Up Environment Variables

Edit `moegpt/settings.py` and set your Google Gemini API key:

```python
GENERATIVE_AI_KEY = "YOUR-GEMINI-API-KEY"
```

> **Note:** For production, use environment variables or a secrets manager.

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## ✨ Usage

- **Register:** Create a new account via the registration page.
- **Login:** Access the chatbot after logging in.
- **Chat:** Ask questions, receive answers, and enjoy rich formatting.
- **History:** View, switch, or delete chat modules from the history dropdown.
- **Profile:** See your stats and account info on the profile page.
- **Logout:** Securely log out at any time.

---

## 🧩 Customization

- **Styling:**  
  Modify the Bootstrap-based templates in `chatbot/templates/` and `authorization/templates/` for your branding.

- **Database:**  
  Switch to PostgreSQL or MySQL by updating `DATABASES` in `settings.py`.

- **AI Model:**  
  Change the Gemini model version or prompt formatting in `chatbot/views.py`.

---

## 🛡️ Security & Best Practices

- **Never commit your API keys to version control.**
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` for production.
- Use HTTPS and secure session settings in production.

---

## 🧪 Testing

Run Django's test suite:

```bash
python manage.py test
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Credits

- [Django](https://www.djangoproject.com/)
- [Google Gemini API](https://ai.google.dev/)
- [Bootstrap](https://getbootstrap.com/)
- [FontAwesome](https://fontawesome.com/)

---

## 🌟 Get Started Now!

Unleash the power of conversational AI with MoeGPT.  
Ask anything, get everything – beautifully formatted, instantly.

---
