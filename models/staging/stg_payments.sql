{{ config(
    materialized='table',
    schema='staging',
    tags=['staging']
) }}

WITH payments AS (
    SELECT
        ID AS PAYMENT_ID,
        ORDERID AS ORDER_ID,
        PAYMENTMETHOD AS PAYMENT_METHOD,
        STATUS,
        AMOUNT,
        CREATED AS PAYMENT_DATE,
        _BATCHED_AT,
        CURRENT_TIMESTAMP() AS _DBT_LOADED_AT
    FROM {{ source('stripe', 'payment') }}
)

SELECT * FROM payments
