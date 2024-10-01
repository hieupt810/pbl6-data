import psycopg

from constants import LINK, MAX_LENGTH
from constants.selector import Selector
from utils.driver import Driver
from utils.environment import Environment

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                image TEXT,
                price TEXT,
                min_order TEXT,
                url TEXT
            )
        """)
    conn.commit()

if __name__ == "__main__":
    driver = Driver()

    try:
        with psycopg.connect(Environment.DATABASE_URL) as conn:

            create_table(conn)

            with conn.cursor() as cur:
                for link in LINK:
                    driver.open_new_tab(link)

                    pictures = driver.find_elements_by_css_selector(
                        Selector.PRODUCT_PICTURE
                    )
                    subjects = driver.find_elements_by_css_selector(
                        Selector.PRODUCT_SUBJECT
                    )
                    prices = driver.find_elements_by_css_selector(
                        Selector.PRODUCT_PRICE
                    )
                    min_order = driver.find_elements_by_css_selector(
                        Selector.PRODUCT_MIN_ORDER
                    )
                    urls = driver.find_elements_by_css_selector(
                        Selector.PRODUCT_URL
                    )

                    assert len(pictures) == len(subjects) == len(prices) == len(min_order) == len(urls)
                    for i in range(MAX_LENGTH):
                        cur.execute(
                            "INSERT INTO products (name, image, price, min_order, url) VALUES (%s, %s, %s, %s, %s)",
                            (
                                subjects[i].text,
                                pictures[i].get_attribute("src"),
                                prices[i].text,
                                min_order[i].text,
                                urls[i].get_attribute("href")
                            ),
                        )
                        conn.commit()
                        print(f"Inserted data {i + 1}/{MAX_LENGTH}")

                    driver.close_current_tab()
    finally:
        driver.close()
