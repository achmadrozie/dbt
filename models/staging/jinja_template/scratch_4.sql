select 1 as dummy_col

{#
    {% set jennas_dictionary = {
    'word' : 'data',
    'part_of_speech' : 'noun',
    'defintion' : 'the building block of life'  
    } %}

    {{ jennas_dictionary['word']  }} is a 
            {{ jennas_dictionary['part_of_speech'] }} 
            that means {{ jennas_dictionary['definition'] }}
#}
