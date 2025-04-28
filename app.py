# app.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from simulation import run_simulation
from visualization import plot_balance_over_time, plot_win_breakdown, plot_sequence_frequency

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Path for session history
SESSION_HISTORY_PATH = "session_history.csv"

# Sidebar inputs
st.sidebar.title("🌐 Simulation Controls")
starting_balance = st.sidebar.number_input("Starting Balance", min_value=1)
starting_bet = st.sidebar.number_input("Starting Bet", min_value=1)
uploaded_file = st.sidebar.file_uploader("Upload Baccarat Outcomes CSV", type=["csv"])

# Buttons
start_simulation = st.sidebar.button("Start Simulation")
reset_app = st.sidebar.button("Reset App")

if reset_app:
    st.rerun()

# Main title
st.title("🎰 Baccarat Betting Simulator")

# Create tabs
simulator_tab, past_sessions_tab = st.tabs(["Simulator", "Past Sessions"])

# Simulator Tab
with simulator_tab:
    if start_simulation:
        if uploaded_file is None:
            st.error("Please upload a CSV file.")
        else:
            data = pd.read_csv(uploaded_file)
            results, stats = run_simulation(data, starting_balance, starting_bet)

            # Create output filename based on input file name
            input_filename = uploaded_file.name.replace('.csv', '').replace(' ', '_')
            output_path = f"output/simulation_results_{input_filename}.csv"

            results.to_csv(output_path, index=False)

            st.success(f"Simulation complete! Results saved to {output_path}")

            # 🏆 Session Summary Cards
            st.header("🏆 Session Summary")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Final Balance", f"${stats['Final Balance']:.2f}")
            col2.metric("Total Profit", f"${stats['Total Profit']:.2f}")
            col3.metric("Win Rate", stats['Win Rate'])
            col4.metric("Hands Played", stats['Hands Played'])

            # 📊 Simulation Statistics
            st.header("📊 Simulation Statistics")
            for key, value in stats.items():
                if key not in ["Final Balance", "Total Profit", "Win Rate"]:
                    st.write(f"**{key}:** {value}")

            # 📈 Visualizations
            st.header("📈 Visualizations")
            st.plotly_chart(plot_balance_over_time(results))
            st.plotly_chart(plot_win_breakdown(results))
            st.plotly_chart(plot_sequence_frequency(results))

            # 📋 Simulation Results Table Section
            st.header("📋 Simulation Results Table")
            with st.expander("Click to view full simulation details"):
                def highlight_win_loss(row):
                    if row["Result"] == "Win":
                        return ['background-color: #a5d6a7'] * len(row)
                    elif row["Result"] == "Loss":
                        return ['background-color: #ef9a9a'] * len(row)
                    else:
                        return ['background-color: #90caf9'] * len(row)
                styled_results = results.style.apply(highlight_win_loss, axis=1)
                st.dataframe(styled_results, use_container_width=True)

            # 📥 Download CSV Button
            with open(output_path, "rb") as f:
                st.download_button(
                    label="📥 Download Simulation Results CSV",
                    data=f,
                    file_name=f"simulation_results_{input_filename}.csv",
                    mime="text/csv"
                )

            # 📝 Save session summary
            session_summary = {
                "Date/Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Input File": uploaded_file.name,
                "Starting Balance": starting_balance,
                "Starting Bet": starting_bet,
                "Final Balance": stats["Final Balance"],
                "Total Profit": stats["Total Profit"],
                "Win Rate": stats["Win Rate"],
                "Hands Played": stats["Hands Played"]
            }

            if os.path.exists(SESSION_HISTORY_PATH):
                session_history = pd.read_csv(SESSION_HISTORY_PATH)
                session_history = pd.concat([session_history, pd.DataFrame([session_summary])], ignore_index=True)
            else:
                session_history = pd.DataFrame([session_summary])

            session_history.to_csv(SESSION_HISTORY_PATH, index=False)

# Past Sessions Tab
with past_sessions_tab:
    st.header("📜 Past Sessions History")
    if os.path.exists(SESSION_HISTORY_PATH):
        history = pd.read_csv(SESSION_HISTORY_PATH)

        # Filter option
        only_profitable = st.checkbox("Show Only Profitable Sessions")
        if only_profitable:
            history = history[history["Total Profit"] > 0]

        # Highlighting function
        def highlight_profit(row):
            if row["Total Profit"] > 0:
                return ['background-color: #a5d6a7'] * len(row)
            elif row["Total Profit"] < 0:
                return ['background-color: #ef9a9a'] * len(row)
            else:
                return [''] * len(row)

        # Multi-select session deletion
        selected_indices = st.multiselect(
            "Select sessions to delete (by row index):",
            options=history.index,
            format_func=lambda x: f"{history.loc[x, 'Date/Time']} - {history.loc[x, 'Input File']}",
            key="selected_sessions"
        )

        if selected_indices:
            if st.button("🗑️ Delete Selected Sessions", key="delete_button"):
                st.session_state["confirm_delete"] = True

        if st.session_state.get("confirm_delete"):
            st.warning("Are you sure you want to delete the selected sessions?", icon="⚠️")
            if st.button("Yes, delete", key="confirm_delete_button"):
                history = history.drop(st.session_state["selected_sessions"])
                history.reset_index(drop=True, inplace=True)
                history.to_csv(SESSION_HISTORY_PATH, index=False)
                st.success("Selected sessions deleted successfully!")
                st.session_state.pop("confirm_delete", None)
                st.session_state.pop("selected_sessions", None)
                st.rerun()

        styled_history = history.style.apply(highlight_profit, axis=1)

        st.dataframe(styled_history, use_container_width=True)

        st.download_button(
            label="📥 Download Full Session History",
            data=history.to_csv(index=False),
            file_name="session_history.csv",
            mime="text/csv"
        )
    else:
        st.info("No past sessions found. Run a simulation first!")
