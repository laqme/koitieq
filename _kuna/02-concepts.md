---
title: "Béoqsıo"
title_en: "Concepts"
chapter: 2
slug: "2"
subject: "types, intension, discourse, deixis"
---

## The basic types

What are entities (<math>○</math>)? They encompass anything "in the world" about which we might want to make predications, such as me, or your name, or Spain, or the fact that you are reading this textbook. And <math>◐</math> is the result of such a predication: true or false.

But these types alone are not enough to model real-life predications, which have truth values that depend on their context: time, the world, the current values of bound pronouns, and so on. Furthermore, we would like to analyze not just statements, but any kind of _speech act_ that a speaker might contribute to the discourse. To this end, there are at least some other "atomic" types that will come up in our analysis of Toaq sentences. Let's take a brief look at all of them.

<ol style="gap:0.5em;display:flex;flex-direction:column;">
<li><math>✲</math> is the type of <em>events</em>. An event is an <em>instance</em> of something being the case in some world, at some time.</li>
<li><math>〜</math> is the type of <em>possible worlds</em>. We rarerly deal with <math>〜</math> on its own: instead, a squiggly underline indicates a function from possible worlds to the type it's under. For example, <span class=int>○</span> is short for <div class="kuna-math-container"><math><mrow><mi>〜</mi><mo>›</mo><mi>○</mi></mrow></math></div>. Later, we'll learn why this pattern is so common, and what roles it plays in our semantics.</li>
<li><math>🕔</math> is the type of <em>time intervals</em>. Really, they are just <em>sets</em> of points in time, and they need not be contiguous like a real interval. They are used to describe or bound when an event happens, and as such they'll come up when we dig into the semantics of tenses.</li>
<li><math>!</math> is the type of <em>speech acts</em>. For example: a declaration, a question, a wish. This is the type of Toaq sentences: Kuna describes which speech act a sentence amounts to.</li>
</ol>


<details class="aside semantics" markdown="1">
<summary>Metalanguage</summary>
If entities encompass anything in the world, why don't they encompass events or time intervals? Why isn't everything type <math>○</math>?

There are, in fact, entities corresponding to such things. When we talk about _ké jıaq_{:.t} or _ké hora_{:.t}, they are entities just as _ké kune_{:.t} and _ké sıo_{:.t} are. The distinction is rather made in the **metalanguage**; the symbolic language we are describing right now, which Kuna uses to talk _about_ Toaq. So <math>○</math> refers to any such things as described _in Toaq_, where they can be subjects and objects and referents of pronouns, and <math>🕔</math> refers to time intervals _only_ in the context of describing the underlying behavior of tenses for Kuna to understand and manipulate.

Making the distinction between <math>○</math> and other types helps the semantics be "type-directed" without confusing the language for the metalanguage. It also keeps us from running into issues when denoting things like "this sentence is false":

</details>

## Operators

Kuna inherits the following standard notation for operators from mathematical logic.

| Symbol | Description |
| :---: | --- |
| <math>e : ✲</math> | <math>e</math> has type <math>✲</math> |
| <math>∃x P</math> | there exists x such that P |
| <math>∀x P</math> | for all x, P |
| <math>∧</math> | and |
| <math>∨</math> | or |
| <math>¬</math> | not |
| <math>→</math> | implies |
| <math>↔</math> | if and only if |

Additionally, <math>≺</math> is the "amongness" relation on pluralities, and we like to write function application without parentheses: <math>f g h ∧ x y</math> means <math>(f(g))(h) ∧ x(y)</math>.

In this text, we'll use <math>x := y</math> to mean: <math>x</math> is defined as being equal to <math>y</math>.

## Notation for values

We will stick to certain sets of letters when naming members of these basic types. Here are our picks:

| Type | Letter | Description |
| --- | --- | --- |
| <math>○</math> | <math>𝑎, 𝑏, 𝑐…</math> | Entities |
| <math>◐</math> | <math>𝑃, 𝑄, 𝑅…</math> | Truth values |
| <math>✲</math> | 𝑒, 𝑒¹, 𝑒²… | Events |
| <math>〜</math> | 𝑤, 𝑤¹, 𝑤²… | Worlds | 
| <math>🕔</math> | 𝑡, 𝑡¹, 𝑡²… | Times |

To describe functions without giving them a name, we will use "lambda function" notation: <math>λx E</math> is a function mapping <math>x</math> to <math>E</math>. Here, <math>E</math> is some expression that may refer to the input variable <math>x</math>. So the following definitions are equivalent:

<blockquote><math>f(x)</math> := <b>red</b>(x) ∧ <b>sweater</b>(x)<br><math>f<mphantom>(x)</mphantom></math> := λx&nbsp; <b>red</b> x ∧ <b>sweater</b> x</blockquote>

## Denotation

We say that Toaq words or phrases **denote**, or simply "stand for", certain formulas. When describing Toaq's semantics, or Kuna's implementation, we will often use "denotation brackets" ⟦…⟧ to denote this relationship between Toaq words or phrases and expressions in our mathematical language.

