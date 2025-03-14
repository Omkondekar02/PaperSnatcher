import requests
import csv

# Define the PubMed API URLs
PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Add your PubMed API key here
API_KEY = "YOUR_API_KEY_HERE"

def fetch_paper_ids(query: str, max_results: int = 10):
    """Fetches PubMed paper IDs based on the query."""
    print("🔍 Fetching paper IDs from PubMed API...")

    params = {
        'db': 'pubmed',
        'term': query,
        'retmax': max_results,
        'retmode': 'xml',
        'api_key':  '3a94d29441a719bb957e02dc45da04648808' # Use API Key
    }
    response = requests.get(PUBMED_API_URL, params=params)

    print(f"📝 API Response Code: {response.status_code}")
    print(f"📜 API Response (First 500 chars): {response.text[:500]}")  # Show part of response

    if response.status_code == 200:
        paper_ids = response.text.split('<Id>')[1:]  # Extract IDs from XML
        paper_ids = [id.split('</Id>')[0] for id in paper_ids]
        print(f"✅ Fetched {len(paper_ids)} paper IDs: {paper_ids}")
        return paper_ids
    else:
        print("❌ Error fetching paper IDs. Check your API key and internet connection.")
        return []

import requests
import xml.etree.ElementTree as ET

EFETCH_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_paper_details(paper_id: str):
    """Fetches actual title, authors, source, and year from PubMed API."""
    print(f"🔍 Fetching details for paper ID: {paper_id}")

    params = {
        'db': 'pubmed',
        'id': paper_id,
        'retmode': 'xml'
    }
    response = requests.get(EFETCH_API_URL, params=params)

    if response.status_code != 200:
        print(f"❌ Error fetching details for {paper_id}")
        return {}

    # Parse XML response
    root = ET.fromstring(response.text)

    # Extract title
    title_elem = root.find(".//ArticleTitle")
    title = title_elem.text if title_elem is not None else "Unknown Title"

    # Extract authors
    authors_list = []
    for author in root.findall(".//Author"):
        last_name = author.find("LastName")
        first_name = author.find("ForeName")
        if last_name is not None and first_name is not None:
            authors_list.append(f"{first_name.text} {last_name.text}")
    authors = ", ".join(authors_list) if authors_list else "Unknown Authors"

    # Extract source (journal)
    source_elem = root.find(".//Journal/Title")
    source = source_elem.text if source_elem is not None else "Unknown Source"

    # Extract year
    year_elem = root.find(".//PubDate/Year")
    year = year_elem.text if year_elem is not None else "Unknown Year"

    paper_data = {
        'PubMedID': paper_id,
        'Title': title,
        'Authors': authors,
        'Source': source,
        'Year': year,
    }

    print(f"✅ Data fetched for {paper_id}: {paper_data}")
    return paper_data

def save_to_csv(data, filename="papers.csv"):
    """Save the fetched data to a CSV file."""
    print(f"📁 Attempting to save {len(data)} papers to {filename}...")

    if not data:
        print("⚠️ No data to save!")
        return

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['PubMedID', 'Title', 'Authors', 'Source', 'Year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            print(f"📌 Writing row: {row}")
            writer.writerow(row)

    print(f"✅ CSV file '{filename}' saved successfully!")

def main():
    print("🚀 Running main function...")
    query = "pharmaceutical research"
    
    paper_ids = fetch_paper_ids(query)
    if not paper_ids:
        print("⚠️ No paper IDs found. Stopping program.")
        return

    papers_data = []
    for paper_id in paper_ids:
        details = fetch_paper_details(paper_id)
        if details:
            papers_data.append(details)

    if not papers_data:
        print("⚠️ No papers to save! Something is wrong with fetch_paper_details.")
        return

    save_to_csv(papers_data)

if __name__ == "__main__":
    main()
