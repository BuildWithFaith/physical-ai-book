
import requests
import sys

def test_connection():
    url = "http://localhost:8002"
    print(f"Testing connection to {url}...")
    
    # Test Root Endpoint
    try:
        response = requests.get(f"{url}/")
        print(f"Root endpoint status: {response.status_code}")
        print(f"Root endpoint response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to the server at root endpoint.")
        sys.exit(1)

    # Test Chat Endpoint
    chat_url = f"{url}/chat"
    payload = {
        "query": "What is Python?",
        "top_k": 1
    }
    
    print(f"\nTesting chat endpoint at {chat_url}...")
    try:
        response = requests.post(chat_url, json=payload)
        print(f"Chat endpoint status: {response.status_code}")
        if response.status_code == 200:
            print(f"Chat endpoint response: {response.json()}")
        else:
            print(f"Chat endpoint error response: {response.text}")
    except Exception as e:
        print(f"ERROR: Failed to connect to chat endpoint: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_connection()
