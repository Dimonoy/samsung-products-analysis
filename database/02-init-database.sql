CREATE DATABASE IF NOT EXISTS samsung_ecom;
ALTER DATABASE samsung_ecom CHARACTER SET euckr;
USE samsung_ecom;
   
# Overall storage for a single record: 894 bytes
CREATE TABLE IF NOT EXISTS products(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    model VARCHAR(15) NOT NULL,
    model_code VARCHAR(15) NOT NULL,
    link VARCHAR(255) NOT NULL,
    item_category VARCHAR(31) NOT NULL,
    item_classification_number VARCHAR(15) NOT NULL,
    standard_price INT UNSIGNED,
    member_price INT UNSIGNED,
    benefit_price INT UNSIGNED,
    coupon_discount INT UNSIGNED,
    outlet_special_price INT UNSIGNED,
    rating FLOAT NOT NULL,
    quantity_of_reviews MEDIUMINT UNSIGNED NOT NULL,
    stock_quantity MEDIUMINT UNSIGNED NOT NULL,
    additional_properties JSON,
    date_time_collected TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB, CHARACTER SET euckr, ROW_FORMAT=COMPACT, TABLESPACE products_tablespace;
