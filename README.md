📖 Introduction
This project focuses on learning how to use redis for basic operations and how to use redis as a simple cache

🛠️ Technologies Used
Python 3.7+
Redis server
redis-py (Python Redis client)
typing (for type annotations)

🚀 Getting Started
Prerequisites
# Install Redis Server in repository
sudo apt-get -y install redis-server

# install the Python package to work with Redis in Python
pip3 install redis

# Change Redis config file to restrict access to only the local machine
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

Project Structure
0x02-redis_basic/
│
├── exercise.py          # Main exercise file
├── web.py               # Web cache implementation
├── main.py              # Test case
└── README.md            # Project documentation

🎯 Learning Objectives
By the end of this project, you should be able to:
Learn how to use redis for basic operations
Learn how to use redis as a simple cache

📝 Tasks
0. Writing strings to Redis
Create a Cache class
Implement writing to Redis using a random key
Store input data in Redis
Track function calls using decorators

1. Reading from Redis and recovering original type
Implement methods to convert data back to desired format
Handle integer, string and bytes conversions
Create a system to track function calls

2. Incrementing values
Track how many times methods are called
Implement a counter system using Redis

3. Storing lists
Store lists in Redis
Implement parameterized caching
Handle complex data structures

4. Retrieving lists
Implement methods to retrieve lists from cache
Handle data type conversions for lists
Implement replay functionality

5. Implementing an expiring web cache and tracker
Implement a get_page function

💻 Usage Example
# Creating a cache instance
cache = Cache()

# Storing data
key = cache.store("hello")
print(cache.get(key))

# Using with decorator
@count_calls
@call_history
def store_user(user_id):
    return cache.store(f"user:{user_id}")

🔍 Testing
Run tests using:
python3 main.py

Additional Resources
Redis Official Documentation
Redis Python Client
Redis Command Reference

⚠️ Important Notes
Ensure Redis server is running before executing the code
Handle exceptions appropriately
Follow type annotations in Python code
Use decorators as specified in the tasks
Implement proper error handling

👥 Author/Email
Silas Edet/silasedtsnr@gmail.com

📄 License
This project is licensed under the ALX Africa License
