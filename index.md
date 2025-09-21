---
layout: chapter
title: Kóıtıeq
title_en: Walkway
---

A textbook for [Toaq](https://toaq.me).

<img width="100%" src="./tieq.svg" alt="An abstract illustration of a path of little black rectangles with colored side paths.">

## Chapters

<table class="index"><tbody>
{% for chapter in site.chapters %}
<tr style="{% if chapter.wip == true %}opacity:0.5{% endif %}">
  <td style="display:flex;align-items:baseline; width: 12rem;">{{chapter.chapter}}.
  <a lang="qtq" style="margin:0 0.5em;" href="{{chapter.url | relative_url}}"><b>{{ chapter.title }}</b></a>
  <div style="flex:1;border-bottom:2px dotted #8888"></div>
  </td>
  <td style="padding-left: 0.25em;">{{chapter.subject}}</td>
</tr>
{% endfor %}
</tbody></table>
