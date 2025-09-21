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

<img width="100%" src="../../soai.svg" alt="An abstract illustration of colored lines at various angles.">

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

In Kuna, we use symbols to represent types: for example, <math>○</math> for entities, <math>◐</math> for truth values, and <math>α › β</math> for functions. This is mostly for fun, but it has some tangible upsides. For one, we avoid the confusion common in semantics literature where lowercase letters mean different things as values and as types:

| Letter | As value | As type |
| :---: | :---: | :---: |
| <math>e</math> | an event | …or the _entity_ type? |
| <math>t</math> | a time interval | …or the _truth value_ type? |
| <math>v</math> | a value | …or the _event_ type? |

It also lends a sort of iconicity to the system. We can begin to recognize certain combinations of symbols, and think of them as complex glyphs, without being tempted to unpack them into their parts. Finally, abbreviating α → β into the narrower α › β pays off when dealing with lots of nested functions.
