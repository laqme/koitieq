---
title: "Hıa Kúna?"
title_en: "What is Kuna?"
chapter: 1
slug: "1"
subject: "introduction to Kuna"
---

## Introduction

<!-- This counterpart to Kóıtıeq documents _Kuna_, It assumes you've finished Kóıtıeq, and so you're comfortable with Toaq grammar. However, you don't need to understand Kuna in order to speak Toaq. -->

Kuna is a program that reads and interprets Toaq sentences. It parses the grammar of a Toaq sentence into a tree structure, where each leaf is a lexical unit (a **lexeme**) and each sub-tree is a grammatical unit (a **constituent**). Then, it works its way up this tree from the leaves, composing the meaning of the whole sentence from the meaning of each part.

In a way, such a program is "living proof" that Toaq is a loglang: we show that Toaq unambiguously encodes predicate logic by defining a mapping, in the form of an executable program, from Toaq sentences to syntax and semantics.

## Kuna is complex

Neither the inner workings nor the outputs produced by Kuna are simple to understand. Both are based on theories gathered across the fields of syntax and natural language semantics. The challenge is that we apply them all at once.

Scientists often assume a simplified model of reality when studying the single phenomenon they're interested in; in much the same way, linguists studying some subject in semantics (like "plurals" or "aspects" or "scope") will zoom in on their object of study and rightfully cut out the rest of the complexity. But we must account for all of Toaq at once, and so Kuna will turn even the simplest of Toaq clauses into a daunting expression that pulls out all the semantic stops.

This part of Kóıtıeq serves as documentation for Kuna. It will be a fair bit more complex than the rest of Kóıtıeq. You'll want to have read and mostly understood all of the colored boxes in Kóıtıeq itself, before tackling this guide.

We will describe a theory of Toaq semantics in all of its messy implementation details. We will work our way up, by first tackling the abstract concepts, and then describing a kind of "mini-Toaq" to which we add layers of complexity one by one.

## Compositionality and functions

The idea that Kuna can do its job at all — build up the meaning of a sentence by working up from the leaves — is called the [principle of compositionality](https://en.wikipedia.org/wiki/Principle_of_compositionality). An early approach to natural language semantics was Richard Montague's [Montague grammar](https://en.wikipedia.org/wiki/Montague_grammar), which modeled the meaning of the various parts of speech as mathematical _functions_. To compose meanings, we apply functions to arguments.

For example, we may think of adjectives as functions from "entities" to "truth-values": the word *red* means some function *R* that maps red things to _True_, and non-red things to _False_.

<figure>
  <div class="tree">
    <div>this sweater is red<br><math>R(s)</math></div>
    <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
      <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
      <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
    </svg>
    <div class="tree-children">
      <div>this sweater<br><math>s</math></div>
      <div>is red<br><math>R</math></div>
    </div>
  </div>
</figure>

If we say this is the fundamental way semantics "compose", we need to answer a basic question: how do we know that the formula at the top should be <math>R(s)</math> and not <math>s(R)</math>?

The answer we commit to is that our semantics are **type-driven**. We know which way around to apply things because we keep track of the _types_ as we denote constituents. At any point we either have a function of type <math>A → B</math> on the left and an argument of type <math>A</math> on the right, or the other way around. The types tell us which operation to perform. So let's write them in the tree:

<figure>
  <div class="tree">
    <div>this sweater is red<br><math>R(s) : ◐</math></div>
    <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
      <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
      <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
    </svg>
    <div class="tree-children">
      <div>this sweater<br><math>s : ○</math></div>
      <div>is red<br><math>R : ○ › ◐</math></div>
    </div>
  </div>
</figure>

This innocent diagram summarizes the essence of Kuna already: parsing the structure of a sentence, and letting the _types_ of the leaves tell us how to combine the _meanings_ of constituents, all the way up to the top of the tree.

We'll close this first chapter with a note on the _sıteleq_{:.t} used in Kuna to represent types.

## Symbols for types

In Kuna, we use symbols to represent types: <math>○</math> for entities, <math>◐</math> for truth values, and <math>α › β</math> for functions. This is mostly for fun, but it has some tangible upsides. For one, we avoid the confusion common in semantics literature where lowercase letters mean different things as values and as types:

| Letter | As value | As type |
| :---: | :---: | :---: |
| <math>e</math> | an event | the _entity_ type |
| <math>t</math> | a time interval | the _truth value_ type |
| <math>v</math> | a value | the _event_ type |

It also lends a sort of iconicity to the system. We can begin to recognize certain combinations of symbols, and think of them as complex glyphs, without being tempted to unpack them into their parts.

# Concepts

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
