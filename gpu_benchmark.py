import time
import requests
import json

# The local Ollama API endpoint
url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2:latest",
    "prompt": "Write a highly detailed, 500-word sci-fi story about a robot waking up on Mars.",
    "stream": True
}

print("Initiating Inference. Watch your GPU telemetry...\n")

start_time = time.time()
token_count = 0

# Send the request and stream the response
response = requests.post(url, json=payload, stream=True)

for line in response.iter_lines():
    if line:
        data = json.loads(line)
        # Print the text as it generates
        print(data.get("response", ""), end="", flush=True)
        token_count += 1
        
        if data.get("done"):
            break

end_time = time.time()
total_time = end_time - start_time
tps = token_count / total_time

print("\n\n" + "="*40)
print(f"Total Tokens Generated: {token_count}")
print(f"Total Time: {total_time:.2f} seconds")
print(f"Hardware Throughput: {tps:.2f} Tokens Per Second (TPS)")
print("="*40)
