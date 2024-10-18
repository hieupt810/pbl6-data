import psycopg

from utils.driver import Driver
from utils.environment import Environment
from utils.load_json import load_json


def crawl_products(website: str, MAX_LENGTH: int = 500):
    driver = Driver()
    try:
        data = load_json(website)
        with psycopg.connect(Environment.DATABASE_URL) as conn:
            with conn.cursor() as cur:

                for link in data["categories"]:
                    driver.open_new_tab(link)

                    titles = driver.find_by_css_selector(data["title"])
                    images = driver.find_by_css_selector(data["image"])
                    prices = driver.find_by_css_selector(data["price"])
                    hrefs = driver.find_by_css_selector(data["href"])
                    min_orders = driver.find_by_css_selector(data["min_order"])
                    assert (
                        len(titles)
                        == len(images)
                        == len(prices)
                        == len(hrefs)
                        == len(min_orders)
                    )
                    for i in range(MAX_LENGTH):
                        cur.execute(
                            "INSERT INTO products (title, image, price, min_order, href) VALUES (%s, %s, %s, %s, %s)",
                            (
                                titles[i].text,
                                images[i].get_attribute("src"),
                                prices[i].text,
                                hrefs[i].get_attribute("href"),
                                min_orders[i].text,
                            ),
                        )
                        conn.commit()

                    driver.close_current_tab()

        print(f"Crawled {website} successfully.")
    finally:
        driver.close()
