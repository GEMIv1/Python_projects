# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# Load  historical financial data from the csv file
data = pd.read_excel('a_Dataset_CreditScoring.xlsx')

# Explore and preprocess the data
data = data.drop('ID', axis=1)  # we don't need the id
data = data.fillna(data.mean())  # filling missing values with mean

X = data.iloc[:, 1:28].values
y = data.iloc[:, 0].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Data normalization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Risk model building
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# Evaluate the model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))

# checking the probability
predictions = classifier.predict_proba(X_test)

# model output file
df_prediction_prob = pd.DataFrame(predictions, columns=['Prob_0', 'Prob_1'])
df_prediction_target = pd.DataFrame(classifier.predict(X_test), columns=['Predicted_Target'])
df_test_data = pd.DataFrame(y_test, columns=['Actual Outcome'])
dfx = pd.concat([df_test_data, df_prediction_target, df_prediction_prob], axis=1)

# Use double backslashes or a raw string for file path
dfx.to_csv(r"D:\python\py\Python projects\Credit Scoring Model\output.csv")
dfx.head()