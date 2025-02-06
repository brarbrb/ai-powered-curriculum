import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FILE_SIZE_LIMIT_MB = 1000  # Maximum file size in MB 


def scrape_gotfriends_selenium(start_page, end_page, json_filename="job_listings.json"):
    """
    Scrapes pages from gotfriends.co.il using Selenium, parses the data, and writes them to JSON files.

    :param start_page: First page number to scrape (int)
    :param end_page: Last page number to scrape (int)
    :param json_filename: The base name of the JSON file to save the data
    """
    driver = webdriver.Chrome()
    all_job_listings = []  # Collect all job listings
    current_file_index = 1  # Start with the first file

    try:
        for page in range(start_page, end_page + 1):
            url = f'https://www.gotfriends.co.il/jobs/?page={page}&total=1739'
            print(f"Loading page {page}: {url}")
            driver.get(url)

            # Wait for the page to load/render
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "item"))
            )

            # Find each job block
            job_blocks = driver.find_elements(By.CLASS_NAME, "item")
            print(f"  Found {len(job_blocks)} job listings on page {page}")

            # Extract job details from each block
            for job_block in job_blocks:
                job_data = {
                    "job_title": "",
                    "job_description": "",
                    "job_requirements": ""
                }

                # Extract job title
                try:
                    title_element = job_block.find_element(By.CLASS_NAME, "title")
                    job_data["job_title"] = title_element.text.strip()
                except Exception as e:
                    print(f"Error extracting job title: {e}")

                # Extract job description and requirements
                try:
                    inner_block = job_block.find_element(By.CLASS_NAME, "inner")
                    job_data.update(parse_job_block(inner_block.text.strip()))
                except Exception as e:
                    print(f"Error extracting job details: {e}")

                # Validate and append job data
                if job_data["job_title"] or job_data["job_description"] or job_data["job_requirements"]:
                    all_job_listings.append(job_data)
                else:
                    print(f"Skipped empty job data on page {page}")

            # Save to JSON file after processing each page
            current_file_index = write_jobs_to_json(
                all_job_listings,
                base_filename=json_filename,
                current_file_index=current_file_index
            )
            all_job_listings.clear()  # Clear the list after saving

    finally:
        driver.quit()

    return current_file_index


def parse_job_block(block: str) -> dict:
    """
    Given a single job listing (block of text),
    return a dict with 'job_description' and 'job_requirements'.
    """
    job_data = {"job_description": "", "job_requirements": ""}
    lines = block.strip().splitlines()

    in_description = False
    in_requirements = False

    for line in lines:
        line = line.strip()

        if line.startswith("תיאור המשרה"):
            in_description = True
            in_requirements = False
            continue

        elif line.startswith("דרישות המשרה"):
            in_requirements = True
            in_description = False
            continue

        elif line.startswith("מס' משרה") or "שלחו קורות חיים" in line:
            # End of listing or next part
            in_description = False
            in_requirements = False
            continue

        if in_description:
            job_data["job_description"] += line + "\n"

        if in_requirements:
            job_data["job_requirements"] += line + "\n"

    return job_data


def write_jobs_to_json(new_job_listings, base_filename, current_file_index):
    """
    Appends new job listings to the JSON file. Creates a new file if the size exceeds the limit.
    """
    # Construct the current file name
    current_filename = f"{os.path.splitext(base_filename)[0]}_{current_file_index}.json"

    # Load existing data if the file exists
    if os.path.exists(current_filename):
        with open(current_filename, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    # Combine existing data with new data
    combined_data = existing_data + new_job_listings

    # Check file size after combining
    if len(json.dumps(combined_data).encode('utf-8')) > FILE_SIZE_LIMIT_MB * 1024 * 1024:
        # Create a new file if size exceeds the limit
        current_file_index += 1
        current_filename = f"{os.path.splitext(base_filename)[0]}_{current_file_index}.json"
        combined_data = new_job_listings  # Start the new file with the new data

    # Write the combined data back to the file
    with open(current_filename, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(new_job_listings)} jobs to {current_filename}")
    return current_file_index


if __name__ == "__main__":
    scrape_gotfriends_selenium(start_page=1, end_page=1740, json_filename="job_listings.json")
