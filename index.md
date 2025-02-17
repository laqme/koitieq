---
layout: chapter
title: Koıtıeq
title_en: A Toaq textbook
---

This is a work-in-progress textbook for Toaq.

## Chapters

{% for chapter in site.chapters %}
1. [<b lang="qtq">{{ chapter.title }}</b>]({{ chapter.url | relative_url }}) (<span lang="en">{{ chapter.title_en }}</span>){% endfor %}
