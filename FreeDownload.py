import requests
import sys
import os
from urllib.parse import urlparse

def download_page(url):
    """Download the HTML content of the given URL and save as .html."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        response.raise_for_status()
        
        # Determine encoding from headers or fallback to utf-8
        encoding = response.encoding if response.encoding else 'utf-8'
        html_content = response.text
        
        # Generate filename from URL
        parsed = urlparse(url)
        netloc = parsed.netloc.replace('www.', '')
        path = parsed.path.strip('/').replace('/', '_') or 'index'
        if not path:
            path = 'index'
        filename = f"{netloc}_{path}.html"
        # Remove unsafe characters
        filename = ''.join(c for c in filename if c.isalnum() or c in '._-')
        
        # Save file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"[+] Page saved as: {filename}")
        print(f"[+] Size: {len(html_content)} characters")
        return True
    except requests.exceptions.RequestException as e:
        print(f"[-] Error downloading page: {e}")
        return False

def main():
    print("="*60)
    print("   WEB PAGE DOWNLOADER - Save HTML")
    print("="*60)
    url = input("Enter URL (e.g., https://example.com): ").strip()
    if not url:
        print("[-] No URL provided.")
        sys.exit(1)
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    print(f"[+] Downloading: {url}")
    download_page(url)

if __name__ == "__main__":
    main()