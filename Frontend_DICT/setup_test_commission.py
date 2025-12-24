from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
MONGO_URI = "mongodb+srv://admin:T2b_T.gTEv%40qmFB@cluster0.ytnahqm.mongodb.net/?appName=Cluster0"
DB_NAME = "dictator_ai_db"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    db = client[DB_NAME]
    users_collection = db["users"]
    
    print("=" * 50)
    print("COMMISSION TEST SETUP")
    print("=" * 50)
    
    username = "HighCommand"
    
    # Find user
    user = users_collection.find_one({"username": username})
    
    if not user:
        print(f"ERROR: User '{username}' not found!")
        exit()
    
    print(f"\nFound user: {username}")
    print(f"Current balance: ${user.get('affiliate_balance', 0)}")
    print(f"Commission start: {user.get('commission_start_date', 'Not set')}")
    
    # Update user
    print("\nSetting up test commission...")
    
    users_collection.update_one(
        {"username": username},
        {"$set": {
            "affiliate_balance": 15.50,
            "commission_start_date": datetime.utcnow().isoformat(),
            "payout_status": None
        }}
    )
    
    # Verify
    updated_user = users_collection.find_one({"username": username})
    
    print("\nSETUP COMPLETE!")
    print(f"Balance: ${updated_user.get('affiliate_balance')}")
    print(f"Commission start: {updated_user.get('commission_start_date')}")
    print(f"Payout status: {updated_user.get('payout_status', 'None')}")
    print("\nWith days=0, this should unlock IMMEDIATELY!")
    print("Refresh your Referral Modal now!")
    
except Exception as e:
    print(f"ERROR: {e}")
