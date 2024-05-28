
#### 2. `regression.py`
This is the file the students will implement. Here is an example structure they might use:
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
