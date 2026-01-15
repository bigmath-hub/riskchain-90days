import requests
import json
import sys
import os

NODE_URL = os.getenv("RPC_URL", "https://eth.llamarpc.com")

block_arg = sys.argv[1] if len(sys.argv) > 1 else "latest"

payload = {
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": [block_arg, False], 
    "id": 1
}

headers = {"Content-Type": "application/json"}

response = requests.post(NODE_URL, headers=headers, data=json.dumps(payload))
if response.status_code == 200:
    block_data = response.json().get("result")
    if block_data is None:
        sys.exit(1)
        
    print(f"blockNumber: {block_data['number']}")
    print(f"blockHash: {block_data['hash']}")
    print(f"txCount: {len(block_data['transactions'])}")

    out_name = f"data/sample/block_{block_arg}.json"

    with open(out_name, 'w', encoding='utf-8') as f:
        json.dump(block_data, f, ensure_ascii=False, indent=4)

else:
    print(f"Error: {response.status_code}, {response.text}")
    sys.exit(1)


