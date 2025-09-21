---
layout: chapter
title: Méı'aq
title_en: Mountain pass
permalink: /kuna/
---

A guide through [Kuna](https://github.com/toaq/kuna), a program that reads and interprets Toaq sentences.

## Chapters

<table class="index"><tbody>
{% for kuna_page in site.kuna %}
<tr>
  <td style="display:flex;align-items:baseline; width: 12rem;">{{kuna_page.chapter}}.
  <a lang="qtq" style="margin:0 0.5em;" href="{{kuna_page.url | relative_url}}"><b>{{ kuna_page.title }}</b></a>
  <div style="flex:1;border-bottom:2px dotted #8888"></div>
  </td>
  <td style="padding-left: 0.25em;">{{kuna_page.subject}}</td>
</tr>
{% endfor %}
</tbody></table>
