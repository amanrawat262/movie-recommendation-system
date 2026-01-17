# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **Python and Machine Learning**, designed to suggest movies similar to a user's choice based on metadata such as genres, keywords, cast, and crew.

This project focuses on **feature engineering, text vectorization, and similarity computation**, and serves as a strong foundational ML project for data science portfolios.

---

## 🚀 Project Overview

Recommendation systems are widely used by platforms like **Netflix, Amazon Prime, and YouTube** to personalize user experience.

This project implements a **Content-Based Filtering** approach where recommendations are made by analyzing movie attributes rather than user behavior.

### The system:
- Processes movie metadata  
- Converts textual features into numerical vectors  
- Computes similarity scores  
- Recommends top similar movies  

---

## 🧠 How It Works

### 1. Data Preprocessing
- Cleaned and merged multiple movie-related columns  
- Handled missing values  
- Extracted relevant textual features  

### 2. Feature Engineering
- Combined genres, keywords, cast, and crew into a single tag  
- Applied text normalization (lowercasing, stemming)  

### 3. Vectorization
- Used **CountVectorizer** to convert text into vectors  

### 4. Similarity Calculation
- Computed **Cosine Similarity** between movie vectors  

### 5. Recommendation Logic
- Given a movie title, the system returns the **Top N similar movies**

---

## 📂 Project Structure

Movie-Recommendation-System/
│
├── move_recommending_part2.ipynb # Main Jupyter Notebook
├── data/ # Dataset files (if added)
├── images/ # Screenshots / diagrams
└── README.md # Project documentation

---

## 🛠 Tech Stack

**Programming Language:**  
- Python  

**Libraries:**  
- pandas  
- numpy  
- scikit-learn  
- nltk  

**ML Concepts:**  
- Content-Based Filtering  
- Cosine Similarity  
- NLP preprocessing  

---

## 📊 Sample Output
![git](https://github.com/amanrawat262/movie-recommendation-system/assets/117387452/5e2f951d-aa74-4cb6-af84-cbbc704f880e)


---

## 🧩 What I Learned From This Project

- How real-world recommendation systems work  
- Feature extraction from unstructured text  
- Vector space models and similarity metrics  
- Importance of data preprocessing in ML  
- Practical use of NLP in ML projects  

---

## 🔮 Future Improvements

- Add Collaborative Filtering  
- Hybrid recommendation approach  
- Deploy using Streamlit / FastAPI  
- Integrate user ratings  
- Improve recommendations using TF-IDF or Word Embeddings  

---

## ⚙️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the notebook
```bash
jupyter notebook move_recommending_part2.ipynb
```

👤 Author

Aman Rawat
🎓 M.Tech CSE | Data Science Enthusiast
💼 Software Engineer
📫 Email: amanrawat262@gmail.com

⭐ If you like this project

Give it a star ⭐ and feel free to fork or contribute!
