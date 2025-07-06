
# 📰 Fake News Detection App

A machine learning web application built using **Streamlit** to classify news articles as **Fake** or **Real**. It uses a TF-IDF vectorizer and a trained scikit-learn model.

---

## 🚀 Features

- Classifies news articles as Fake or Real
- Interactive web interface using Streamlit
- Uses a pre-trained model for fast predictions
- Simple to run locally with minimal setup

---

## 🧠 How It Works

1. The model is trained in `Fake_News_Detection.ipynb` using a labeled dataset.
2. A TF-IDF vectorizer converts news text into numerical features.
3. A scikit-learn classifier is trained (e.g., PassiveAggressiveClassifier).
4. The model and vectorizer are saved as `.pkl` files in the `models/` folder.
5. The Streamlit app (`fnd_app_py.py`) loads them to make predictions.

---

## 📁 Project Structure

```
.
├── fnd_app_py.py                # Streamlit app script
├── Fake_News_Detection.ipynb    # Jupyter notebook for training model
└── README.md                    # This file
```

---


## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/prasadloki/fake-news-detection.git
cd fake-news-detection
```

### 2. (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

## ▶️ Run the App

```bash
streamlit run fnd_app_py.py
```

Your browser will open at [http://localhost:8501](http://localhost:8501)

---

## 🧪 Try These Examples

Paste the following into the app:

- `"NASA discovers alien base under Antarctica."` → 🟥 Fake  
- `"The RBI raised the repo rate to manage inflation."` → 🟩 Real  
- `"Drinking Dettol cures COVID-19, says viral message."` → 🟥 Fake  
- `"India's PM speaks at the UN climate conference."` → 🟩 Real  

---

## ✅ To-Do (Optional Improvements)

- Show prediction confidence score
- Add example buttons in the UI
- Deploy to Streamlit Cloud
- Add word importance visualization (e.g., LIME/SHAP)

---

## 👤 Author

**Prasad Bodduboina**  
📧 [bodduboinaprasad@gmail.com]

---

## 🙏 Acknowledgments

- Streamlit for UI
- Scikit-learn for machine learning
- The dataset source (Kaggle or other)
