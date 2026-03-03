# TELUGU_MOVIE_RECOMMENDATION_SYSTEM-1-
🎬 Telugu Movie Recommendation System
📌 Project Overview

The Telugu Movie Recommendation System is a content-based recommendation application developed using Python, Machine Learning, and Streamlit. The system helps users discover Telugu movies based on their preferred genre and number of recommendations.

With the growing number of Telugu films released every year across multiple genres, users often find it difficult to choose movies that match their interests. This project aims to simplify the movie selection process by providing intelligent recommendations based on movie content.

🎯 Objective

The main objective of this project is to build a content-based movie recommendation system that:

Allows users to select a genre

Allows users to specify the number of movies they want

Recommends top-rated movies in the selected genre

Displays detailed movie information including overview and rating

Uses Machine Learning techniques to analyze movie content

🧠 Methodology

The system follows a content-based filtering approach using Natural Language Processing techniques.

1️⃣ Data Preprocessing

Cleaned the dataset by handling missing values

Converted ratings to numeric format

Combined important text features (Genre + Overview)

2️⃣ Feature Engineering

A new column called combined_features was created by merging:

Genre

Movie Overview

This improves contextual understanding of each movie.

3️⃣ Text Vectorization (TF-IDF)

TF-IDF (Term Frequency – Inverse Document Frequency) is used to convert textual data into numerical vectors. It assigns higher weight to important words and reduces the importance of common words.

4️⃣ Similarity Calculation (Cosine Similarity)

Cosine similarity is applied to measure the similarity between movies based on their vector representations. Movies with higher similarity scores are considered more related.

5️⃣ Recommendation Logic

User selects a genre

System filters movies of that genre

Movies are ranked based on rating

Top N movies are displayed with overview and rating

🖥️ Technologies Used

Python

Pandas (Data Processing)

Scikit-learn (TF-IDF & Cosine Similarity)

Streamlit (Web Interface)

Matplotlib (Data Visualization)

📊 Type of Machine Learning

This project uses:

Unsupervised Learning

Content-Based Filtering

Natural Language Processing (NLP)

Since the system does not predict a target variable and instead finds similarity between movies, it falls under unsupervised learning.

🚀 Features

Interactive web interface

Genre selection from available dataset

User-defined number of recommendations

Top-rated movies in selected genre

Movie overview display

Clean and responsive UI

🔮 Future Enhancements

Add collaborative filtering

Implement hybrid recommendation system

Integrate movie posters using TMDB API

Add user login and personalized recommendations

Deploy application online

📌 Conclusion

The Telugu Movie Recommendation System demonstrates the practical implementation of machine learning and NLP techniques in building real-world recommendation systems. The project successfully provides relevant movie suggestions based on user preferences, improving user experience and decision-making.
