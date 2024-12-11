import os
from flask import Flask, request, jsonify
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to extract internal links from a page
def get_internal_links(url, domain):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for anchor in soup.find_all('a', href=True):
            link = anchor['href']
            link = urljoin(url, link)  # Make the link absolute
            if urlparse(link).netloc == domain:  # Only internal links
                links.add(link)
        return list(links)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return []

# Function to crawl the domain and build a sitemap
def crawl_domain(start_url):
    domain = urlparse(start_url).netloc
    to_visit = [start_url]
    visited = set()
    sitemap = {}

    while to_visit:
        current_url = to_visit.pop()
        if current_url not in visited:
            visited.add(current_url)
            print(f"Crawling {current_url}")
            links = get_internal_links(current_url, domain)
            sitemap[current_url] = links
            to_visit.extend(links)  # Add new links to the queue

    return sitemap

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()
    start_url = data.get('url')
    if not start_url:
        return jsonify({'error': 'URL is required'}), 400

    sitemap = crawl_domain(start_url)
    return jsonify(sitemap)

if __name__ == '__main__':
    app.run(debug=True)
