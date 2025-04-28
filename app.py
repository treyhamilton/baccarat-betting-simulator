# app.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from simulation import run_simulation
from visualization import plot_balance_over_time, plot_win_breakdown, plot_sequence_frequency

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Sidebar inputs
st.sidebar.title("🌐 Simulation Controls")
starting_balance = st.sidebar.number_input("Starting Balance", min_value=1)
starting_bet = st.sidebar.number_input("Starting Bet", min_value=1)
uploaded_file = st.sidebar.file_uploader("Upload Baccarat Outcomes CSV", type=["csv"])

# Buttons
start_simulation = st.sidebar.button("Start Simulation")
reset_app = st.sidebar.button("Reset App")

if reset_app:
    st.experimental_rerun()

# Main title
st.title("🎰 Baccarat Betting Simulator")

if start_simulation:
    if uploaded_file is None:
        st.error("Please upload a CSV file.")
    else:
        data = pd.read_csv(uploaded_file)
        results, stats = run_simulation(data, starting_balance, starting_bet)

        # 🛠 Create output filename based on input file name
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
