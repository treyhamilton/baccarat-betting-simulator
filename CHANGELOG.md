# 📜 CHANGELOG

All notable changes to this project will be documented in this file.

## [v1.3] - 2025-04-28

### Major Enhancements
- Added multi-level dynamic dropdowns to **Load Past Simulation** tab
  - Select by Baccarat Round ➔ Starting Balance ➔ Starting Bet
  - Browse and reload any past simulation without rerunning
- Updated simulation results file naming to include:
  - Input File Name, Starting Balance, Starting Bet, and Timestamp
  - Example: `simulation_results_lonestar_rd3_500_5_20250428_1945.csv`
- Improved session history tracking with a new field for the Output File name
- Ensured clean separation between **New Simulations** and **Past Simulations** browsing
- Added automatic prevention of file overwriting for different runs on the same input file

### Bug Fixes
- Fixed potential KeyError when loading outdated session history files
- Added error handling for missing past simulation files

### UI/UX Improvements
- Clean, intuitive multi-level dropdown selection system for past simulations
- Friendly success/error messages for loading simulations
- Enhanced scalability for managing many simulations across multiple rounds and parameter sets

---

## [v1.2] - 2025-04-28
### Added
- Ability to **select and delete specific past sessions** from session history
- Multi-select sessions based on Date/Time and Input Filename
- **Confirmation step** before session deletion
- Live session table refresh after deletions

### Fixed
- Streamlit compatibility: updated rerun method to `st.rerun` for newer versions
- Minor UI improvements for better session management flow

---

## [v1.0] - 2025-04-27
### Added
- Initial release of **Baccarat Betting Simulator**
- Custom betting sequence (P ➔ B ➔ P ➔ P ➔ B ➔ B)
- Bet doubling logic on loss
- Tie handling rules
- Full session result statistics tracking
- Balance Over Time Line Chart
- Win/Loss/Tie Breakdown Pie Chart
- Sequence Betting Frequency Bar Chart
- Simulation results downloadable as CSV
- Streamlit-based professional UI
