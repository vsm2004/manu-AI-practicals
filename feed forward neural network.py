import numpy as np

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.random.rand(1, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.random.rand(1, self.output_size)
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def feedforward(self, inputs):
        # Calculate hidden layer output
        hidden_sum = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_sum)
        
        # Calculate output layer output
        output_sum = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        output = self.sigmoid(output_sum)
        
        return output
    
    def train(self, inputs, targets, epochs, learning_rate):
        for epoch in range(epochs):
            # Feedforward
            hidden_sum = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
            hidden_output = self.sigmoid(hidden_sum)
            output_sum = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
            output = self.sigmoid(output_sum)
            
            # Backpropagation
            # Calculate output layer error
            output_error = targets - output
            output_delta = output_error * self.sigmoid_derivative(output)
            
            # Calculate hidden layer error
            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * self.sigmoid_derivative(hidden_output)
            
            # Update weights and biases
            self.weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
            self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate
            
            # Print error for each epoch
            if epoch % 100 == 0:
                error = np.mean(np.abs(output_error))
                print(f"Epoch {epoch}: error {error}")


# Example usage
if __name__ == "__main__":
    # Define input, hidden, and output layer sizes
    input_size = 2
    hidden_size = 3
    output_size = 1

    # Create a feedforward neural network
    nn = FeedForwardNN(input_size, hidden_size, output_size)

    # Example training data
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])

    # Train the neural network
    nn.train(inputs, targets, epochs=1000, learning_rate=0.1)

    # Test the neural network with new data
    new_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    predictions = nn.feedforward(new_data)
    print("Predictions after training:")
    print(predictions)
