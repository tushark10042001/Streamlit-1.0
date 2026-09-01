from sklearn.linear_model import LinearRegression
import joblib

# Training data
X = [[500], [1000], [1500], [2000], [2500]]
y = [25, 50, 75, 100, 125]

# Create model
model = LinearRegression()

# Train
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved!")