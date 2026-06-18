-- ==========================================
-- STORED PROCEDURE
-- Calculate Daily Sales For Store
-- ==========================================

USE retail_sales_db;

DELIMITER //

CREATE PROCEDURE CalculateDailySales(
    IN storeid INT
)
BEGIN

    SELECT
        store_id,
        sale_date,
        SUM(total_amount) AS daily_sales

    FROM sales

    WHERE store_id = storeid

    GROUP BY
        store_id,
        sale_date;

END //

DELIMITER ;

-- ==========================================
-- EXECUTE PROCEDURE
-- ==========================================

CALL CalculateDailySales(1);
