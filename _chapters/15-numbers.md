---
title: "Ké jıuchaqpatı"
title_en: "The birthday party"
chapter: 15
slug: "15"
subject: "numbers and dates"
---

## Numbers

The simplest Toaq numbers are made from the following words:

| Word | Meaning |
| --- | --- |
| _koam_{:.t} | zero |
| _shı_{:.t} | one |
| _gu_{:.t} | two |
| _saq_{:.t} | three |
| _jo_{:.t} | four |
| _fe_{:.t} | five |
| _cı_{:.t} | six |
| _dıaı_{:.t} | seven |
| _roaı_{:.t} | eight |
| _neı_{:.t} | nine |
| _heı_{:.t} | ten |

In the falling tone, a number acts like a **counting verb** or adjective:

> _fe_{:.t}<br>▯ are five in number
>
> _**Neı** ké chaıbıo._{:.t}<br>
> The teacups **are nine**.
>
> _Cho jí ké lua **gu**._{:.t}<br>
> I like the **two** stories.

In the rising tone by itself, it refers to an **abstract quantity**:

> _fé_{:.t}<br>the number five
>
> _Ma reutoaı **sáq**?_{:.t}<br>
> Is **three** a prime number?

In the rising tone and followed by a verb, it acts as an **article**:

> _fé kue_{:.t}<br>five books
>
> _Zudeq jí **jó** zu._{:.t}<br>
> I speak **four** languages.

<details class="aside semantics" markdown="1">
<summary>Plural logic</summary>

Toaq is built on **plural logic**. We say a variable can refer to _things_, plural. For example, when we turn _"The teacups are nine"_ into a formula, we might say: _xx_ _are_ teacups, and _xx_ _are_ nine. We don't need to talk about a "set" of nine teacups.

What's the point? Consider the following example. When we say "the students gathered", it means they did so as a group. But "the students ate" means each individual student ate. In _singular logic_, we might put this as: _gather(S)_, for some set of students _S_, and then ∀_x_ ∈ _S_: _ate(x)_. That is, we interpret "the students" differently in these two sentences. But then how do we make sense of "the students gathered and ate"? Maybe sets aren't actually how language works.

If we embrace plurality from the ground up in our semantics, and say "_xx_ **are** students, and _xx_ gathered, and _xx_ ate," we can let the predicates themselves decide what to do with those plurals. Instead of talking about sets and membership, we take the relationship _xx are among yy_ (written _xx_ ≺ _yy_) as fundamental.

All this is why _fe_{:.t} can just mean: "▯ **are** five in number."

