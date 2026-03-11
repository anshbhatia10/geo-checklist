import json
import requests
from bs4 import BeautifulSoup
import sys

def validate_geo_schemas(url):
    print(f"--- Qlavo GEO Validator ---")
    print(f"Analyzing: {url}\n")
    
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'QlavoGEOValidator/1.0'})
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    json_ld_scripts = soup.find_all('script', type='application/ld+json')
    
    found_schemas = []
    for script in json_ld_scripts:
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                found_schemas.append(data.get('@type'))
            elif isinstance(data, list):
                for item in data:
                    found_schemas.append(item.get('@type'))
        except:
            continue

    required = ["Organization", "FAQPage", "WebSite"]
    
    print("Results:")
    for schema in required:
        status = "✅ FOUND" if schema in found_schemas else "❌ MISSING"
        print(f"- {schema}: {status}")
    
    print("\n--- Recommendation ---")
    if all(schema in found_schemas for schema in required):
        print("Excellent! Your site has the core citation building blocks for AI Search.")
    else:
        print("AI engines (ChatGPT, Claude, Perplexity) rely on these schemas for citation accuracy.")
        print("Visit qlavo.in/geo-resources to learn how to add the missing tags.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python geo-validator.py <url>")
    else:
        validate_geo_schemas(sys.argv[1])
