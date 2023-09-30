# Deepublish Store Web Scraper

This Python script allows you to scrape data from the Deepublish Store website (https://deepublishstore.com/). It uses the `requests`, `BeautifulSoup`, and `csv` libraries to extract information from the website's HTML content.

## Usage

1. Make sure you have the required Python libraries installed:

   - `requests`: To make HTTP requests.
   - `BeautifulSoup`: To parse HTML content.
   - `csv`: To handle CSV file operations.

   You can install these libraries using pip:

   ```bash
   pip install requests beautifulsoup4
   ```

2. Modify the `HOME` variable to specify the base URL of the Deepublish Store website if needed.

3. Run the script. It performs the following steps:

   - Fetches the HTML content of the Deepublish Store's homepage.
   - Extracts category URLs from the homepage.
   - Iterates through each category URL to scrape product data.

   The script is designed to extract data for products in the "Agama Islam" category. You can customize the category or page structure as needed.

## Output

The script does not provide a specific output format but is intended for data extraction purposes. You can extend the script to perform specific data extraction and save it to a CSV file, database, or any other storage format as needed.

## Disclaimer

Ensure that you comply with the website's terms of use and any legal or ethical considerations when scraping data from websites. It's essential to respect the website's policies and robots.txt file, if applicable, to avoid legal issues.
