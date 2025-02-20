---
layout: chapter
title: Koıtıeq
title_en: A Toaq textbook
---

This is a work-in-progress textbook for Toaq.

## Chapters

<table class="index"><tbody>
{% for chapter in site.chapters %}
<tr>
  <td><a href="{{chapter.url | relative_url}}"><b lang="qtq">{{chapter.chapter}}. {{ chapter.title }}</b></a></td>
  <td style="padding-left: 0.25em;">… {{chapter.subject}}</td>
</tr>
{% endfor %}
</tbody></table>
