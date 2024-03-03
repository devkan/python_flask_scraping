# Python Web Scraping and Flask Web Service Project

This project demonstrates a simple implementation using Python with `playwright` and `BeautifulSoup4` for scraping a job site. The core functionality includes scraping data and saving it to a CSV file if no data exists. If data already exists, it retrieves the stored data to serve through a web service built with Flask, showcasing the data on a microsite.

## Overview

The goal of this project is to illustrate how to scrape data from a job site using Python libraries and then utilize Flask to create a micro web service that displays the scraped data. It's an excellent example of how to integrate web scraping and web service development into a single Python project.

## Technologies Used

- **Playwright**: A Python library for browser automation, used to scrape dynamic content from job sites.
- **BeautifulSoup4**: A Python library for parsing HTML and XML documents, used to extract data from the scraped pages.
- **Flask**: A micro web framework in Python, used to create a simple web service to display the scraped data.

## Project Structure

- `extractors/*.py`: The script that contains the scraping logic using Playwright and BeautifulSoup4.
- `flask_x.py`: The Flask application that serves the scraped data through a simple web interface.
- `requirements.txt`: A file listing all the necessary Python libraries to run the project.
- `save/`: A directory where the scraped save in CSV format is stored and accessed.

## Installation and Setup

To set up this project, follow these steps:

1. **Clone the repository**:
   ```
   git clone https://github.com/devkan/python_flask_scraping
   ```
2. **Install dependencies**:
   Navigate to the project directory and run:
   ```
   pip install -r requirements.txt
   ```
3. **Start the Flask app**:
   ```
   python flask_x.py
   ```
   This will start the Flask server, making the scraped data accessible through the microsite.

## Usage

Once the Flask server is running, you can access the microsite at `http://localhost:5000` (or the configured port) to view the data scraped from the job site. The web service dynamically displays the data from the CSV file, providing an interactive way to explore the scraped information.

## Conclusion

This project serves as a practical example of combining web scraping and web service development in Python. It showcases the powerful capabilities of Playwright and BeautifulSoup4 for scraping, alongside the simplicity and effectiveness of Flask for web service creation.
