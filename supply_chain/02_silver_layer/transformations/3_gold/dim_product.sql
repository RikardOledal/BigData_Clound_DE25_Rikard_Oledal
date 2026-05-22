CREATE OR REFRESH MATERIALIZED VIEW supply_chain.3_gold.dim_product
COMMENT "Dim products deduplicated - gold layer" AS

SELECT
    product_card_id AS product_id,
    MAX_BY(product_name, order_date) AS product_name,
    MAX_BY(product_price, order_date) AS product_price
FROM
    supply_chain.2_silver.supply_chain_obt
GROUP BY
    product_id
ORDER BY
    product_id;