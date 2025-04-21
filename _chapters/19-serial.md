---
title: "Joe chıe súq báq"
title_en: "You're a quick learner"
chapter: 19
slug: "19"
subject: "serial verbs"
---

## Conversation

> **A**: _Fı akımı ké haqrıaq ꝡo. Ma **buo** súq, **lá** soa já ké choaq kọshı?_{:.t}<br>
> **B**: _Rạnho… Chum **sho gẹfeao** jí ꝡeı._{:.t.sec}<br>
> **A**: _Feao súq môı hí raı?_{:.t}<br>
> **B**: _**Deq baı** jí báq haq, kéo… **juoq hıo** jí báq poq châ hí raı móq?_{:.t.sec}<br>
> **A**: _**Leo sı** súq kú, ꝡá **shue nhame** súq côm chóaq ba._{:.t}<br>
> **B**: _Ina. **Taı tua** jí séu hú nha._{:.t.sec}<br>
> **A**: _Tíu **mıu le** jí, ꝡá jıa gı tú raı. Aıka!_{:.t}<br>

<div class="side-by-side" markdown="1">

| Word | Meaning |
| --- | --- |
| _buo_{:.t} | ▯ is ready to **lá**{:.v} |
| _juoq_{:.t} | ▯ should **lá**{:.v} |
| _leo_{:.t} | ▯ tries to **lá**{:.v} |
| _shao_{:.t} | ▯ wants to **lá**{:.v} |
| _sho_{:.t} | ▯ becomes such that they **lá**{:.v} |
| _shue_{:.t} | ▯ keeps **lá**{:.v}-ing |
| _taı_{:.t} | ▯ succeeds at **lá**{:.v}-ing |
| _soa_{:.t} | ▯ helps ▯ |
| _choaq_{:.t} | ▯ is a guest |
| _kọshı_{:.t} | ▯ is first |
| _feao_{:.t} | ▯ is anxious |
| _châ hí raı_{:.t} | how? |
| _nhame_{:.t} | ▯ smiles |
| _com_{:.t} | ▯ happens at (audience) ▯ |
| _séu_{:.t} | at least |

</div>

## To-clauses with _lá_{:.t}

The word _lá_{:.t} introduces a _lá_{:.t}-clause. This is a subclause without a tense and with a "gap" subject _já_{:.t}, corresponding to a _to_-clause in English:

> _lá feao já_{:.t}<br>
> to be anxious
>
> _lá bua já Súomıgua_{:.t}<br>
> to live in Finland

In the table above, we see that _shao_{:.t} means "▯ wants to **lá**{:.v}." The object is a _lá_{:.t}-clause:

> _Shao jí, **lá bua já Súomıgua.**_{:.t}<br>
> I want **to live in Finland**.

A _lá_{:.t}-clause describes a **property**. _To be anxious_ is a property, and _to live in Finland_ is a property. A property is like a content clause with a "gap" in it, marked by _já_{:.t}.

In a Toaq dictionary, if a verb has "satisfies property ▯" in its definition, it means you can put a _lá_{:.t}-clause there. In this textbook, we'll just write **lá**{:.v} instead.

<details class="aside grammar" markdown="1">
<summary>The gap pronoun <i class="t">já</i></summary>

The pronoun _já_{:.t} doesn't have an English equivalent. In English, there's just a gap between _to_ and the verb where _já_{:.t} would go. But in Toaq, _já_{:.t} being an actual word means it doesn't have to be the subject of the _lá_{:.t}-clause. It can go somewhere else:

> _lá maı sá poq já_{:.t}<br>
> to be loved by someone
>
> _Shao nháo, lá maı sá poq já._{:.t}<br>
> She wants to be loved by someone.

It can even be a prepositional object.

> _lá marao súq gâq já_{:.t}<br>
> to be danced with by you<br>

</details>

<details class="aside semantics" markdown="1">
<summary>What are properties?</summary>

A property is a function from entities to statements. When we define _P_(_x_) as the statement _x lives in Finland_, then _P_ is a property, and _P_(_Mary_) is the statement _Mary lives in Finland_.

In semantics, we often use a notation from **lambda calculus** to describe a property without giving it a name. In this notation, our _P_ would be written as _λx. x lives in Finland_.

Toaq's grammar for _lá_{:.t}-clauses is a bit similar to this notation: we can think of _lá_{:.t} as meaning _λj._ and _já_{:.t} as a reference to this variable _j_.

<!--The _λx._ means we are introducing a function over a variable _x_, and what follows is the "body" of the function — some statement that may refer to the now-bound variable _x_.

The choice of variable (here _x_) is arbitrary: _λb. b lives in Finland_ is another way to write _P_.-->

The simplest Toaq verb that relates an entity to a property is _ıq_{:.t}, which means "▯ satisfies property ▯." Symbolically, _ıq a P_{:.t} means _P_(_a_).

