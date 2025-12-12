# Tiki Product Fetcher

This project fetches product data from the Tiki API and stores it into a PostgreSQL database.  
It supports multi-threaded requests for faster fetching and uses environment variables to safely store database credentials.

---

## Features

- Fetch product details (id, name, price) from Tiki API.
- Multi-threaded requests to speed up data fetching.
- Save fetched products to PostgreSQL.
- Secure database credentials using `.env`.

---

## Project Structure
#### pro1/
#### ├─ src/ # Python scripts
#### │ ├─ db.py # PostgreSQL insert logic
#### │ └─ fetchThread.py # API fetching and multi-thread logic
#### ├─ data/ # CSV/JSON data (ignored in GitHub)
#### ├─ .env.example # Template for environment variables
#### ├─ .gitignore
#### ├─ README.md

---

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Required Python packages:

```bash
pip install requests psycopg2-binary python-dotenv
```
# Set Up
### 1. Clone this repository:
     git clone https://github.com/aboywanttocode/crawl200kdata.git
     cd tiki-fetcher
###  Create and activate a virtual environment (optional but recommended):
# Windows
python -m venv venv
venv\Scripts\activate

# Running the Project
### 1. Fetch product data from Tiki API
``` python src/fetchThread.py ```
- This script reads product IDs from data/products-0-200000.csv.

- Fetches product details (id, name, price) using multi-threading.

- Saves results to data/products_100.json (or more depending on your CSV).
### 2. Insert products into PostgreSQL
```python src/db.py ```
- Reads JSON file data/products_100.json.
- Inserts products into the products table.
- Uses .env for database credentials to stay secure.

# 4.Fill in your PostgreSQL credentials in .env:
```
DB_HOST=localhost
DB_NAME=postgresss
DB_USER=postgres
DB_PASSWORD=yourpassword
```
# 5. Environment Variables
- .env contains sensitive database credentials and should not be committed.
- .env.example is a template showing which variables are required.
- Make sure to keep .env private.

# Notes
- Multi-threading (ThreadPoolExecutor) is used to speed up API requests.
- The data/ folder is ignored in GitHub because it may contain large CSV/JSON files.
- Only src/ and .env.example are committed to the repository.
- ON CONFLICT (id) DO NOTHING is used in PostgreSQL insert to avoid duplicates.
