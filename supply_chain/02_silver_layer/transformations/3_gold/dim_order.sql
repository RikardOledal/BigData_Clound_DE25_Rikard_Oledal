CREATE OR REFRESH MATERIALIZED VIEW supply_chain.3_gold.dim_order
COMMENT "Dim order deduplicated - gold layer" AS

SELECT
    order_id,
    MAX_BY(order_state, order_date) AS order_state
FROM 
    supply_chain.2_silver.supply_chain_obt
GROUP BY
    order_id
ORDER BY
    order_id;
