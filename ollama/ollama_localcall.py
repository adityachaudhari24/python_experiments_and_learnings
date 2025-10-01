# write ollama local call to summarize the website content, I have installed ollama locally

import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import sys

def get_website_content(url):
    """Fetch and extract text content from a website."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text[:8000]  # Limit to first 8000 characters
        
    except Exception as e:
        print(f"Error fetching website content: {e}")
        return None

def summarize_with_ollama(content, model="deepseek-r1:8b"):
    """Use Ollama to summarize the content using OpenAI-compatible API."""
    try:
        # Initialize OpenAI client pointing to Ollama
        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"  # Ollama doesn't require a real API key
        )
        
        # Create chat completion
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides concise and informative summaries of web content."
                },
                {
                    "role": "user",
                    "content": f"Please provide a comprehensive summary of the following website content:\n\n{content}"
                }
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return None

def main():
    """Main function to handle URL input and summarization."""
    if len(sys.argv) != 2:
        print("Usage: python ollama_localcall.py <URL>")
        print("Example: python ollama_localcall.py https://example.com")
        return
    
    url = sys.argv[1]
    
    print(f"Fetching content from: {url}")
    content = get_website_content(url)
    
    if not content:
        print("Failed to fetch website content.")
        return
    
    print(f"Content length: {len(content)} characters")
    print("Generating summary...")
    
    summary = summarize_with_ollama(content)
    
    if summary:
        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50)
        print(summary)
    else:
        print("Failed to generate summary.")

if __name__ == "__main__":
    main()