---
title: "Báq sıo bẹmuıdıu"
title_en: "Concepts from semantics"
chapter: 3
slug: "3"
subject: "intension, discourse, deixis"
---

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

## Event predicates

A final concept we should get comfortable with before stepping into the next chapter is the idea of an _event predicate_. Conceptually, this is a predicate that describes what kind of event something is, without yet situating it in time.

A sentence like _Jıa suaq Mía nha_{:.t} promises the existence of a _Mía-singing-event_ in the future. In this case, the _event predicate_ is a function that has type <span class=int>✲&nbsp;›&nbsp;◐</span> and describes the event involved:

> ⟦_suaq Mía_{:.t}⟧ = λ𝑤 λ𝑒&nbsp; 𝑒 is a Mía-singing-event in 𝑤

It, too is intensional (depends on the world variable): this is what lets us tie events to a possible world that they might or might not happen in.

The essential structure of any Toaq clause is that the verb-plus-nouns describe an _event predicate_, which is then modified by the aspect, tense, and complementizer nodes to describe a _proposition_.

<figure style="margin: 2em 0;display:flex; align-items: center; gap: 1em; justify-content: center; text-align: center;">
  <div><i class=t>suaq Mía</i><br><span class=int>✲&nbsp;›&nbsp;◐</span></div>
  <div style="font-size: 80%;" class="arrow-underline">aspect, tense, complementizer</div>
  <div><i class=t>ꝡa jıa tam suaq Mía</i><br><span class=int>◐</span></div>
</figure>
