# Get Papers List

This Python program fetches research papers from PubMed based on a user query. It filters the papers based on whether at least one author is affiliated with a pharmaceutical or biotech company, and returns the results in a CSV file.

## Features

- Fetch research papers from PubMed API.
- Filter results to identify authors affiliated with pharmaceutical or biotech companies.
- Output the filtered results to a CSV file with the following columns:
  - PubmedID: Unique identifier for the paper.
  - Title: Title of the paper.
  - Publication Date: Date the paper was published.
  - Non-academic Author(s): Names of authors affiliated with non-academic institutions.
  - Company Affiliation(s): Names of pharmaceutical/biotech companies.
  - Corresponding Author Email: Email address of the corresponding author.

## Requirements

- Python 3.13 or higher
- Poetry (for dependency management)
- Dependencies will be automatically installed via `poetry install`.

## Setup Instructions

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/get-papers-list.git
   cd get-papers-list
