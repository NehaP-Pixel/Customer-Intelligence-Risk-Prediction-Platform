import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pathlib import Path

# Find project folder
BASE_DIR = Path(
    r"C:\Users\DELL\OneDrive\Desktop\AIML-W1-Employee-Attrition"
)

# Load dataset
df = pd.read_csv(BASE_DIR / "dataset" / "employee_attrition.csv")

# Features
features = [
    "Age",
    "Monthly_Income",
    "Year_At_Company",
    "Job_Satisfaction",
    "Overtime",
    "Distance_From_Home"
]

X = df[features].copy()

# Convert Overtime
X["Overtime"] = X["Overtime"].astype(str).str.strip().str.lower()

X["Overtime"] = X["Overtime"].map({
    "yes": 1,
    "no": 0,
    "1": 1,
    "0": 0
})

# Convert all features to numeric
for column in features:
    X[column] = pd.to_numeric(X[column], errors="coerce")

# Remove rows containing missing values
X = X.dropna()

# Make sure y has the same rows
y = df.loc[X.index, "Attrition"]

# Remove missing target values
valid_rows = y.notna()

X = X.loc[valid_rows]
y = y.loc[valid_rows]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train Logistic Regression
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)


# Prediction function
def predict_attrition():

    age = float(input("Age: "))
    income = float(input("Monthly Income: "))
    years = float(input("Years at Company: "))
    satisfaction = float(input("Job Satisfaction: "))

    overtime = input("Overtime (Yes/No): ").strip().lower()

    if overtime == "yes":
        overtime_value = 1
    else:
        overtime_value = 0

    distance = float(input("Distance From Home: "))

    # Create DataFrame with proper feature names
    input_data = pd.DataFrame([[
        age,
        income,
        years,
        satisfaction,
        overtime_value,
        distance
    ]], columns=features)

    # Make prediction
    prediction = model.predict(input_data)

    if prediction[0] == "Yes":
        return "Prediction: High Attrition Risk"
    else:
        return "Prediction: Low Attrition Risk"


# Run prediction
if __name__ == "__main__":
    print(predict_attrition())