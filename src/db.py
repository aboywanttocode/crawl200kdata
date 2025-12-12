import json
import psycopg2
from psycopg2.extras import execute_batch

JSON_FILE = "pro1\data\products_100.json"

# ====== INSERT FUNCTION ======
def insert_products(json_file, conn):
    with open(json_file, "r", encoding="utf-8") as f:
        products = json.load(f)

    rows = []
    for p in products:
        rows.append((
            p.get("id"),
            p.get("name"),
            p.get("price")
        ))

    sql = """
        INSERT INTO products (id, name, price)
        VALUES (%s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """

    with conn.cursor() as cur:
        execute_batch(cur, sql, rows, page_size=50)

    conn.commit()
    print(f"Inserted {len(rows)} products into PostgreSQL")


# ====== MAIN ======
def main():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    insert_products(JSON_FILE, conn)
    conn.close()


if __name__ == "__main__":
    main()
