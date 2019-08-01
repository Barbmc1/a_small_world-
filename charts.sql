/*Working manufacturers query*/
SELECT a_small_world_manufacturers.manufacturer_name, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_manufacturers
    ON a_small_world_manufacturers.id =a_small_world_products.manufacturer_id 
    GROUP BY a_small_world_manufacturers.manufacturer_name
	ORDER BY a_small_world_manufacturers.manufacturer_name

/*Working distributors query.*/
SELECT a_small_world_distributors.distributor_name, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_distributors
    ON a_small_world_products.distributors_id = a_small_world_distributors.id
    GROUP BY a_small_world_distributors.distributor_name
    ORDER BY a_small_world_distributors.distributor_name

/*Working for catagory_1 count.*/
SELECT a_small_world_catagories.catagory_1, COUNT(*)
    FROM a_small_world_products
    INNER JOIN a_small_world_catagories
    ON a_small_world_products.catagories_id = a_small_world_catagories.id
    GROUP BY a_small_world_catagories.catagory_1
    ORDER BY a_small_world_catagories.catagory_1




/*Query gets the catagory_1 for each product and counts each ocurance. */
CREATE VIEW cat_1 AS
    SELECT a_small_world_catagories.catagory_1, COUNT(*)
        FROM a_small_world_products
        INNER JOIN a_small_world_catagories
        ON a_small_world_products.catagories_id = a_small_world_catagories.id
        GROUP BY a_small_world_catagories.catagory_1

/*Query gets the sub_cat_1 for each product and counts each ocurance. */
CREATE VIEW sub_1 AS
    SELECT a_small_world_catagories.catagory_1, COUNT(*)
        FROM cat_1
        INNER JOIN a_small_world_catagories
        ON a_small_world_products.catagories_id = a_small_world_catagories.id
        GROUP BY a_small_world_catagories.catagory_1



/*Query gets the manufacturer for each products and tracks count for each manufacturer.*/
CREATE VIEW prod_manuf AS 
    SELECT a_small_world_manufacturers.manufacturer_name, COUNT(*)
        FROM a_small_world_products
        INNER JOIN a_small_world_manufacturers
        ON a_small_world_products.product_manufacturer_id = a_small_world_manufacturers.id
        GROUP BY a_small_world_manufacturers.manufacturer_name


/*Query gets the distributor for each products and tracks count for each distributor.*/
CREATE VIEW prod_dist AS 
    SELECT a_small_world_distributors.distributor_name, COUNT(*)
        FROM a_small_world_products
        INNER JOIN a_small_world_distributors
        ON a_small_world_products.distributor_id = a_small_world_distributors.id 
        GROUP BY a_small_world_distributors.distributor_name 


