{% if summary is defined %}
**summary**
{% endif %}
{% if thumbnail is not defined %}
{% if link is defined %}
##[{{ title }}]({{ link }})
{% else %}
##{{ title }}
{% endif %}
{% else %}
{% if link is defined %}
| | 
|-:|:-
| ![{{ thumbnail }}]({{ thumbnail }}) | <h3>[{{ title }}]({{ link }})</h3>
{% else %}
| | 
|-:|:-
| ![{{ thumbnail }}]({{ thumbnail }}) | <h3>{{ title }}</h3>
{% endif %}
{% endif %}
{% if image is defined %}
| | 
|-:|:-
| ![{{ image }}]({{ image }}) | {{ body }}
{% else %}
{{ body }}
{% endif %}
