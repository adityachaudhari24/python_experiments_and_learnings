# key commands

### create env
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

### install dependencies 
pip install requests beautifulsoup4 openai

### freez requirements
pip freeze > requirements.txt

### run the file 
python ollama_localcall.py https://example.com

### make sure you have ollama installed locally 
[ollama.com](https://ollama.com) and install!

Once complete, the ollama server should already be running locally.  
If you visit:  
[http://localhost:11434/](http://localhost:11434/)


