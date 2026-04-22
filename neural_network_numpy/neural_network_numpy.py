import numpy as np

# Input dataset (XOR problem)
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

# Expected output
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Sigmoid activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x*(1-x)

# Random seed for reproducibility
np.random.seed(1)

# Initialize weights
weights_input_hidden = np.random.rand(2,2)
weights_hidden_output = np.random.rand(2,1)

# Training
for epoch in range(10000):

    # Forward propagation
    hidden_layer = sigmoid(np.dot(X, weights_input_hidden))
    output = sigmoid(np.dot(hidden_layer, weights_hidden_output))

    # Error
    error = y - output

    # Backpropagation
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_layer)

    # Update weights
    weights_hidden_output += hidden_layer.T.dot(d_output)
    weights_input_hidden += X.T.dot(d_hidden)

print("Predicted Output:")
print(output)