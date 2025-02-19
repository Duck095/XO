import torch
import torch.nn as nn

BOARD_SIZE = 8
NUM_ACTIONS = BOARD_SIZE * BOARD_SIZE  # 64 ô

class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(NUM_ACTIONS, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, NUM_ACTIONS)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
