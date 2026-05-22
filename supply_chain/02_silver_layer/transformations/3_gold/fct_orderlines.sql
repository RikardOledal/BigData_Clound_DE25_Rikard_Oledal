CREATE OR REFRESH STREAMING TABLE supply_chain.3_gold.fct_orderlines
    COMMENT "Fact table - gold layer" AS
SELECT
    order_item_id,
    order_id,
    customer_id,
    product_card_id AS product_id,
    date_format(order_date, 'yyyyMMddHHmm')::bigint AS order_datetime_id,
    order_item_product_price_dec AS order_item_price,
    order_item_quantity AS quantity,
    order_item_discount_rate AS discount_rate,
    order_item_price*quantity*(1-discount_rate) AS total_amount
FROM STREAM supply_chain.2_silver.supply_chain_obt;