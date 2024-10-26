# NoSQL Project

## Description
This project implements various MongoDB operations using both MongoDB shell commands and Python scripts. It covers basic database operations, document manipulation, and data analysis using MongoDB and the PyMongo driver.

## Technologies
- MongoDB 4.2
- Python 3.7
- PyMongo 3.10
- Ubuntu 18.04 LTS

## Requirements

### MongoDB
- All files interpreted on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All files should end with a new line
- First line of all files should be a comment
- A README.md file at the root of the folder is mandatory
- File length will be tested using `wc`

### Python Scripts
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7) and `PyMongo` (version 3.10)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/env python3`
- Code should use `pycodestyle` style (version 2.5.*)
- All modules and functions must be documented
- Code should not be executed when imported

## Files

### MongoDB Command Files
| File | Description |
|------|-------------|
| `0-list_databases` | Lists all MongoDB databases |
| `1-use_or_create_database` | Creates or uses the `my_db` database |
| `2-insert` | Inserts a document in the collection `school` |
| `3-all` | Lists all documents in the collection `school` |
| `4-match` | Lists documents with specific criteria |
| `5-count` | Displays the number of documents in the collection |
| `6-update` | Updates documents in the collection |
| `7-delete` | Deletes documents from the collection |

### Python Scripts
| File | Description |
|------|-------------|
| `8-all.py` | Lists all documents in a collection |
| `9-insert_school.py` | Inserts a new document in a collection |
| `10-update_topics.py` | Updates document topics by school name |
| `11-schools_by_topic.py` | Returns list of schools by topic |
| `12-log_stats.py` | Provides stats about Nginx logs |

## Usage

### MongoDB Commands
```bash
$ cat 0-list_databases | mongo
$ cat 1-use_or_create_database | mongo
# ... and so on for other MongoDB command files
```

### Python Scripts
```bash
$ ./8-all.py
$ ./9-insert_school.py
# ... and so on for other Python scripts
```

## Example Usage of Python Scripts

### List All Documents
```python
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school
schools = list_all(school_collection)
for school in schools:
    print(school)
```

### Insert School
```python
new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
print("New school created: {}".format(new_school_id))
```

## Log Stats Example Output
```bash
$ ./12-log_stats.py
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
```

## Author
- Silas Edet
-silasedetsnr@gmail.com

## License
This project is licensed under the terms of the ALX license.
