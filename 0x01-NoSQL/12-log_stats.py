#!/usr/bin/env python3
"""
A script that provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def log_stats():
    """Prints the statistics of Nginx logs from the logs.nginx collection"""
    # Connect to the MongoDB server
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    nginx_collection = db.nginx

    # Total count of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods counts
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET method with /status path
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()

