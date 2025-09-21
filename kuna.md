---
layout: chapter
title: Méı'aq
title_en: Mountain pass
permalink: /kuna/
---

A guide to [Kuna](https://github.com/toaq/kuna) (a program that reads and interprets Toaq sentences), and the theory of semantics it's based on.

<img width="75%" style="margin:auto;" src="./meiaq.svg" alt="An abstract illustration of a path of little black rectangles with colored side paths.">


<div class="aside grammar" markdown="1">

This guide is much more technical than [Kóıtıeq](..). You should understand all the boxes in Kóıtıeq before reading Méı'aq. It's also fairly fast-paced: feel free to linger on each chapter and ask some questions before moving on.

</div>

## Chapters

<table class="index"><tbody>
{% for kuna_page in site.kuna %}
<tr>
  <td style="display:flex;align-items:baseline; width: 15rem;">{{kuna_page.chapter}}.
  <a lang="qtq" style="margin:0 0.5em;" href="{{kuna_page.url | relative_url}}"><b>{{ kuna_page.title }}</b></a>
  <div style="flex:1;border-bottom:2px dotted #8888"></div>
  </td>
  <td style="padding-left: 0.25em;">{{kuna_page.subject}}</td>
</tr>
{% endfor %}
</tbody></table>
