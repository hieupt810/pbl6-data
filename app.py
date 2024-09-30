import psycopg

from constants import LINK, MAX_LENGTH
from constants.selector import Selector
from utils.driver import Driver
from utils.environment import Environment

if __name__ == "__main__":
    driver = Driver()

    try:
        with psycopg.connect(Environment.DATABASE_URL) as conn:
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

                    assert len(pictures) == len(subjects) == len(prices)
                    for i in range(MAX_LENGTH):
                        cur.execute(
                            "INSERT INTO products (name, image, price) VALUES (%s, %s, %s)",
                            (
                                subjects[i].text,
                                pictures[i].get_attribute("src"),
                                prices[i].text,
                            ),
                        )
                        conn.commit()
                        print(f"Inserted data {i + 1}/{MAX_LENGTH}")

                    driver.close_current_tab()
    finally:
        driver.close()
