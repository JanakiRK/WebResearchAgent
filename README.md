
# WebResearchAgent

A Python-based web research assistant that searches the internet, extracts webpage content, generates summaries, and saves research findings in a Markdown report.

## Features

- Search the web using DuckDuckGo.
- Scrape webpage content using Requests and BeautifulSoup.
- Extract webpage titles and clean text.
- Generate simple extractive summaries.
- Combine search, scraping, and summarisation into one research workflow.
- Handle invalid inputs and webpage failures.
- Generate structured Markdown research reports.
- Automated tests using pytest.

## Technologies Used

- Python 3
- DDGS
- Requests
- BeautifulSoup4
- Pytest
- Python-dotenv

## Project Structure

```text
WebResearchAgent/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── search.py
│   ├── scraper.py
│   ├── summariser.py
│   ├── research_agent.py
│   └── report_generator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_search.py
│   ├── test_scraper.py
│   ├── test_summariser.py
│   └── test_research_agent.py
│
├── reports/
├── pytest.ini
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd WebResearchAgent
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the research agent from the project root:

```bash
python src/main.py
```

The application will:

1. Search the web for the configured research question.
2. Retrieve relevant webpages.
3. Extract and summarise webpage content.
4. Display research findings in the terminal.
5. Generate a Markdown research report.

## Generated Reports

Reports are saved in the `reports/` directory.

Default report:

```text
reports/research_report.md
```

## Running Tests

Run all automated tests:

```bash
python -m pytest -v
```

## Future Improvements

- AI-powered summarisation.
- User-provided research questions.
- Export reports to PDF.
- Improved search result filtering.
- Support for multiple report formats.

## Author

Developed as a Python learning project.
