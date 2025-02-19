import torch
import numpy as np
from dqn_model import DQN

BOARD_SIZE = 8

class DQNBot:
    def __init__(self, model_path="dqn_model.pth"):
        self.model = DQN()
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()

    def get_move(self, board):
        state = np.array([1 if cell == "X" else -1 if cell == "O" else 0 for row in board for cell in row], dtype=np.float32)
        state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)

        with torch.no_grad():
            q_values = self.model(state_tensor)
            action = q_values.argmax().item()

        r, c = divmod(action, BOARD_SIZE)
        return (r, c) if board[r][c] == " " else None
