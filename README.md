
# 🎰 Baccarat Betting Simulator

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
├── app.py                # Main Streamlit app
├── simulation.py         # Core simulation engine
├── visualization.py      # Chart generation
├── output/                # Saved simulation results
├── session_history.csv    # Tracker for past sessions
├── README.md              # (This file)
└── requirements.txt       # Project dependencies
```

---

## 🖼️ Screenshots

*(Optional - Insert screenshots showing the beautiful UI here if you want.)*

---

## 📈 Changelog

See [Releases](https://github.com/treyhamilton/baccarat-betting-simulator/releases) for version history.

---

## 👨‍💻 Built With ❤️ by Trey Hamilton

---
