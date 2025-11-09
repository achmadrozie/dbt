{{ config(
    materialized='table',
    schema='staging',
    tags=['staging']
) }}

WITH customers AS (
    SELECT
        ID AS CUSTOMER_ID,
        FIRST_NAME,
        LAST_NAME,
        FIRST_NAME || ' ' || LAST_NAME AS FULL_NAME,
        CURRENT_TIMESTAMP() AS _DBT_LOADED_AT
    FROM {{ source('raw', 'customers') }}
)

SELECT * FROM customers
