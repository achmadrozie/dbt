{% for j in range(5) %}
    select {{ j }} as number{% if not loop.last %} union all{% endif %}
{% endfor %}

