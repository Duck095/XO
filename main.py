import csv
from minimax import MinimaxBot
from DQN_bot import DQNBot
from game_play import play_game

dqn_bot = DQNBot("dqn_model.pth")
minimax_bot = MinimaxBot()

results = []

for i in range(1000):
    winner = play_game(minimax_bot, dqn_bot)
    results.append((i + 1, winner))

with open("results/match_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Game", "Winner"])
    writer.writerows(results)

print("Match results saved to match_results.csv")
