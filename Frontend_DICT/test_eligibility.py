import requests

# Test the eligibility endpoint directly
API_BASE = "http://localhost:5000"

# First, login to get token
login_response = requests.post(
    f"{API_BASE}/api/login",
    json={"username": "admin", "password": "123"}
)

if login_response.status_code == 200:
    token = login_response.json()['token']
    print("Login successful!")
    print(f"Token: {token[:20]}...")
    
    # Now check eligibility
    print("\nChecking commission eligibility...")
    eligibility_response = requests.get(
        f"{API_BASE}/api/commission/eligibility",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    print(f"\nStatus Code: {eligibility_response.status_code}")
    print(f"Response: {eligibility_response.json()}")
    
    data = eligibility_response.json()
    print("\n" + "="*50)
    print("ELIGIBILITY CHECK RESULT:")
    print("="*50)
    print(f"Eligible: {data.get('eligible')}")
    print(f"Days Remaining: {data.get('days_remaining')}")
    print(f"Balance: ${data.get('affiliate_balance')}")
    print(f"Payout Status: {data.get('payout_status')}")
    print(f"Message: {data.get('message')}")
    print(f"Commission Start: {data.get('commission_start_date')}")
    
    if data.get('eligible'):
        print("\n✓ REDEEM BUTTON SHOULD BE ENABLED!")
    else:
        print("\n✗ REDEEM BUTTON WILL BE DISABLED")
        print(f"Reason: {data.get('message')}")
else:
    print(f"Login failed: {login_response.status_code}")
    print(login_response.text)
