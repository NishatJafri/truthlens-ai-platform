# 🔎 TruthLens: AI-Powered Data Quality & Reliability Assessment Platform

## 📌 Overview

TruthLens is an AI-powered data analysis platform designed to evaluate the **trustworthiness of datasets**.
It detects anomalies, bias, and data quality issues, and generates a **Truth Score** to measure dataset reliability.

---

## 🚀 Features

* 📂 Upload and explore datasets
* ⚙️ Automated data preprocessing
* ⚠️ Anomaly detection using Isolation Forest
* ⚖️ Bias detection across categorical features
* 📊 Data quality analysis (missing values, statistics)
* 🧠 Explainable AI for anomaly insights
* 📈 Interactive visualizations
* 🎯 Truth Score (overall dataset reliability)

---

## 🧠 How It Works

1. **Data Preprocessing**

   * Removes duplicates
   * Handles missing values
   * Scales numerical data

2. **Anomaly Detection**

   * Uses Isolation Forest algorithm
   * Flags unusual data points

3. **Bias Detection**

   * Detects imbalance in categorical data
   * Calculates bias score

4. **Truth Score Calculation**

   * Combines anomaly and bias scores
   * Generates a reliability percentage

5. **Explanation Engine**

   * Explains why a data point is anomalous
   * Uses statistical deviation logic

---

## 🖥️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Streamlit**
* **Matplotlib, Seaborn**

---

## 📁 Project Structure

```
TruthLens/
│── data/
│── models/
│── pages/
│── src/
│   ├── preprocessing.py
│   ├── anomaly_detection.py
│   ├── bias_detection.py
│   ├── truth_score.py
│   ├── explanation_engine.py
│── utils/
│── App.py
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone <your-repo-link>
cd TruthLens
```

2. Create virtual environment:

```
python -m venv venv
```

3. Activate environment:

```
.\venv\Scripts\activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Run the app:

```
streamlit run App.py
```

---

## 📊 Output Example

* Truth Score: **85%**
* Bias detected in: `gender`
* Anomalies detected: `12 rows`
* Explanation:

  * "Salary significantly higher than average"
  * "Age significantly lower than average"

---

## 🎯 Use Cases

* Data quality validation
* Fraud detection
* AI model fairness checking
* Business data auditing

---

## 💡 Future Enhancements

* Advanced fairness metrics
* Real-time data monitoring
* Model saving & reuse
* Dashboard export (PDF reports)

---

## 👩‍💻 Author

**Nishat & Aisha **
MCA Students

---

## ⭐ Final Note

TruthLens aims to bring **transparency and trust** into data-driven systems by combining
AI, statistics, and explainability in one platform.
