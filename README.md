# PaperSnatcher
# Research Paper Fetcher

## Overview
This Python program fetches research papers from PubMed based on a user-specified query. It filters the results to include only papers where at least one author is affiliated with a pharmaceutical or biotech company and saves the filtered data as a CSV file.

## Features
- Fetches papers using the PubMed API
- Supports full PubMed query syntax
- Filters papers based on company affiliations
- Saves results as a CSV file with relevant details
- Command-line interface with various options

## Installation
This project uses **Poetry** for dependency management.

### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/research-paper-fetcher.git
   cd research-paper-fetcher
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Activate the virtual environment:
   ```sh
   poetry shell
   ```

## Usage
The program is executed as a command-line script with the following options:

```sh
python fetchpaper.py -q "your search query" -f output.csv
```

### Command-Line Arguments
| Option  | Description |
|---------|-------------|
| `-h` or `--help` | Display usage instructions |
| `-d` or `--debug` | Enable debug mode to print additional logs |
| `-f` or `--file` | Specify the output filename (default: console output) |

## Output Format
The script generates a CSV file with the following columns:

| PubMedID | Title | Publication Date | Non-academic Authors | Company Affiliation(s) | Corresponding Author Email |
|----------|-------|------------------|-----------------------|----------------------|---------------------------|
| 40080018 | Sample Title | 2024-01-10 | John Doe | Biotech Ltd | john.doe@biotech.com |

## Code Structure
- `fetchpaper.py`: Main script that fetches and processes research papers.
- `utils.py`: Contains helper functions for API requests and filtering.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation file.

## Development
To contribute or modify the project:
1. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
2. Make your changes and commit them:
   ```sh
   git commit -m "Add new feature"
   ```
3. Push to GitHub and create a pull request:
   ```sh
   git push origin feature-branch
   ```

## Tools & Technologies Used
- **Python 3.8+**
- **Requests** for API calls
- **CSV** for file handling
- **Poetry** for dependency management

## License
This project is licensed under the MIT License.

---
Feel free to modify and update as needed!

