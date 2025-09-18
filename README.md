[README.md](https://github.com/user-attachments/files/22414528/README.md)
# 📊 CORD-19 Data Explorer

This project is a beginner-friendly **data analysis and visualization tool** built with **Streamlit**, using the **CORD-19 research dataset**.  
It demonstrates how to **load, clean, analyze, and visualize real-world data** in an interactive web application.

---

## 🚀 Features

- **Data Loading & Exploration**
  - Load the `metadata.csv` file (1M+ research papers metadata)
  - Display dataset sample, shape, data info, missing values, and summary statistics

- **Data Cleaning & Preparation**
  - Convert `publish_time` to datetime
  - Extract publication year
  - Compute abstract word counts
  - Remove columns with too many missing values

- **Data Analysis & Visualizations**
  - 📈 Publications over time (line chart)
  - 📊 Top journals publishing COVID-19 research (bar chart)
  - ☁️ Word cloud of research paper titles
  - 📑 Distribution of paper counts by source

- **Interactive Web App**
  - Filter publications by year range (slider)
  - View filtered dataset (titles, authors, journals)

---

## 🛠️ Tech Stack

- [Python 3.7+](https://www.python.org/)  
- [Pandas](https://pandas.pydata.org/) – data manipulation  
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) – visualization  
- [WordCloud](https://pypi.org/project/wordcloud/) – word cloud generation  
- [Streamlit](https://streamlit.io/) – interactive web app framework  

---

## 📂 Project Structure

