{{ config(
    materialized='table',
    schema='marts',
    tags=['marts', 'dimension']
) }}

WITH customers AS (
    SELECT
        CUSTOMER_ID,
        FIRST_NAME,
        LAST_NAME,
        FULL_NAME,
        _DBT_LOADED_AT
    FROM {{ ref('stg_customers') }}
)

SELECT * FROM customers
