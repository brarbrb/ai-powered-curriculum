# AI Powered Curriculum

## Empowering Students to Learn Purposefully

### **Project Overview**
In today's rapidly evolving job market, students often struggle to select courses that will enhance their employability and align with industry demands. Our project bridges this gap by providing data-driven insights to help students and job seekers make informed course selections.

By analyzing job listings and course offerings, our tool matches relevant courses to industry requirements, enabling users to gain essential skills for their desired career paths.

This project was inspired by real-world challenges faced by students selecting courses.

---

## **Data Used**
We built a **large and relevant dataset** from various sources:
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
-   Datasets links are attached down bellow.
-   Scraping code can be find in `scraper.py` file

---

## **AI & Algorithms Used**
### **Data Preprocessing & Translation**
- Used `deep-translator` (GoogleTranslator) to **translate Hebrew job listings** to English.
- Standardized course descriptions to improve comparability.

### **Semantic Similarity with Sentence-BERT**
- Employed **Sentence-BERT (SBERT)** for job-course similarity analysis.
- **Cosine similarity** was used to find the best-matching courses for each job listing.

### **Clustering for Trend Analysis**
- Applied **K-means clustering** to identify major areas in job listings and course content.

---

## **Installation**
### **1) Clone the Repository**
```sh
 git clone https://github.com/your-username/ai-powered-curriculum.git
 cd ai-powered-curriculum
```
### **2) Install Dependencies**
```sh
 pip install -r requirements.txt
```
### **3) Run the Web Scraper**
```sh
 python scraper.py
```
### **4) Run the Jupyter Notebook for Analysis**
```sh
 jupyter notebook
```
---

## **Usage**
1. Run the **web scraper** to collect job listings.
2. Load the **dataset** in the Jupyter notebook.
3. Use the **SBERT model** to find relevant courses for a given job listing.
4. Analyze trends using **K-means clustering**.
5. Generate **recommendations** for students and job seekers.
---

## **Evaluation & Results**

### **Key Findings**
- Courses with **high similarity scores** to multiple jobs are likely to be **key skill boosters**.
- Some job listings used **vague buzzwords**, leading to challenges in precise course matching.
- Filtering job listings significantly improved recommendation relevance.

  ### **Challenges Faced**
- **Varying Writing Styles**: Course summaries and job descriptions had different structures, affecting similarity scores.
- **Computational Resources**: Training SBERT on large datasets required significant processing time.
- **Empirical Evaluation**: Lack of ground-truth data made it difficult to quantitatively assess the accuracy of our recommendations.

---
## **Dataset Links**:
- [Technion Course Data (Cheesfork GitHub)](https://github.com/michael-maltsev/technion-sap-info-fetcher)
- [Kaggle Udemi Course Data](https://www.kaggle.com/datasets/suddharshan/best-data-science-courses-udemy)
- [Kaggle Coursera Course Data](https://www.kaggle.com/datasets/tianyimasf/coursera-course-dataset)
- [Job Listings from GotFriends](https://www.gotfriends.co.il/)

