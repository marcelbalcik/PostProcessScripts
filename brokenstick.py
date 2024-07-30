#This Python script is designed to analyze the glass transition temperature (Tg) of polymers by applying a broken-stick regression model to experimental data. 
#The script reads temperature-volume data from a text file and uses broken-stick regression to identify a significant change in the polymer's volume response due to temperature variations.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression

# Function to calculate total squared error of two linear regressions divided at index idx
def total_squared_error(idx, X, Y):
    reg1 = LinearRegression().fit(X[:idx], Y[:idx])
    reg2 = LinearRegression().fit(X[idx:], Y[idx:])
    pred1 = reg1.predict(X[:idx])
    pred2 = reg2.predict(X[idx:])
    error1 = np.sum((Y[:idx] - pred1)**2)
    error2 = np.sum((Y[idx:] - pred2)**2)
    return error1 + error2

# Load data
file_path = 'your_data_file.txt'  # Specify your file path
data = pd.read_csv(file_path, delim_whitespace=True)
X = data['Temperature'].values.reshape(-1, 1)
Y = data['Volume'].values

# Find the best breakpoint
result = minimize(lambda idx: total_squared_error(int(idx), X, Y), x0=[len(X) // 2], bounds=[(1, len(X)-1)])
best_idx = int(result.x)

# Fit models on both segments
reg1 = LinearRegression().fit(X[:best_idx], Y[:best_idx])
reg2 = LinearRegression().fit(X[best_idx:], Y[best_idx:])

# Predict values
Y_pred1 = reg1.predict(X[:best_idx])
Y_pred2 = reg2.predict(X[best_idx:])

# Plot results
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='blue', label='Data')
plt.plot(X[:best_idx], Y_pred1, 'r-', label='Segment 1 Fit')
plt.plot(X[best_idx:], Y_pred2, 'g-', label='Segment 2 Fit')
plt.axvline(X[best_idx], color='black', linestyle='--', label='Breakpoint at {:.2f}'.format(X[best_idx][0]))
plt.xlabel('Temperature')
plt.ylabel('Volume')
plt.title('Broken Stick Regression for Glass Transition Temperature')
plt.legend()
plt.savefig('Broken_Stick_Regression.jpg')  # Save the plot as a JPEG file
plt.show()

print(f"Estimated breakpoint (Glass Transition Temperature): {X[best_idx][0]} °C")