# 🏠 House Price Prediction ML

> An end-to-end Machine Learning web app that predicts house prices based on area and number of bedrooms — built with Python, Scikit-learn, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Linear Regression](https://img.shields.io/badge/Model-Linear%20Regression-0B5345?style=flat)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

---

## 🔗 Live Demo

👉 **[Click here to try the app]https://(house-price-prediction-ml-abvkn7u87dvvrnpsiebdgz.streamlit.app/)**
> *(Replace with your Streamlit Cloud link after deployment)*

---

## 📸 Preview

![App Screenshot](screenshot.png)
> *(Add a screenshot of your app here)*

---

## 🧠 How It Works

```
User Input (Area + Bedrooms)
        ↓
Linear Regression Model
        ↓
Predicted Price (₹ Lakhs)
```

The model learns the relationship between:
- **Area** (sq ft) → bigger area = higher price
- **Bedrooms** (BHK count) → more bedrooms = higher price

**Prediction Formula learned by the model:**
```
Price = (Area × 0.0496) + (Bedrooms × 4.39) + 1.29
```

**Example:** 1500 sq ft, 3 BHK → ₹ 88.88 Lakhs

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Linear Regression |
| R² Score | 0.99 |
| Mean Absolute Error | ₹ 4.22 Lakhs |
| Training Samples | 400 |
| Test Samples | 100 |

---

## 📁 Project Structure

```
house-price-prediction-ml/
│
├── app.py              # Streamlit web app (UI)
├── train.py            # Model training script
├── predict.py          # Standalone prediction script
├── model.pkl           # Saved trained model
├── housing_data.csv    # Dataset
└── README.md
```

---

## ⚙️ Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/anujapawar09/house-price-prediction-ml.git
cd house-price-prediction-ml
```

**2. Install dependencies**
```bash
pip install streamlit scikit-learn pandas numpy
```

**3. Train the model** *(skip if model.pkl already exists)*
```bash
python train.py
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data handling |
| Scikit-learn | ML model (Linear Regression) |
| Streamlit | Web app UI |
| Pickle | Model serialization |

---

## ✨ Features

- 🎯 Predicts house price instantly based on area & bedrooms
- 📐 Interactive slider for area input (500 – 5000 sq ft)
- 🛏️ Dropdown selector for BHK count (1–6 BHK)
- 💰 Clean animated price result display
- 📱 Responsive dark-themed UI

---

## 👩‍💻 Author

**Anuja Pawar**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/anujapawar9)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/anujapawar09)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-C8973A?style=flat)](https://anujapawar09.github.io/anujapawar_portfolio/)
