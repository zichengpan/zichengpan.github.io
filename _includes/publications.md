<h2 style="margin: 30px 0px 15px;">Featured Publications</h2>

<p style="margin: 15px 0px 15px; font-size: 16px; color: #595959 !important; font-weight: bold;">For a full list, please refer to my <a href="https://scholar.google.com/citations?user=GsURDp0AAAAJ" target="_blank">Google Scholar</a> and <a href="https://orcid.org/0000-0001-5890-0165" target="_blank">ORCID</a>.</p>

<p style="margin: 15px 0px 30px; font-size: 16px; color: #595959 !important; font-weight: bold;">* Equal contribution</p>

<div class="publications-plain">

<h3 style="margin: 40px 0px 20px; font-size: 18px; color: #13294B; font-weight: 700;">Journal Publications</h3>

{% assign journal_counter = 1 %}
{% for link in site.data.publications.journals %}

<div style="margin-bottom: 25px; text-align: left;">
  <div style="display: flex; align-items: flex-start; margin-bottom: 5px;">
    <span style="font-weight: 600; margin-right: 8px; color: #666; min-width: 25px;">[J{{ journal_counter }}]</span>
    <div style="flex: 1;">
      <div class="title" style="font-weight: 600; margin-bottom: 5px; color: #595959 !important;">
        {% if link.pdf %}<a href="{{ link.pdf }}" target="_blank" style="color: #595959 !important; text-decoration: none;">{{ link.title }}</a>{% else %}{{ link.title }}{% endif %}
      </div>
      <div class="author" style="margin-bottom: 3px;">{{ link.authors }}</div>
      <div class="periodical" style="margin-bottom: 8px;">
        {% if link.q1_ranking %}
        <span class="badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; padding: 2px 8px;">{{ link.q1_ranking }}</span>
        {% endif %}
        {% if link.core_ranking %}
        <span class="badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 8px; font-size: 14px; padding: 2px 8px;">{{ link.core_ranking }}</span>
        {% endif %}
        <em>{{ link.conference }}</em>
      </div>
      <div class="links">
        {% if link.pdf %} 
        <a href="{{ link.pdf }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">PDF</a>
        {% endif %}
        {% if link.code %} 
        <a href="{{ link.code }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">Code</a>
        {% endif %}
        {% if link.page %} 
        <a href="{{ link.page }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">Project</a>
        {% endif %}
        {% if link.data %} 
        <a href="{{ link.data }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">Dataset</a>
        {% endif %}
        {% if link.bibtex %} 
        <a href="{{ link.bibtex }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">BibTex</a>
        {% endif %}
      </div>
    </div>
  </div>
</div>

{% assign journal_counter = journal_counter | plus: 1 %}
{% endfor %}

<h3 style="margin: 40px 0px 20px; font-size: 18px; color: #13294B; font-weight: 700;">Conference Publications</h3>

{% assign conference_counter = 1 %}
{% for link in site.data.publications.conferences %}

<div style="margin-bottom: 25px; text-align: left;">
  <div style="display: flex; align-items: flex-start; margin-bottom: 5px;">
    <span style="font-weight: 600; margin-right: 8px; color: #666; min-width: 25px;">[C{{ conference_counter }}]</span>
    <div style="flex: 1;">
      <div class="title" style="font-weight: 600; margin-bottom: 5px; color: #595959 !important;">
        {% if link.pdf %}<a href="{{ link.pdf }}" target="_blank" style="color: #595959 !important; text-decoration: none;">{{ link.title }}</a>{% else %}{{ link.title }}{% endif %}
      </div>
      <div class="author" style="margin-bottom: 3px;">{{ link.authors }}</div>
      <div class="periodical" style="margin-bottom: 8px;">
        {% if link.core_ranking %}
        <span class="badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 8px; font-size: 14px; padding: 2px 8px;">CORE {{ link.core_ranking }}</span>
        {% endif %}
        <em>{{ link.conference }}</em>
      </div>
      <div class="links">
        {% if link.pdf %} 
        <a href="{{ link.pdf }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">PDF</a>
        {% endif %}
        {% if link.code %} 
        <a href="{{ link.code }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">Code</a>
        {% endif %}
        {% if link.page %} 
        <a href="{{ link.page }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">Project</a>
        {% endif %}
        {% if link.data %} 
        <a href="{{ link.data }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">Dataset</a>
        {% endif %}
        {% if link.bibtex %} 
        <a href="{{ link.bibtex }}" target="_blank" class="btn badge" style="background-color: transparent; color: #595959 !important; border: 1px solid #ccc; margin-right: 5px; font-size: 14px; text-decoration: none; padding: 2px 8px;">BibTex</a>
        {% endif %}
      </div>
    </div>
  </div>
</div>

{% assign conference_counter = conference_counter | plus: 1 %}
{% endfor %}

</div>


