{{ config(
    materialized='table',
    schema='staging',
    tags=['staging']
) }}

WITH orders AS (
    SELECT
        ID AS ORDER_ID,
        USER_ID AS CUSTOMER_ID,
        ORDER_DATE,
        STATUS,
        _ETL_LOADED_AT,
        CURRENT_TIMESTAMP() AS _DBT_LOADED_AT
    FROM {{ source('raw', 'orders') }}
)

SELECT * FROM orders
