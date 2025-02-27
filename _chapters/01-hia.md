---
title: "Hıa Tóaqzu?"
title_en: "What is Toaq?"
chapter: 1
slug: "1"
subject: "what is Toaq?"
---

This book is a textbook for Toaq. Toaq is a constructed language, or _conlang:_ a human language created with a purpose, like Esperanto or Toki Pona. The name is pronounced /ˈtʰo.aŋ/.

What, then, is its purpose? Toaq is a **loglang**, in the tradition of Loglan and Lojban. Conlangs in this family investigate the interaction between logic and language. Specifically, in Toaq, each valid sentence has a single way to parse its grammar, and then _calculate_ its meaning by following a certain algorithm.

(To avoid any confusion or debate about the precise definition of the word _loglang_, we sometimes also refer to this goal by saying that Toaq is **monoparsing**.)

At the same time, Toaq is also an **artlang**. It tries to achieve its loglang goals in a way that still feels like a natural language. Its design weighs "logic" with elegance and aesthetics.

Essentially, Toaq is a [_formal language_](https://en.wikipedia.org/wiki/Formal_language) in which you may talk about everyday things. It looks like this:

> _Jueq há ké kubolue róı ké tıuq ba._{:.t} \
> _Mix the egg yolks and the sugar together._{:.sm}
> <audio controls><source src="../assets/audio/jueq-ha.ogg"></audio>
>
> _Haıda ní sheq téqna nha, hóꝡa jóm fıe!_{:.t} \
> _This blade shall lay waste to thee, vile demon!_{:.sm}
> <audio controls><source src="../assets/audio/haida-ni.ogg"></audio>
>
> _Foaına, Tóaqzu bï, sá jıoqjuao nä, tıembo tú kuna zujuaodue tó shí chateı, lâ muaogaı há ké kunateı hoqbo, rúbıe jıoq há ké muı hôq lîeı jíoqjuao da._{:.t} \
> _Specifically, as for Toaq, there is an algorithm J, so that each valid sentence has only one way to parse its grammar, and then calculate its meaning by following J._{:.sm}
> <audio controls><source src="../assets/audio/foaina.ogg"></audio>
>
> <!--
> _jeba ahaha sieqnhe juagi ni2 foto vei_{:.t} \
> _dude hahaha this pic is amazingly cursed_{:.sm}
> <audio controls><source src="../assets/audio/jeba.ogg"></audio>
> -->
>
<!-- > _Gıtu :) â, ma noalıe súq kú, lá joaıtaı já báq toa tıao chôq Tóadua móq?_{:.t} \
> _No worries :) ah, is it that you're having trouble finding the right words using Toadua?_{:.sm} -->
>
> _« Bu deq kuıdo jí pó áq, kushe », ïe kuq Álısı hóa kı, \
> « kûı kú, ꝡá bu eq jí áq dâ. »_{:.t} \
> _“I can’t explain myself, I’m afraid, sir,” said Alice, “because I’m not myself, you see.”_{:.sm}
> <audio controls><source src="../assets/audio/alisi.ogg"></audio>
{: style="line-height:1.3;margin:2em 3em;"}

Toaq exists at the intersection of human languages like English and formal languages like Prolog, and may be analyzed using tools from either world. This textbook sets out to teach Toaq more or less as though it were a natural, human language. The main parts of the text stay friendly, and focus on helping you understand and communicate in Toaq.

From time to time, there will be "asides," in colored boxes, explaining what is really going on behind the scenes, but these are merely supplemental to the main texts and explanations in the book. You will encounter the following kinds of asides:

<details class="aside grammar" markdown="1">
<summary>Grammar aside</summary>
This box contains grammar details. For example, instead of simply telling you that _shao nuo_{:.t} means _want to sleep_, it might point out that this construction is known as a _serial verb_.
</details>

<details class="aside semantics" markdown="1">
<summary>Semantics aside</summary>
This box contains semantic details. For example, it may point out that _Nuo jí da_{:.t} asserts the existence of a _sleeping event_ at some definite, but unspecified time.
</details>

<details class="aside culture" markdown="1">
<summary>Culture aside</summary>
This paragraph contains cultural details. For example, it may tell you that _nuotoa_{:.t} are words dreamt up by Toaq community members in their sleep, like _naqdelıq_{:.t} _tomboy_.
</details>

It may be wise to skip over technical asides on a first reading of the book, and then, once you've become more comfortable with Toaq, read the book again and engage with the contents of the asides as well.

## Versions of Toaq

Toaq's development has taken it through multiple _versions_. Each new version is named by a new Greek letter. Toaq Alpha (2013) and Toaq Beta (2017) served as predecessors to a planned "final version" of the language. The next version, in 2021, was called Gamma by the community, and released roughly alongside a tutorial called _Toaq with Ease_.

In the process of formalizing this language by writing a parser, it became clear that the language needed some far-reaching changes to meet its goal, leading to the development of Toaq Delta in 2022. The formalization process continued with work on a new parser, called [_Kuna_](https://github.com/toaq/kuna). Questions that came up during the development of this new parser, in turn, inspired some new ideas about scope, negation, and so on. This course aims to document a version of Toaq that incorporates those ideas while not being so radical as to call it Epsilon.

<div class="aside grammar" markdown="1">

(It's Toaq Delta + [Simple Focus](https://toaq.me/Simple_Focus) + [Pronoun structure](https://toaq.me/Pronoun_structure) + [Some Scope Creep](https://toaq.me/Some_Scope_Creep) + [Kıazıu](https://toaq.me/Kıazıu) + [Eatoaq](https://robin.town/blog/sa-ea-buriaq)'s complementizers, pendents, generics, discursives, variable names.)

</div>

## How to use this textbook

This textbook serves as the "post-Delta" answer to _Toaq with Ease_, from which it inherits a few qualities:

- Each lesson is structured around a small dialogue, followed by explanations.
- The book aims to teach both vocabulary and grammar, following actual usage.
- By the end, the reader should be able to communicate in simple Toaq.

No English translations are given to the dialogues. You are encouraged to repeat the contents of each lesson until you can understand the dialogue without much trouble. If you have any questions, check out the [Toaq Wiki](https://toaq.me), or [ask us on Discord](https://discord.gg/BjRry9QtwY). _Taıba!_{:.t}
