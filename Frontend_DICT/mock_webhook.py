import requests
import json
import uuid
import sys

# Configuration
SERVER_URL = "http://127.0.0.1:5000/api/webhooks/btcpay"

def send_mock_webhook():
    print("--- BTCPay Mock Webhook Sender ---")
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        plan = sys.argv[2] if len(sys.argv) > 2 else "infantry"
        print(f"Using arguments: User={user_id}, Plan={plan}")
    else:
        user_id = input("Enter User ID to credit (e.g., u1): ").strip() or "u1"
        plan = input("Enter Plan (infantry/commander): ").strip().lower() or "infantry"
    
    coins = 100 if plan == 'infantry' else 300
    
    payload = {
        "id": "mock_event_" + str(uuid.uuid4()),
        "type": "InvoiceSettled",
        "invoiceId": "mock_invoice_" + str(uuid.uuid4()),
        "metadata": {
            "userId": user_id,
            "username": "mock_user",
            "plan": plan,
            "coins": coins,
            "referrer": None
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "BTCPay-Sig": "sha256=mock_signature_bypass" 
    }
    
    print(f"\nSending payload to {SERVER_URL}...")
    print(json.dumps(payload, indent=2))
    
    try:
        response = requests.post(SERVER_URL, json=payload, headers=headers)
        print(f"\nResponse Status: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            print("\n[OK] Webhook processed successfully! Check your user's coin balance.")
        else:
            print("\n[FAIL] Webhook failed.")
            
    except Exception as e:
        print(f"\n[ERROR] Connection Error: {e}")
        print("Make sure server.py is running on port 5000.")

if __name__ == "__main__":
    send_mock_webhook()
