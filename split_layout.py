import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find where the TOPBAR ends and HERO starts
hero_start = html.find('<!-- HERO -->')
# Find where the FOOTER starts
footer_start = html.find('<!-- FOOTER -->')

top = html[:hero_start]
body_content = html[hero_start:footer_start]
bottom = html[footer_start:]

# Replace title
top = top.replace('<title>Papá Gamer Mex — El medio gamer de las familias mexicanas</title>', '<title>{{ title | default("Papá Gamer Mex — El medio gamer de las familias mexicanas") }}</title>')

base_njk = top + '\n<main>\n  {{ content | safe }}\n</main>\n' + bottom

with open("_includes/base.njk", "w", encoding="utf-8") as f:
    f.write(base_njk)

index_njk = '---\nlayout: base.njk\n---\n\n' + body_content

with open("index.njk", "w", encoding="utf-8") as f:
    f.write(index_njk)

# We can also create a post.njk layout for articles
post_njk = """---
layout: base.njk
---
<article class="section" style="max-width: 800px; margin: 0 auto; padding-top: 2rem;">
  <div style="margin-bottom: 2rem;">
    {% if category %}
      <span class="cat-tag tag-cyan" style="position: static; display: inline-block; margin-bottom: 1rem;">{{ category }}</span>
    {% endif %}
    <h1 style="font-family: 'Exo 2', sans-serif; font-size: 2.5rem; color: var(--white); margin-bottom: 1rem;">{{ title }}</h1>
    <div style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem;">
      <span>📅 {{ page.date | date("yyyy-MM-dd") }}</span> | <span>✍️ {{ author }}</span>
    </div>
    {% if image %}
      <img src="{{ image }}" alt="{{ title }}" style="width: 100%; border-radius: 12px; margin-bottom: 2rem;">
    {% endif %}
  </div>
  
  <div class="post-content" style="font-size: 1.1rem; line-height: 1.8; color: var(--text);">
    {{ content | safe }}
  </div>
</article>

<style>
.post-content h2 { font-family: 'Exo 2', sans-serif; color: var(--white); margin: 2rem 0 1rem; }
.post-content h3 { font-family: 'Exo 2', sans-serif; color: var(--cyan); margin: 1.5rem 0 1rem; }
.post-content p { margin-bottom: 1.5rem; }
.post-content a { color: var(--cyan); text-decoration: none; }
.post-content a:hover { text-decoration: underline; }
.post-content ul, .post-content ol { margin-bottom: 1.5rem; padding-left: 2rem; }
.post-content li { margin-bottom: 0.5rem; }
.post-content blockquote { border-left: 4px solid var(--purple); padding-left: 1rem; color: var(--text-muted); font-style: italic; margin-bottom: 1.5rem; }
</style>
"""

with open("_includes/post.njk", "w", encoding="utf-8") as f:
    f.write(post_njk)

print("Split successful!")
