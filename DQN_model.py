"""sử dụng model Deep Q-Network(DQN) để dự đoán giá trị Q cho từng hành động trong trò chơi tic-tac-toe 8x8
DQN sử dung mạng nơ-ron nhân tạo để ánh xạ trạng thái bàn cờ vào giá trị Q của từng hành động có thể thực hiện
"""
import torch
import torch.nn as nn

BOARD_SIZE = 8
NUM_ACTIONS = BOARD_SIZE * BOARD_SIZE  # 64 ô
"""ƯU:
đơn giản dễ triển khai (gồm 3 lớp), tính toán nhanh
có khả năng học chiến lược bằng cách cập nhật các giá trị Q
dùng ReLU giúp tăng tốc độ hộ tụ so với sigmoid hoạc tanh
"""
"""NHƯỢC:
không tận dụng được thông tin không gian của bàn cờ(do model coi trạng thái như vector phẳng thay vì sử dụng mô hình CNN để học đặc trưng không gian)
không có dropout hoặc batch normalization(dễ bị overfitting)
"""

class DQN(nn.Module):
    def __init__(self):
        """ 128 là giá trị phổ biến đủ mạnh để học mà không gây lãng phí tài nguyên 
        fc1 lớp có kích thức 64,số lượng neuron ẩn là 128,giúp model học các đặc trưng từ trạng thái đầu vào
        fc2 lớp tiếp theo cs 128 neuron, học các đặc trưng phức tạp hơn 
        fc3 lớp cuối ánh xạ từ 128 neuron về NUM_ACTIONS = 64 là giá trị Q của từng hành động có thể thực hiện
        """
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(NUM_ACTIONS, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, NUM_ACTIONS)

    def forward(self, x):
        """hàm dùng để xác định dữ liệu đi qua mạng neuron
        sử dụng relu sau lớp fc1/fc2 ,giữ lại các giá trị dương,giúp học được các đặc trưng phi tuyến tính
        không có activation function nào ở fc3 vì đầu ra là giá trị Q cho mỗi hành 
        """
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