> _lá bua já Súomıgua_{:.t}<br>
> <i>λx</i>. _x_ lives in Finland
>
> _Iq Méarı, lá bua já Súomıgua._{:.t}<br>
> (<i>λx</i>. _x_ lives in Finland)(Mary)
>
> _Bua Méarı Súomıgua._{:.t}<br>
> Mary lives in Finland.

</details>

## Serial verbs: _lá_{:.t} means merge

We saw that putting verbs side-by-side makes adjectives: _haq noqgı_{:.t} means _tasty food_.

When the first verb's definition ends in a **lá**{:.v} slot, however, we get a different behavior: the definitions of the two verbs **merge**.

<div class="serial-combine" markdown="1">

<div class="serial-part" markdown="1">

_buo_{:.t}<br>▯ is ready to **lá**{:.v}

</div>

<div class="serial-part" markdown="1">

_nuo_{:.t}<br>
▯ sleeps

</div>

</div>

<div class="serial-result" markdown="1">

_buo nuo_{:.t}<br>
▯ is ready to sleep

</div>

This _buo nuo_{:.t} is called a **serial verb**; the first verb is the **head** and the second verb is the **tail**.

When merging, the **lá**{:.v}-clause slot of the head and the subject of the tail both disappear. But if the tail has other slots, they'll be present in the serial verb:

<div class="serial-combine" markdown="1">

<div class="serial-part" markdown="1">

_buo_{:.t}<br>▯ is ready to **lá**{:.v}

</div>

<div class="serial-part" markdown="1">

_soı_{:.t}<br>
▯ fights ▯

</div>

</div>

<div class="serial-result" markdown="1">

_buo soı_{:.t}<br>
▯ is ready to fight ▯

</div>

Essentially, _Buo soı jí nháo_{:.t} is short for _Buo jí, **lá** soı <i>já</i> nháo_{:.t}. The tail's subject gets turned into _já_{:.t}.

## Serial verbs: _ꝡá_{:.t} means stack

There's another way verbs can form serial verbs. When the first verb's definition ends in a **ꝡá**{:.v} slot, the definitions **stack**.

<div class="serial-combine" markdown="1">

<div class="serial-part" markdown="1">

_dua_{:.t}<br>▯ knows that **ꝡá**{:.v}

</div>

<div class="serial-part" markdown="1">

_nuo_{:.t}<br>
▯ sleeps

</div>

</div>

<div class="serial-result" markdown="1">

_dua nuo_{:.t}<br>
▯ knows that ▯ sleeps

</div>

The difference compared to merging is that with stacking, the tail's subject doesn't disappear.

<div class="serial-combine" markdown="1">

<div class="serial-part" markdown="1">

_dua_{:.t}<br>▯ knows that **ꝡá**{:.v}

</div>

<div class="serial-part" markdown="1">

_cho_{:.t}<br>
▯ likes ▯

</div>

</div>

<div class="serial-result" markdown="1">

_dua cho_{:.t}<br>
▯ knows that ▯ likes ▯

</div>

Essentially, _Dua cho jí nháo Tóaqzu_{:.t} is short for _Dua jí, **ꝡá** cho nháo Tóaqzu_{:.t}.

<details class="aside grammar" markdown="1">
<summary>Complex serial verbs</summary>

The tail of a serial verb can itself be a serial verb. This means that three or more verbs can form one big serial verb, merging from right to left:

> _leo baı_{:.t}<br>
> ▯ tries to make ▯

> _shao (leo baı)_{:.t}<br>
> ▯ wants to try to make ▯

> _sho (shao (leo baı))_{:.t}<br>
> ▯ starts to want to try to make ▯

In lesson 8, we saw that a verb can be followed by adjectives. The whole truth is that a _serial verb_ can be followed by _serial adjectives_. Thus, we can replace every verb in

> _sá gıaqche zaomıa bomıa_{:.t}<br>
> some musician (who is) famous (and) wealthy<br>
> some wealthy, famous musician

with a serial verb, resulting in:

> _sá **leo gıaqche**{:.subs} **shao zaomıa**{:.subs} **shao bomıa**{:.subs}_{:.t}<br>
> some tries-to-be-musician (who is) wants-to-be-famous (and) wants-to-be-wealthy

Each "simple" verb, _without_ a trailing **lá**{:.v} or **ꝡá**{:.v} slot in its definition, marks the end of one of these little sub-serials.

</details>

<details class="aside grammar" markdown="1">
<summary>Serials and scope</summary>

There is a subtle but important difference between these sentences:

> <center><div class="scope t"><span class="sb"><i>Ꝡa</i></span> shao jí, <div class="scope t s2"><span class="sb"><i>lá</i></span> geq já&nbsp;<b>sía raı</b></div> da.</div></center>

> <center><div class="scope t"><span class="sb"><i>Ꝡa</i></span> shao geq jí <b>sía raı</b> da.</div></center>

The first sentence means "I want to be such that there is nobody that I meet" (I want to be alone). The scope of _sía_{:.t} is limited by the _lá_{:.t}-clause.

But the second sentence means "There is nobody that I want to meet." When we use a serial verb, there's no inner scope island, and _sía_{:.t} scopes over the whole sentence.

</details>
