{% for link in site.data.navigation.main %}
  <a href="./{{ link.url }}">{{ link.title }}</a>
{% endfor %}
