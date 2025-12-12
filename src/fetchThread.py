import csv
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time 
# ====== SETTINGS ======
PRODUCT_ID_FILE = "pro1/data/products-0-200000.csv"
OUTPUT_FILE = "pro1/data/products_100.json"
API_URL = "https://api.tiki.vn/product-detail/api/v1/products/{}"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


# LOAD PRODUCT IDS FROM CSV 
def load_ids(file_path):
    ids = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row and row[0].isdigit():
                ids.append(int(row[0]))
            if len(ids) >= 1000:
                break
    return ids


# FETCH ONE PRODUCT
def fetch_product(pid):
    try:
        r = requests.get(API_URL.format(pid), headers=HEADERS, timeout=5)

        if r.status_code == 200:
            data = r.json()

            if "id" not in data:
                print(f" Invalid response for ID {pid}")
                return None

            return {
                "id": data.get("id"),
                "name": data.get("name"),
                "price": data.get("price")
            }

        print(f"HTTP {r.status_code} for ID {pid}")
        return None

    except Exception as e:
        print(f"Exception for ID {pid}: {e}")
        return None


# FETCH USING THREADS 
def fetch_products_threaded(ids, max_workers=50):
    results = []

    print(f"\nStarting threaded fetch with {max_workers} threads...\n")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_product, pid): pid for pid in ids}

        for future in as_completed(futures):
            pid = futures[future]
            res = future.result()
            if res:
                results.append(res)

    print(f"\nThreaded fetch complete. Success: {len(results)}/{len(ids)}")
    return results


# deploy 
def main():
    start = time.time()
    ids = load_ids(PRODUCT_ID_FILE)
    print(f"Loaded {len(ids)} product IDs")

    results = fetch_products_threaded(ids, max_workers=50)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    end = time.time()
    print(f"\nTime taken: {end - start:.2f} seconds")
    print("\nDONE")
    print(f"Saved {len(results)} products → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
