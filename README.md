# 📊 Student Depression Analysis

<p style="font-size:18px">
This project analyzes a <strong>Student Depression Dataset</strong> to understand mental health trends and predictors among students. It combines statistical summaries, data preprocessing, and insightful visualizations to explore how demographic, academic, and lifestyle factors contribute to depression.
</p>

---

## 🧾 Dataset Description

The dataset contains various features aimed at capturing the mental health state of students. It includes:

- **Demographic Details:** Age, Gender, City  
- **Academic Factors:** CGPA, Academic Pressure, Study Satisfaction  
- **Lifestyle & Wellbeing:** Sleep Duration, Dietary Habits, Work/Study Hours  
- **Mental Health Indicators:** Financial Stress, Family History, Suicidal Thoughts  
- **Target Variable:** `Depression` (0 = Not Depressed, 1 = Depressed)

### 🛠️ Preprocessing Steps

- Handled missing values in the `Age` column using the **median**
- Converted `Gender` to numerical format (Male → 0, Female → 1)
- Dropped `Work Pressure` and `Job Satisfaction` as less relevant

---

## 📌 Key Findings

- 🔍 The `Age` column had missing values that were imputed using the **median**
- ⚙️ Gender was encoded numerically for analysis
- 📉 **Depression** is linked to:
  - Higher **academic and financial stress**
  - Low **study/job satisfaction**
  - Certain **degrees** and **gender combinations**

### 📊 Statistical Summary (Age)

- **Mean:** ~24  
- **Median (Depression):** varies  
- **Standard Deviation:** ~3.7

---

## 📈 Insights from Visualizations

- 🟥 **Histogram** of Age Distribution shows visible difference in depressed vs. non-depressed students
- 📊 **Bar Plot** shows differences in depression rates across degree types
- 🔵 **Scatter Plot** visualizes Age vs CGPA, colored by depression status
- 📐 **Z-Score Analysis** used for identifying outliers in Age
- 👥 **Young Adults Focus:** Students aged 18–25 form a key at-risk group

---

## 📁 Files

- `data1.csv` – The input dataset  
- `analysis_script.py` – Python script for data processing & visualization  
- `README.md` – Project documentation  

---

## ✅ Requirements

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn
