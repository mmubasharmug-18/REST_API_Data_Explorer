import json
from pathlib import Path

from api_client import APIClient


API_URL = "https://jsonplaceholder.typicode.com"

client = APIClient(API_URL)

users = client.get("/users")


if users:

    selected_users = []

    for user in users:
        selected_users.append({
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"]
        })

    print("\n===== REST API DATA EXPLORER =====\n")

    for user in selected_users:
        print(f"ID       : {user['id']}")
        print(f"Name     : {user['name']}")
        print(f"Username : {user['username']}")
        print(f"Email    : {user['email']}")
        print(f"City     : {user['city']}")
        print(f"Company  : {user['company']}")
        print("-" * 40)

    output_file = Path("data/users.json")

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(selected_users, file, indent=4)

    print(f"\nSaved {len(selected_users)} users to {output_file}")