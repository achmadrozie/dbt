{{ config(
    materialized='table',
    schema='marts',
    tags=['marts', 'fact']
) }}

WITH orders AS (
    SELECT
        o.ORDER_ID,
        o.CUSTOMER_ID,
        o.ORDER_DATE,
        o.STATUS,
        COUNT(p.PAYMENT_ID) AS PAYMENT_COUNT,
        COALESCE(SUM(p.AMOUNT), 0) AS TOTAL_AMOUNT,
        c.FULL_NAME AS CUSTOMER_NAME,
        o._DBT_LOADED_AT
    FROM {{ ref('stg_orders') }} o
    LEFT JOIN {{ ref('stg_payments') }} p
        ON o.ORDER_ID = p.ORDER_ID
    LEFT JOIN {{ ref('stg_customers') }} c
        ON o.CUSTOMER_ID = c.CUSTOMER_ID
    GROUP BY
        o.ORDER_ID,
        o.CUSTOMER_ID,
        o.ORDER_DATE,
        o.STATUS,
        c.FULL_NAME,
        o._DBT_LOADED_AT
)

SELECT * FROM orders
