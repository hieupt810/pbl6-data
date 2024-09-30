class Selector:
    PRODUCT_PICTURE = ".hugo4-pc-grid-item:has(.pic-wrapper):has(.subject):has(.price) > .hugo4-product > .pic-wrapper > .hugo4-product-picture > .picture-image"
    PRODUCT_SUBJECT = ".hugo4-pc-grid-item:has(.pic-wrapper):has(.subject):has(.price) > .hugo4-product > .hugo4-product-wrap-margin > .subject > span"
    PRODUCT_PRICE = ".hugo4-pc-grid-item:has(.pic-wrapper):has(.subject):has(.price) > .hugo4-product > .hugo4-product-wrap-margin > .hugo4-product-price-area > .price > div"
    PRODUCT_MIN_ORDER = ".hugo4-pc-grid-item:has(.pic-wrapper):has(.subject):has(.price) > .hugo4-product > .hugo4-product-wrap-margin > .moq > .moq-number"
    PRODUCT_URL = ".hugo4-pc-grid-item:has(.pic-wrapper):has(.subject):has(.price) > .hugo4-product"
