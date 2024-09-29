# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Step 1: Data - Movie reviews and labels (0: Negative, 1: Positive)
reviews = [
    "This movie was fantastic, I loved it!", 
    "The plot was boring and predictable", 
    "Amazing performance by the cast", 
    "I wasted two hours of my life", 
    "Brilliant direction and storytelling", 
    "The movie was a disaster", 
    "What a great film!", 
    "It was an awful experience",
    "The cinematography was beautiful", 
    "Terrible acting and poor script"
]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1: Positive, 0: Negative

# Step 2: Create a pipeline to combine vectorization and model
# Vectorizer with stop words removal and other pre-processing features
vectorizer = CountVectorizer(lowercase=True, stop_words='english')
classifier = MultinomialNB()

# Pipeline to process and classify
model = make_pipeline(vectorizer, classifier)

# Step 3: Train the model
model.fit(reviews, labels)

# Step 4: Test the model with new reviews
new_reviews = ["The movie was a masterpiece", "Worst film I've ever seen", "The plot was very engaging", "Terrible acting"]
predicted = model.predict(new_reviews)

# Step 5: Output the predictions
for review, label in zip(new_reviews, predicted):
    print(f"Review: '{review}' is classified as: {'Positive' if label == 1 else 'Negative'}")
