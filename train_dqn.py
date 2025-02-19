import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from DQN_model import DQN
from collections import deque

BOARD_SIZE = 8
NUM_ACTIONS = BOARD_SIZE * BOARD_SIZE
GAMMA = 0.95
LR = 0.001
EPSILON = 1.0
EPSILON_MIN = 0.01
EPSILON_DECAY = 0.995
BATCH_SIZE = 64
MEMORY_SIZE = 10000
EPISODES = 1000
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())
print("CUDA current device:", torch.cuda.current_device() if torch.cuda.is_available() else "None")
print("CUDA device name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None")

class DQNAgent:
    def __init__(self):
        self.model = DQN()
        self.model = DQN().to(device)
        self.target_model = DQN().to(device)
        self.memory = deque(maxlen=MEMORY_SIZE)
        self.optimizer = optim.Adam(self.model.parameters(), lr=LR)
        self.loss_fn = nn.MSELoss()

    def get_state(self, board):
        return np.array([1 if cell == "X" else -1 if cell == "O" else 0 for row in board for cell in row], dtype=np.float32)

    def choose_action(self, state, epsilon):
        if random.random() < epsilon:
            return random.randint(0, NUM_ACTIONS - 1)
        with torch.no_grad():
            state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
            return self.model(state_tensor).argmax().item()

    def train(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(self.memory, BATCH_SIZE)
        states, actions, rewards, next_states, dones = zip(*batch)
        states = torch.tensor(states, dtype=torch.float32).to(device)
        actions = torch.tensor(actions, dtype=torch.int64).unsqueeze(1).to(device)
        rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
        next_states = torch.tensor(next_states, dtype=torch.float32).to(device)
        dones = torch.tensor(dones, dtype=torch.float32).to(device)

        q_values = self.model(states).gather(1, actions).squeeze(1)
        with torch.no_grad():
            q_next = self.target_model(next_states).max(1)[0]
            q_target = rewards + GAMMA * q_next * (1 - dones)

        loss = self.loss_fn(q_values, q_target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def update_target_model(self):
        self.target_model.load_state_dict(self.model.state_dict())

def train_dqn():
    agent = DQNAgent()
    epsilon = EPSILON

    for episode in range(EPISODES):
        board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        state = agent.get_state(board)
        done = False

        while not done:
            action = agent.choose_action(state, epsilon)
            r, c = divmod(action, BOARD_SIZE)
            if board[r][c] != " ":
                continue
            board[r][c] = "X"
            reward = 0
            done = False
            next_state = agent.get_state(board)
            agent.memory.append((state, action, reward, next_state, done))
            state = next_state

        agent.train()
        agent.update_target_model()
        epsilon = max(EPSILON_MIN, epsilon * EPSILON_DECAY)

        if episode % 100 == 0:
            print(f"Episode {episode}, Epsilon: {epsilon:.4f}")

    torch.save(agent.model.state_dict(), "dqn_model.pth")
    print("Model saved!")

if __name__ == "__main__":
    train_dqn()
print("Using device:", device)
if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))
