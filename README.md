# AI Powered Curriculum

## Empowering Students to Learn Purposefully
---
Anat Lorman, Alon Eitan and Barbara Aleksandrov


### **Project Overview**
In today's rapidly evolving job market, students often struggle to select courses that will enhance their employability and align with industry demands. Our project bridges this gap by providing data-driven insights to help students and job seekers make informed course selections.

By analyzing job listings and course offerings, our tool matches relevant courses to industry requirements, enabling users to gain essential skills for their desired career paths.

This project was inspired by real-world challenges faced by students selecting courses.

---

## **Data Used**
We built a large and relevant dataset from various sources:
- **Job Listings Dataset**: Scraped from **GotFriends** (~2000 rows) using celenium. Each job entry contains:
  - `job_title`
  - `job_description`
  - `job_requirements`
        
- **Course Dataset**: Gathered from **Technion (Cheesfork GitHub), Coursera, and Udemy** (~4000 rows). Each course entry contains:
  - `course_name`
  - `course_summary`
  - `course_source`

**Notes:**
- Job listings were filtered to include only data-related roles (e.g., **Data Scientist, Data Engineer, Data Analyst**).
- Technion courses were limited to the **Faculty of Data and Decision Sciences** to ensure relevance.
- Datasets links are attached down bellow.
- Code used for data scraping can be find in `scraper.py` file

---

## **AI & Algorithms Used**
### Data Preprocessing: Translation
- Used `deep-translator` (GoogleTranslator) to **translate Hebrew job listings** to English. This way is highly flexible and can be used for any other Language.

### Semantic Similarity with Sentence-BERT
- Employed **Sentence-BERT (SBERT)** `'bert-base-nli-mean-tokens'` from `sentence_transformers` library for job-course similarity analysis.
- In SBERT, Cosine similarity is used to find the best-matching courses for each job listing.

### Clustering for Trend Analysis
- Applied **K-means clustering** from `sklearn` library to identify major areas in job listings and course content.

---

## **Installation**
### 1) Clone the Repository
```sh
 git clone https://github.com/your-username/ai-powered-curriculum.git
 cd ai-powered-curriculum
```
### 2) Install Dependencies
```sh
 pip install -r requirements.txt
```
### 3) Run the Web Scraper
```sh
 python scraper.py
```
### 4) Run the Jupyter Notebook
```sh
 jupyter notebook
```
---

## **Usage**
1. Run the **web scraper** to collect job listings.
2. Load the **dataset** in the Jupyter notebook and run it
3. Generate **recommendations** for students and job seekers.

---
## **Dataset Links**:
- [Technion Course Data (Cheesfork GitHub)](https://github.com/michael-maltsev/technion-sap-info-fetcher)
- [Kaggle Udemi Course Data](https://www.kaggle.com/datasets/suddharshan/best-data-science-courses-udemy)
- [Kaggle Coursera Course Data](https://www.kaggle.com/datasets/tianyimasf/coursera-course-dataset)
- [Job Listings from GotFriends](https://www.gotfriends.co.il/)

