# Basic Machine Learning Task: Regression

## Objective
The objective of this assignment is to write a simple Python program to perform a basic machine learning task using regression.

## Instructions
1. Fork this repository to your GitHub account.
2. Clone the forked repository to your local machine.
3. Write a Python script named `regression.py` that:
   - Generates a simple dataset.
   - Splits the dataset into training and testing sets.
   - Trains a regression model (e.g., Linear Regression) on the training set.
   - Evaluates the model on the testing set and prints the evaluation metrics (e.g., Mean Squared Error).
4. Commit your changes and push them to your forked repository.

## Requirements
- Do not import any external libraries. Use only built-in Python libraries.

## Example
Here is a basic structure of the `regression.py` script:

```python
import random

# Generate a simple dataset
data = [(x, 2*x + random.randint(-10, 10)) for x in range(100)]
X = [d[0] for d in data]
y = [d[1] for d in data]

# Split the data into training and testing sets
split_idx = int(0.8 * len(data))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# Train a simple linear regression model
def mean(values):
    return sum(values) / len(values)

def covariance(x, y, mean_x, mean_y):
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))

def variance(values, mean):
    return sum((x - mean) ** 2 for x in values)

mean_x, mean_y = mean(X_train), mean(y_train)
b1 = covariance(X_train, y_train, mean_x, mean_y) / variance(X_train, mean_x)
b0 = mean_y - b1 * mean_x

# Predict on the testing set
y_pred = [b0 + b1 * x for x in X_test]

# Evaluate the model
mse = sum((y_test[i] - y_pred[i]) ** 2 for i in range(len(y_test))) / len(y_test)
print(f'Mean Squared Error: {mse}')
