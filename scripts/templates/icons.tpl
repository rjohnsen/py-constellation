class Icons:
    """
    Notes:
        1. Constellation App icons starting with digit is prefixed with 'NS' when
           naming constants. 'NS' is unique to our Python library and stands for 
           'Not Specified'.
    """
{%- for icon in constants %}
    {{icon['name']}} = "{{icon['value']}}" 
{%- endfor %}

