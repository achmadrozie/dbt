{%- set payment_methods = ['bank_transfer','coupon','credit_card','gift_card'] %}

with payments as (
    select 
        *
    from {{ ref('stg_stripe__payments' ) }}
    where 1=1
        and status = 'success'
)
, pivoted as (
    select
        order_id
        {% for payment in payment_methods %}
            , sum(case when payment_method = '{{ payment }}' then amount else 0 end) as {{ payment }}_amount
        {% endfor %}
    from payments
    group by 1
)
select * from pivoted