For more information, see [Plural Quantification](https://plato.stanford.edu/entries/plural-quant/) in the Standford Encyclopedia of Philosophy.

</details>

<details class="aside semantics" markdown="1">
<summary>A plural tour of articles</summary>
Toaq's _sá_{:.t} corresponds to a plural existential quantifier ∃_xx_, so _sá poq_{:.t} means "for some people _xx_."

> _Kueq sá sıomche._{:.t}<br>
> Some students gathered.<br>
> <small>[∃xx: student(xx)] gather(xx)</small>

But the universal quantifier we've been using, _tú_{:.t}, is really the _singular_ universal ∀_x_, meaning "for each _x_." This just turns out to be what's convenient a lot of the time. However, it does mean that you can't meaningfully say:

> _Kueq tú sıomche._{:.t.bad}<br>
> Each student gathered.<br>
> <small>[∀x: student(x)] gather(x)</small>

There is another quantifier, _tútu_{:.t}, corresponding to ∀_xx_. So _tútu poq_{:.t} means "for any person or people _xx_," but it doesn't seem to come up often in everyday speech.

> ? _Kueq tútu sıomche._{:.t}<br>
> Any students gathered.<br>
> <small>[∀xx: student(xx)] gather(xx)</small>

This sentence still means something weird: if there are three students (A, B, and C), then it says _"ABC gathered, and AB gathered, and AC gathered, and BC gathered, and A gathered, and B gathered, and C gathered."_ Ranging over all pluralities is rarely what we want.

More useful is _túq_{:.t}, an article which means something closer to _all_ than to _each_. The phrase _túq poq_{:.t} "all people" refers to the "maximal" _xx_ that are people, in the sense that for any _yy_ that are also people, _yy_ ≺ _xx_.

> _Kueq túq sıomche._{:.t}<br>
> All students gathered.<br>
> <small>gather(xx), where student(xx) and [∀yy: student(yy)] yy ≺ xx</small><br>
> <small>Some students gathered, and _any_ students were among them.</small>

All this to say: when we use a number as an article, it means the same thing as _sá_{:.t} plus a counting verb, which is to claim the existence of some plural _xx_ while restricting its number.

> _Kueq héı sıomche._{:.t}<br>
> _Kueq sá sıomche heı._{:.t}<br>
> Ten students gathered.<br>
> <small>∃xx: student(xx) and ten(xx) and gather(xx)</small>

This means that _Zudeq jí shí zu_{:.t} means "I speak a language" and not "I speak exactly one language." We'll learn how to say that some other time!

</details>

## Counting higher

| Word | Meaning |
| --- | --- |
|  _heı_{:.t} | ten |
| _guheı_{:.t} | twenty |
| _guheı shı_{:.t} | twenty-one |
| _fue_{:.t} | 100 |
| _saqfue heı_{:.t} | 310 |
| _saqfue guheı_{:.t} | 320 |
| _saqfue cı_{:.t} | 306 |

The words for "twenty, thirty…" are made by compounding digits with _heı_{:.t}. The words for "two hundred, three hundred…" are compounds ending in _fue_{:.t}. To say two-digit and three-digit numbers, we put these parts next to each other to add them together. For example, 234 is _gúfue saqheı jo_{:.t} (two-hundred thirty four). Only the first word gets the rising tone:

{:.tone-figure}
_gúfue_{:.t2} _saqheı_{:.t1} _jo_{:.t1}

<audio controls class="center-audio"><source src="../assets/audio/gufue-saqhei-jo.mp3"></audio>

<details class="aside grammar" markdown="1">
<summary>Thousands, millions, decimals</summary>

To count even higher, we use the following "thousands separator" words:

| Word | Meaning |
| --- | --- |
| _bıq_{:.t} | thousand |
| _nhoeı_{:.t} | million |
| _gıga_{:.t} | billion |
| _tera_{:.t} | trillion |

If there's no number before the thousands-word, _shí_{:.t} is implied.

> _gúheı saq bıq jofue feheı cı_{:.t}<br>
> twenty-three thousand, four-hundred and fifty-six (23,456)
>
> _nhóeı neıfue bıq_{:.t}<br>
> one million, nine-hundred thousand (1,900,000)

The word _co_{:.t} is a spoken decimal point.

> _gú co saq koam jo_{:.t}<br>
> two point three zero four (2.304)

</details>

<img width="100%" src="../saq.svg" alt="An abstract illustration of colored triangles.">

## Dates

The names of the months are formed by adding _jue_{:.t} to the numbers 1 through 12.

| Word | Meaning |
| --- | --- |
| _shıjue_{:.t} | ▯ is a January |
| _gujue_{:.t} | ▯ is a February |
| _saqjue_{:.t} | ▯ is a March  |
| _jojue_{:.t} | ▯ is an April |
| _fejue_{:.t} | ▯ is a May |
| _cıjue_{:.t} | ▯ is a June |
| _dıaıjue_{:.t} | ▯ is a July |
| _roaıjue_{:.t} | ▯ is an August |
| _neıjue_{:.t} | ▯ is a September |
| _heıjue_{:.t} | ▯ is an October |
| _heıshıjue_{:.t} | ▯ is a November |
| _heıgujue_{:.t} | ▯ is a December |

By combining number words with _chaq_{:.t}, we get words for the days of the month:

| Word | Meaning |
| --- | --- |
| _fechaq_{:.t} | ▯ is a 5th of the month |
| _saqheıshıchaq_{:.t} | ▯ is a 31th of the month |

You can talk about dates like so:

> _Rao ké patı **ké fechaq po ké saqjue**._{:.t}<br>
> The party is on the 5th of March.

<details class="aside culture" markdown="1">
<summary>Poetic calendar</summary>

There's also this alternative set of month names, where each month's name is an alliteration based on nature or the month's "role" in the year — the English back-translations below are just to give you an idea.

| Word | Meaning |
| --- | --- |
| _chıochu_{:.t} | January – _Newheart_ |
| _luqluoq_{:.t} | February – _Calmstead_ |
| _ırue'ısıe_{:.t} | March – _Galegrace_ |
| _geagom_{:.t} | April – _Hightorch_ |
| _suaqsoq_{:.t} | May – _Songpeak_ |
| _nuoqnea_{:.t} | June – _Mirrorwide_ |
| _nharunhuo_{:.t} | July – _Stormful_ |
| _shuaqshoa_{:.t} | August – _Giftdeep_ |
| _reoruq_{:.t} | September – _Huefall_ |
| _feafao_{:.t} | October – _Bravestop_ |
| _hoehıu_{:.t} | November – _Sunbrook_ |
| _cuaocoa_{:.t} | December – _Passbridge_ |

</details>
