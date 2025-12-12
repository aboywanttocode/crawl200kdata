# Tiki Product Fetcher

This project fetches product data from Tiki API and stores it into a PostgreSQL database.
It supports multi-threaded requests for faster data fetching and uses environment variables for database credentials.


## Installation

1. Clone this repository:
```bash
git clone https:://github.com/aboywanttocode/crawl200kdata
cd crawl200kdata
```

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

## Running the project

Run the main script:
```bash
python src/fetchThread.py
```


### (Project Structure)

# pro1/
# src/          # Python scripts
      db.py
      fetchThread.py
# data/         
    CSV/JSON data (ignored in Git)
# .env.example  
    Template for environment variables
# .gitignore


## Notes

- `.env` contains sensitive data and is **not included** in the repository.
- `data/` folder is ignored to avoid large files.
- Multi-threaded requests are used to fetch data faster.
