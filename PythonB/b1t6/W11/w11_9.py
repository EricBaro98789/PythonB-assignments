import json

users = [
    {"name": "Alice", "age": 30, "location": "London", "balance": 1000},
    {"name": "Bob", "age": 22, "location": "New York", "balance": 500},
    {"name": "Charlie", "age": 35, "location": "Paris", "balance": 3000},
    {"name": "Dana", "age": 28, "location": "Berlin", "balance": 800},
]

age_limit = 25
rich_limit = 2000
user_from_location = False
extra_variable = 0

# Check age
for user in users:
    if user["age"] > age_limit:
        print(f'{user["name"]} is over {age_limit} years old.')

# Check location
location = "Paris"
for user in users:
    if user["location"] == location:
        user_from_location = True
        break

if user_from_location == True:
    print(f'There is at least one user from {location}.')

# Count rich users
rich_users_count = 0
for user in users:
    if user["balance"] > rich_limit:
        rich_users_count += 1

print(f'There are {rich_users_count} users with a balance over {rich_limit}.')
