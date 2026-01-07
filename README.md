# initiative-hub 🎲

initiative-hub is a web application built with Python and Streamlit that works as a virtual tabletop for role-playing games (RPG).  
The goal is to centralize campaigns, characters, notes, and assets in a single persistent platform.

## ✨ Features
- Create and manage RPG campaigns
- User authentication with player and game master (GM) roles
- Full CRUD for character sheets
- Flexible character storage using PostgreSQL (JSONB)
- Campaign and player notes
- Library of spells, monsters, and items (GM-focused)
- Upload and manage maps, tokens, and player icons
- Support for simultaneous online or in-person sessions
- Persistent database storage

## 🛠️ Tech Stack
- **Python** – main programming language  
- **Streamlit** – web interface  
- **PostgreSQL (Supabase)** – database and authentication  
- **GitHub** – version control and open-source collaboration  

## 📂 Project Structure
The project follows a modular and scalable structure, separating UI, business logic, and database access to keep the codebase maintainable and easy to evolve.

## 🚀 Running Locally
1. Clone the repository:
```bash
git clone https://github.com/your-username/initiative-hub.git
cd initiative-hub
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Configure environment variables:

- Copy .env.example to .env

- Fill in your Supabase credentials

4. Run the application:
```bash
streamlit run app/main.py
```

## 🔐 Environment Variables

Sensitive credentials (such as database URLs and API keys) must be stored in a .env file and are never committed to the repository.

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute the code, provided the original license is included.