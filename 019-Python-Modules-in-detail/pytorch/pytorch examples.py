# Tensors
import torch
import torch.nn as nn
import torch.optim as optim

# Create a tensor from a Python list
data = [1, 2, 3, 4, 5]
tensor = torch.tensor(data)

print(tensor)

# Autograd

# Create a tensor with gradient tracking enabled
x = torch.tensor([2.0], requires_grad=True)

# Perform a computation
y = x ** 2 + 3 * x + 1

# Compute gradients
y.backward()

# Access the gradients
print(x.grad)

# Neural Networks

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Print the network architecture
print(net)

# Training a Model

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Training loop
for epoch in range(10):
    running_loss = 0.0

    # Forward pass, backward pass, and optimization
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f"Epoch {epoch+1} - Loss: {running_loss/len(dataloader)}")

# Saving and Loading Models

# Save the model
torch.save(net.state_dict(), 'model.pth')

# Load the model
model = SimpleNet()
model.load_state_dict(torch.load('model.pth'))
