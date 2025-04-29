
# 🎰 Baccarat Betting Simulator

[![Streamlit App](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

> A professional-grade, Streamlit-based simulation tool for analyzing baccarat betting strategies and results across multiple sessions.

---

## 🚀 Features

- Run custom betting simulations using real baccarat outcomes
- Configure starting balance and bet amounts
- Smart betting sequence handling (Player → Banker → Player → Player → Banker → Banker)
- Full session statistics and win/loss tracking
- Dynamic charts: Balance Over Time, Win/Loss Breakdown, Betting Sequences
- Save and load past simulation sessions easily
- View, filter, and delete session history cleanly
- Professional UI with Streamlit tabs, metrics, graphs, and download options
- Export detailed CSV results automatically
- Future-proof design with scalable session management
- 🔐 **Secure Login and Registration system**  
- 🗄️ **SQLite database** to store user accounts  
- 🔒 **Passwords hashed** with bcrypt for security  
- 🎨 **Premium styled login/register pages** (casino green/white theme)  
- 📲 **Remember Me** session support  
- 🧹 Minor UI and backend improvements

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/treyhamilton/baccarat-betting-simulator.git
cd baccarat-betting-simulator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 🎮 How to Use

1. Upload a CSV file containing baccarat outcomes (Player, Banker, Tie).
2. Set your starting balance and starting bet.
3. Click **Start Simulation** to generate detailed results.
4. Or load a **previous simulation** by selecting:
   - Baccarat Round
   - Starting Balance
   - Starting Bet
5. View session stats, graphs, and export results if needed!

---

## 📂 Folder Structure

```
# 📄 Baccarat Betting Simulator — Project Structure

baccarat-betting-simulator/
├── __pycache__/
├── baccarat_round_outcomes/     # CSV files containing outcomes - Used for input
├── output/                      # Saved simulation results
├── app.py                       # Main Streamlit app
├── auth.py                      # User authentication logic (login, register, password hashing)
├── CHANGELOG.md                 # Version change updates
├── README.md                    # (This file)
├── requirements.txt             # Project dependencies
├── session_history.csv          # Tracker for past sessions
├── simulation.py                # Core simulation engine
├── users.db                     # SQLite database storing user credentials
├── visualization.py             # Chart generation

```

---

## 🖼️ Screenshots

*(Optional - Insert screenshots showing the beautiful UI here if you want.)*

---

## 📈 Changelog

See [Releases](https://github.com/treyhamilton/baccarat-betting-simulator/releases) for version history.

---

## 👨‍💻 Built by Trey Hamilton

---