For example, the simplest stab at the meaning of _rú_{:.t} looks something like this:

> ⟦_rú_{:.t}⟧ = <math>λ𝑃 λ𝑄&nbsp; 𝑄 ∧ 𝑃</math>

We can also use denotation brackets in the middle of an expression, to portray a halfway-denoted phrase whose further meaning depends only on the meaning of its smaller parts.

> ⟦_rú ruqshua_{:.t}⟧ = <math>λ𝑄&nbsp; 𝑄 ∧ ⟦<i class=t>ruqshua</i>⟧</math>

The denotation of many lexemes will just be a constant "lexical function" that shares its name. Don't confuse the Toaq word _zuche_{:.t}, which is a verb, is five letters long, et cetera, with the function **zuche** of type <span class=int>○ › ✲ › ◐</span> that produces **true** exactly when its arguments describe a being-a-linguist event:

> ⟦_zuche_{:.t}⟧ = **zuche**<br>
> <span style="display:inline-flex;width:3.6em"></span> = λ𝑤 λ𝑎 λ𝑒&nbsp; **zuche** 𝑤 𝑎 𝑒

(In time, we'll get around to discussing why it takes these arguments in this order.)

## Intension

In philosophy, the word **intension** (spelled with an _s_: not "intention") refers to definitions in terms of properties, or "necessary and sufficient conditions", rather than **extension**, a definition by enumerating the referents.

By extension, in semantics, an **intensional** interpretation of a phrase is one that retains the _sense_ of the words used, whereas an **extensional** interpretation is one that directly gets at the _thing referred to_.

### Why do we need intension?

It turns out that _extension_, i.e. identifying expression with their referents, is not enough for . Suppose that ⟦_Líma_{:.t}⟧ and ⟦_ké joqdoaq po Pérugua_{:.t}⟧ are equal, and refer to Lima (the capital of Peru). Then consider the following sentence:

> _Chı Náo, ꝡá eq ké joqdoaq po Chílegua Líma._{:.t}<br>
> Nao thinks the capital of Chile is Lima.

This describes a reasonable belief, but the principle of compositionality would tell us that this would mean the same as

> _Chı Náo, ꝡá eq ké joqdoaq po Chílegua ké joqdoaq po Pérugua._{:.t}<br>
> Nao thinks the capital of Chile is the capital of Peru.

which is pretty absurd. There is something about these descriptions that we are not capturing, when we skip straight to _referents_ or _extensions_ in our denotation of definite references.

### Intension in Kuna

The solution to this problem used by Kuna is to make the denotations functions from possible worlds to entities: <span class=int>○</span> instead of ○.

> ⟦_Líma_{:.t}⟧ = λ𝑤&nbsp; Lima in world 𝑤<br>
> ⟦_ké joqdoaq po Pérugua_{:.t}⟧ = λw&nbsp; the capital of Peru in world 𝑤

We can imagine possible worlds in which Lima had been founded elsewhere, or Peru had ended up with other borders and picked another capital. When given such worlds as input, these functions will differ in meaning. In this way the functions capture the _sense_ of what was said.

Similarly, ⟦_ꝡá eq ké joqdoaq po Chílegua Líma_{:.t}⟧ does not just equal **false**, because the principle of compositionality would say that the above sentence would reduce to "Nao thinks **false**", which isn't what we want.

Instead, propositions get the type <span class=int>◐</span> rather than ◐: their truth value depends on the world. By denoting the content clause as

> λ𝑤&nbsp; whether, in world 𝑤, the capital of Chile is Lima

we retain the _sense_ of what is said.

Here is a glimpse at the reason for the "squiggle" notation: world-dependence, or intensionality, is expressive and omnipresent in our semantics, while at the same time being a "layer" we don't want to draw too much attention to. We may think of <span class=int>○ › ◐</span> as a special flavor of function from ○ to ◐, that incidentally carries its "sense" with it by depending on the world variable. 

## Discourse and deixis

What is a conversation, or **discourse**, made up of? The common view says _speech acts_: questions, requests, statements, and so on. We denote these with the type <math>!</math>, and for now that is about all we do with them.

Speech acts update the _discourse state_, which describes which participants are committed to the truth of which facts, which questions have been raised, which variables are bound, and so on. Kuna does not yet model the discourse state beyond some support for cross-sentence anaphora. For our purposes, words like _da_{:.t} and _ba_{:.t} "wrap" a proposition up into a speech act, but we have no way of running or combining speech acts: we can only look inside them.

Sometimes, though, the meaning of a word or sentence hinges not just on the world it's said in and the words that came before it, but even on its speaker and their surroundings. A word like _súq_{:.t} or _naı_{:.t} doesn't mean much without the context of who it's said to, or when it's said. Such words are called **deictic**, and using deictic words is called **deixis**.

Kuna models deixis as constituents "depending on the deictic state", the same way it models intensionality as constituents "depending on the world variable." Again we have special notation: placing a curved arrow before a type marks it as a function from deictic state to that type, and so something like ↪ <span class=int>◐</span> describes the type of _deictic_ propositions.
