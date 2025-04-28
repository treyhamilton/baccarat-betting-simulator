
import pandas as pd
import plotly.express as px

def plot_balance_over_time(results):
    fig = px.line(results, x='Hand', y='Balance', title='Balance Over Time')
    return fig

def plot_win_breakdown(results):
    win_count = (results['Result'] == 'Win').sum()
    loss_count = (results['Result'] == 'Loss').sum()
    tie_count = (results['Result'] == 'Push').sum()

    breakdown = pd.DataFrame({
        'ResultType': ['Win', 'Loss', 'Tie'],
        'Count': [win_count, loss_count, tie_count]
    })

    fig = px.pie(breakdown, names='ResultType', values='Count', title='Win/Loss/Tie Breakdown')
    return fig

def plot_sequence_frequency(results):
    sequence_counts = results['Sequence Step'].value_counts().sort_index()
    fig = px.bar(sequence_counts, x=sequence_counts.index, y=sequence_counts.values,
                 labels={'x': 'Sequence Position', 'y': 'Number of Bets'},
                 title='Sequence Betting Frequency')
    return fig
