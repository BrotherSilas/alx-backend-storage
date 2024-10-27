#!/usr/bin/env python3
"""
Enhanced script that provides statistics about Nginx logs stored in MongoDB.
Includes top 10 IP addresses by frequency.
"""

from pymongo import MongoClient


def log_stats():
    """Prints the statistics of Nginx logs from the logs.nginx collection, including top IPs"""
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    nginx_collection = db.nginx

    # Total logs count
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Top 10 IPs
    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
