CREATE TABLESPACE products_tablespace
    ADD DATAFILE '/samsung_ecom/products.ibd'
    FILE_BLOCK_SIZE=16384
    ENGINE=InnoDB;
