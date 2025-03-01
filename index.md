---
layout: chapter
title: Kóıtıeq
title_en: Walkway
---

This is a work-in-progress textbook for Toaq.

<img width="100%" src="./tieq.svg" alt="An abstract illustration of a path of little black rectangles with colored side paths.">

## Chapters

<table class="index"><tbody>
{% for chapter in site.chapters %}
<tr>
  <td style="width: 10rem;"><a lang="qtq" href="{{chapter.url | relative_url}}"><b>{{chapter.chapter}}. {{ chapter.title }}</b></a></td>
  <td style="padding-left: 0.25em;">… {{chapter.subject}}</td>
</tr>
{% endfor %}
</tbody></table>
