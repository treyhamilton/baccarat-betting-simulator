
import pandas as pd

def run_simulation(data, starting_balance, starting_bet):
    sequence = ["Player", "Banker", "Player", "Player", "Banker", "Banker"]
    balance = starting_balance
    sequence_index = 0
    current_bet = starting_bet

    stats = {
        "Player Wins": 0,
        "Banker Wins": 0,
        "Ties": 0,
        "Wins on Player": 0,
        "Wins on Banker": 0,
        "Losses on Player": 0,
        "Losses on Banker": 0,
        "Hands Played": 0,
        "Sequence 1 Bets": 0,
        "Sequence 2 Bets": 0,
        "Sequence 3 Bets": 0,
        "Sequence 4 Bets": 0,
        "Sequence 5 Bets": 0,
        "Sequence 6 Bets": 0,
    }

    results = []

    for i, outcome in enumerate(data['Winning Outcome']):
        if balance < current_bet:
            break

        bet_side = sequence[sequence_index]
        sequence_index_saved = sequence_index
        stats[f"Sequence {sequence_index_saved + 1} Bets"] += 1
        bet_placed = current_bet

        if outcome == "Tie":
            stats["Ties"] += 1
            result = "Push"
            payout = 0
        elif bet_side == outcome:
            result = "Win"
            payout = bet_placed * (1 if bet_side == "Player" else 0.95)
            balance += payout
            sequence_index = 0
            current_bet = starting_bet
            stats[f"Wins on {bet_side}"] += 1
        else:
            result = "Loss"
            balance -= bet_placed
            sequence_index += 1
            stats[f"Losses on {bet_side}"] += 1
            if sequence_index >= len(sequence):
                sequence_index = 0
                current_bet = starting_bet
            else:
                current_bet = bet_placed * 2

        stats["Hands Played"] += 1
        if outcome == "Player":
            stats["Player Wins"] += 1
        elif outcome == "Banker":
            stats["Banker Wins"] += 1

        results.append({
            "Hand": i+1,
            "Bet Side": bet_side,
            "Bet Amount": bet_placed,
            "Outcome": outcome,
            "Result": result,
            "Balance": balance,
            "Sequence Step": sequence_index_saved + 1
        })

    final_stats = {
        **stats,
        "Final Balance": balance,
        "Total Profit": balance - starting_balance,
        "Win Rate": f"{(stats['Wins on Player'] + stats['Wins on Banker']) / max(stats['Hands Played'], 1) * 100:.2f}%"
    }

    return pd.DataFrame(results), final_stats
