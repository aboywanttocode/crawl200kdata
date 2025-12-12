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
pro1/
├─ src/ # Python scripts
│ ├─ db.py # PostgreSQL insert logic
│ └─ fetchThread.py # API fetching and multi-thread logic
├─ data/ # CSV/JSON data (ignored in GitHub)
├─ .env.example # Template for environment variables
├─ .gitignore
├─ README.md

---

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Required Python packages:

```bash
pip install requests psycopg2-binary python-dotenv
```
# Set Up
1. Clone this repository:
git clone https://github.com/username/tiki-fetcher.git
cd tiki-fetcher
2.Create and activate a virtual environment (optional but recommended):
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
3.Create .env file from template:
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
4.Fill in your PostgreSQL credentials in .env:
DB_HOST=localhost
DB_NAME=postgresss
DB_USER=postgres
DB_PASSWORD=yourpassword
