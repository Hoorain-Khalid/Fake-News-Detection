import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Load CSV files
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Label fake as 0 and true as 1
fake["label"] = 0
true["label"] = 1

# Combine both datasets
data = pd.concat([fake, true])
X = data["text"]
y = data["label"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "fake_news_model.pkl")
print("✅ Model trained and saved as fake_news_model.pkl")
