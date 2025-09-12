---
title: "Hıa Kúna?"
title_en: "What is Kuna?"
slug: "k1"
subject: "introduction to Kuna"
wip: true
---

# What is Kuna?

Kuna is a program that reads and interprets Toaq sentences. It parses the grammar of a Toaq sentence into a tree structure, where each leaf is a lexical unit (a **lexeme**) and each sub-tree is a grammatical unit (a **constituent**). Then, it works its way up this tree from the leaves, composing the meaning of the whole sentence from the meaning of each part.

In a way, such a program is "living proof" that Toaq is a loglang: we show that Toaq unambiguously encodes predicate logic by defining a mapping, in the form of an executable program, from Toaq sentences to syntax and semantics.

## Kuna is complex

Neither the inner workings nor the outputs produced by Kuna are simple to understand. Both are based on theories gathered across the fields of syntax and natural language semantics. The challenge is that we apply them all at once. Scientists often assume a simplified model of reality when studying the single phenomenon they're interested in; in much the same way, linguists studying some subject in semantics (like "plurals" or "aspects" or "scope") will zoom in on their object of study and rightfully cut out the rest of the complexity. But we must account for all of Toaq at once, and so Kuna will turn even the simplest of Toaq clauses into a daunting expression that pulls out all the semantic stops.

This part of Kóıtıeq serves as documentation for Kuna. It will be a fair bit more complex than the rest of Kóıtıeq. You may wish to have read and mostly understood all of the colored boxes in Kóıtıeq itself, before tackling this guide.

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

## Symbols for types

In Kuna, we use symbols to represent types: <math>○</math> for entities, <math>◐</math> for truth values, and <math>α › β</math> for functions. This is mostly for fun, but it has some tangible upsides. For one, we avoid the confusion common in semantics literature where lowercase letters mean different things as values and as types:

| Letter | As value | As type |
| :---: | :---: | :---: |
| <math>e</math> | an event | the _entity_ type |
| <math>t</math> | a time interval | the _truth value_ type |
| <math>v</math> | a value | the _event_ type |

It also lends a sort of iconicity to the system. We can begin to recognize certain combinations of symbols, and think of them as complex glyphs, without being tempted to unpack them into their parts.

## The basic types

What are entities (<math>○</math>)? They encompass anything "in the world" about which we might want to make predications, such as me, or your name, or Spain, or the fact that you are reading this textbook. And <math>◐</math> is the result of such a predication: true or false.

But these types alone are not enough to model real-life predications, which have truth values that depend on their context: time, the world, the current values of bound pronouns, and so on. Furthermore, we would like to analyze not just statements, but any kind of _speech act_ that a speaker might contribute to the discourse. To this end, there are at least some other "atomic" types that will come up in our analysis of Toaq sentences. Let's take a brief look at all of them.

<ol style="gap:0.5em;display:flex;flex-direction:column;">
<li><math>✲</math> is the type of <em>events</em>. An event is an <em>instance</em> of something being the case in some world, at some time.</li>
<li><math>〜</math> is the type of <em>possible worlds</em>. We rarerly deal with <math>〜</math> on its own: instead, a squiggly underline indicates a function from possible worlds to the type it's under. For example, <div class="kuna-math-container"><math><mrow><munderover><mrow><mi>○</mi></mrow><mo class="kuna-squiggle">⎵</mo><mo class="kuna-squiggle">⎴</mo></munderover></mrow></math><div class="kuna-squiggle bg-neutral-900 dark:bg-gray-200" style="top: 18.25px; left: 0px; width: 11.7667px; height: 3px;"></div></div> is short for <div class="kuna-math-container"><math><mrow><mi>〜</mi><mo>›</mo><mi>○</mi></mrow></math></div>. Later, we'll learn why this pattern is so common, and what roles it plays in our semantics.</li>
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
| <math>○</math> | <math>a, b, c…</math> | Entities |
| <math>◐</math> | <math>P, Q, R¸</math> | Truth values |
| <math>✲</math> | <math>e, e<sup>1</sup>, e<sup>2</sup>…</math> | Events |
| <math>〜</math> | <math>w, w<sup>1</sup>, w<sup>2</sup></math> | Worlds | 
| <math>🕔</math> | <math>t, t<sup>1</sup>, t<sup>2</sup></math> | Times |

To describe functions without giving them a name, we will use "lambda function" notation: <math>λx E</math> is a function mapping <math>x</math> to <math>E</math>. The following definitions are equivalent:

<blockquote><math>f(x)</math> := <b>red</b>(x) ∧ <b>sweater</b>(x)<br><math>f<mphantom>(x)</mphantom></math> := λx&nbsp; <b>red</b> x ∧ <b>sweater</b> x</blockquote>

