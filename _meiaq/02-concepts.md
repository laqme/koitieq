---
title: "Báq daorıoq róı báq muı"
title_en: "Types and denotations"
chapter: 2
slug: "2"
subject: "the raw ingredients"
---

## The basic types

What are entities (○)? They encompass anything "in the world" about which we might want to make predications, such as me, or your name, or Spain, or the fact that you are reading this textbook. And ◐ is the result of such a predication: true or false.

But these types alone are not enough to model real-life predications, which have truth values that depend on their context: time, the world, the current values of bound pronouns, and so on. Furthermore, we would like to analyze not just statements, but any kind of _speech act_ that a speaker might contribute to the discourse. To this end, there are at least some other "atomic" types that will come up in our analysis of Toaq sentences. Let's take a brief look at all of them.

<ol style="gap:0.5em;display:flex;flex-direction:column;">
<li>✲ is the type of <em>events</em>. An event is an <em>instance</em> of something being the case in some world, at some time.</li>
<li>〜 is the type of <em>possible worlds</em>. We rarely deal with 〜 on its own: instead, a squiggly underline indicates a function from possible worlds to the type it's under. For example, <span class=int>○</span> is short for <div class="kuna-math-container">〜 › ○</div>. Later, we'll learn why this pattern is so common, and what roles it plays in our semantics.</li>
<li>🕔 is the type of <em>time intervals</em>. Really, they are just <em>sets</em> of points in time, and they need not be contiguous like a real interval. They are used to describe or bound when an event happens, and as such they'll come up when we dig into the semantics of tenses.</li>
<li>! is the type of <em>speech acts</em>. For example: a declaration, a question, a wish. This is the type of Toaq sentences: Kuna describes which speech act a sentence amounts to.</li>
</ol>


<details class="aside semantics" markdown="1">
<summary>Metalanguage</summary>
If entities encompass anything in the world, why don't they encompass events or time intervals? Why isn't everything type ○?

There are, in fact, entities corresponding to such things. When we talk about _ké jıaq_{:.t} or _ké hora_{:.t}, they are entities just as _ké kune_{:.t} and _ké sıo_{:.t} are. The distinction is rather made in the **metalanguage**; the symbolic language we are describing right now, which Kuna uses to talk _about_ Toaq. So ○ refers to any such things as described _in Toaq_, where they can be subjects and objects and referents of pronouns, and 🕔 refers to time intervals _only_ in the context of describing the underlying behavior of tenses for Kuna to understand and manipulate.

Making the distinction between ○ and other types helps the semantics be "type-directed" without confusing the language for the metalanguage. It also keeps us from running into issues when denoting things like "this sentence is false".

</details>

## Operators

Kuna inherits the following standard notation for operators from mathematical logic.

| Symbol | Description |
| :---: | --- |
| 𝑒 : ✲ | 𝑒 has type ✲ |
| ∃𝑥 𝑃 | there exists x such that P |
| ∀𝑥 𝑃 | for all x, P |
| ∧ | and |
| ∨ | or |
| ¬ | not |
| → | implies |
| ↔ | if and only if |

Additionally, ≺ is the "amongness" relation on pluralities, and we like to write function application without parentheses: 𝑓 𝑔 ℎ ∧ 𝑥 𝑦 means (𝑓(𝑔))(ℎ) ∧ 𝑥(𝑦).

In this text, we'll use 𝑥 := 𝑦 to mean: 𝑥 is defined as being equal to 𝑦.

## Notation for values

We will stick to certain sets of letters when naming members of these basic types. Here are our picks:

| Type | Letter | Description |
| :-: | --- | --- |
| ○ | 𝑎, 𝑏, 𝑐… | Entities |
| ◐ | 𝑃, 𝑄, 𝑅… | Truth values |
| ✲ | 𝑒, 𝑒¹, 𝑒²… | Events |
| 〜 | 𝑤, 𝑤¹, 𝑤²… | Worlds |
| 🕔 | 𝑡, 𝑡¹, 𝑡²… | Times |

To describe functions without giving them a name, we will use "lambda function" notation: λ𝑥 𝐸 is a function mapping 𝑥 to 𝐸. Here, 𝐸 is some expression that may refer to the input variable 𝑥. So the following definitions are equivalent:

<blockquote>𝑓(𝑥) := <b>red</b>(x) ∧ <b>sweater</b>(x)<br>𝑓 := λx&nbsp; <b>red</b> x ∧ <b>sweater</b> x</blockquote>

## Denotation

We say that Toaq words or phrases **denote**, or simply "stand for", certain formulas. When describing Toaq's semantics, or Kuna's implementation, we will often use "denotation brackets" ⟦…⟧ to show this relationship between Toaq words or phrases and expressions in our mathematical language.

For example, the simplest stab at the meaning of _rú_{:.t} looks something like this:

> ⟦_rú_{:.t}⟧ = λ𝑃 λ𝑄  𝑄 ∧ 𝑃

We can also use denotation brackets in the middle of an expression, to portray a halfway-denoted phrase whose further meaning depends only on the meaning of its smaller parts.

> ⟦_rú ruqshua_{:.t}⟧ = λ𝑄  𝑄 ∧ ⟦<i class=t>ruqshua</i>⟧

The denotation of many lexemes will just be a constant "lexical function" that shares its name. Don't confuse the Toaq word _zuche_{:.t}, which is a verb, is five letters long, et cetera, with the function **zuche** of type <span class=int>○ › ✲ › ◐</span> that produces **true** exactly when its arguments describe a being-a-linguist event:

> ⟦_zuche_{:.t}⟧ = **zuche**<br>
> <span style="display:inline-flex;width:3.6em"></span> = λ𝑤 λ𝑎 λ𝑒&nbsp; **zuche** 𝑤 𝑎 𝑒

(In time, we'll get around to discussing why it takes these arguments in this order.)
