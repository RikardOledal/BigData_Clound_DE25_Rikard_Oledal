CREATE OR REFRESH MATERIALIZED VIEW supply_chain.3_gold.dim_date
COMMENT "Dim date deduplicated - gold layer" AS

SELECT
    date_format(order_date, 'yyyyMMddHHmm')::bigint AS order_datetime_id,
    MAX_BY(product_name, order_date) AS product_name,
    MAX_BY(product_price, order_date) AS product_price,
    order_date
FROM
    supply_chain.2_silver.supply_chain_obt
GROUP BY
    product_id
ORDER BY
    product_id;

Table dim_date {
  datetime_id integer [primary key]
  datetime timestamp
  year integer
  month integer
  weekday string
  hour integer
  minute integer
}