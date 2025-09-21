---
title: "Sá poaqse po Tóaqzu"
title_en: "A fragment of Toaq"
chapter: 4
slug: "4"
subject: "starting small"
---

## Starting small

To recap: Kuna is built on the idea that meaning is _compositional_, and we derive the meaning of a sentence by successively combining the meanings of all the words in it.

To get started studying this phenomenon, we'll imagine a simple fragment of Toaq (let's call it _Póaqzu_{:.t}) where all the sentences are of the form "tense, verb, proper noun, speech act particle."

> _Jıa suaq Mía nha._{:.t}<br>
> _Naı dom Pícarıaq da._{:.t}<br>
> _Pu puagı Tóaqchaq ꝡeı._{:.t}

They all have this syntax tree:

<figure>
  <div class="tree" style="margin-right:-100px">
    <div><i class=t>jıa suaq Mía nha</i><br>SAP</div>
    <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
      <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
      <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
    </svg>
    <div class="tree-children">

        <div class="tree">
          <div><i class=t>jıa suaq Mía</i><br>TP</div>
            <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
              <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
              <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
            </svg>
            <div class="tree-children">
              <div><i class=t>jıa</i><br>T</div>
              <div class="tree">
          <div><i class=t>suaq Mía</i><br>VP</div>
            <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
              <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
              <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
            </svg>
            <div class="tree-children">
              <div><i class=t>suaq</i><br>V</div>
              <div><i class=t>Mía</i><br>N</div>
            </div>
        </div>
            </div>
        </div>
      <div><i class=t>nha</i><br>SA</div>
    </div>

  </div>
</figure>

Here, SA means "speech act", T means "tense", V means "verb", and N means "noun". The corresponding labels ending in P mean "... phrase."

## Types in Póaqzu

What are the _types_ of the denotations of all the constituents (subtrees) in this tree?

From our discussion of intension in the last chapter, We know that _Mía_{:.t} denotes an intensional entity <span class=int>○</span>, and _jıa suaq Mía_{:.t} an intensional truth value <span class=int>◐</span>. We also know that an SAP, a "speech act phrase", is supposed to denote a speech act (&nbsp;!&nbsp;), and we want the verb-and-noun to denote an _event predicate_.

We can summarize this data in the following table:

| Label | Text | Denotation | Type |
| ----- | --- | --- | --- |
| SAP | _Jıa suaq Mía nha._{:.t} | speech act | &nbsp;!&nbsp; |
| TP | _jıa suaq Mía_{:.t} | proposition | <span class=int>◐</span> |
| VP | _suaq Mía_{:.t} | event predicate | <span class=int>✲ › ◐</span> |
| N | _Mía_{:.t} | noun | <span class=int>○</span> |

### Deriving the other types

As described in chapter 1, we'd like to use _function application_ to combine our meanings as we go up the tree. This means we can use the following strategy to help us get an idea of what types the remaining words should have.

> If 𝑋 : α combines with 𝑌 to form 𝑍 : β, then 𝑌 might have a type like α › β.

(In other words: if we want _type-driven compositionality_, then while designing or discovering our semantics, we adopt compositionality-driven types.) Here's an example:

<figure>
  <div class="tree">
    <div><i class=t>jıa suaq Mía nha</i><br>!</div>
    <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
      <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
      <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
    </svg>
    <div class="tree-children">
      <div><i class=t>jıa suaq Mía</i><br><span class=int>◐</span></div>
      <div><i class=t>nha</i><br><span style="background:#fed;margin:-0.2em -1em;padding:0.2em 1em;"><span class=int>◐</span> › &nbsp;!&nbsp;</span></div>
    </div>
  </div>
</figure>

Indeed, it makes intuitive sense for ⟦_nha_{:.t}⟧ to be a function that turns a _proposition_ into a _promise_.

The derivation of the other remaining types is similar:

| Label | Text | Denotation | Type |
| V | _suaq_{:.t} | verb | <span class=int>○</span> &nbsp;›&nbsp; <span class=int>✲ › ◐</span> |
| T | _jıa_{:.t} | tense | <span class=int>✲ › ◐</span> &nbsp;›&nbsp; <span class=int>◐</span> |
| SA | _nha_{:.t} | speech act maker | <span class=int>◐</span> › &nbsp;!&nbsp; |

⟦_suaq_{:.t}⟧ turns a _noun_ 𝑁 into an _event predicate_ describing 𝑁-singing-events. And ⟦_jıa_{:.t}⟧ turns an _event predicate_ 𝑄 into a _proposition_, which claims some future event satisfies 𝑄.

(Both of these descriptions paper over intensionality: there's actually some "λ𝑤" and "in 𝑤" involved.)

## A denoted tree

Now we can denote the entire tree, writing a formula that has the right type at each node.

<figure>
  <div class="tree" style="margin-right:-100px">
    <div><i class=t>jıa suaq Mía nha</i><br>
      <span class=den><b>nha</b>(λ𝑤&nbsp; Mía will sing in 𝑤)</span><br>!</div>
    <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
      <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
      <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
    </svg>
    <div class="tree-children">
      <div class="tree">
        <div><i class=t>jıa suaq Mía</i><br><span class=den>λ𝑤&nbsp; Mía will sing in 𝑤</span><br><span class=int>◐</span></div>
        <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
          <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
          <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
        </svg>
        <div class="tree-children">
          <div><i class=t>jıa</i><br><span class=den>λ𝑃 λ𝑤&nbsp; ∃𝑒: 𝑃 𝑤 𝑒 ∧ future(𝑒)</span><br><span class=int>✲ › ◐</span> &nbsp;›&nbsp; <span class=int>◐</span></div>
          <div class="tree">
                  <div><i class=t>suaq Mía</i><br><span class=den>λ𝑤 λ𝑒&nbsp; 𝑒 is a <br>Mía<sub>𝑤</sub>-singing-event in 𝑤</span><br><span class=int>✲ › ◐</span></div>
                  <svg width="200" height="40" viewBox="0 0 200 40" style="display:block; margin: 0 auto;">
                    <line x1="100" y1="2" x2="10" y2="38" stroke="currentColor" stroke-width="1"/>
                    <line x1="100" y1="2" x2="190" y2="38" stroke="currentColor" stroke-width="1"/>
                  </svg>
                  <div class="tree-children">
                    <div><i class=t>suaq</i><br><span class=den>λ𝑎 (λ𝑤 λ𝑒&nbsp; 𝑒 is an<br>𝑎(𝑤)-singing-event in 𝑤)</span><br><span class=int>○</span> &nbsp;›&nbsp; <span class=int>✲ › ◐</span></div>
                    <div><i class=t>Mía</i><br><span class=den>λ𝑤&nbsp; Mía<sub>𝑤</sub></span><br><span class=int>○</span></div>
                  </div>
                </div>
        </div>
      </div>
      <div><i class=t>nha</i><br><span class=den><b>nha</b></span><br><span class=int>◐</span> › &nbsp;!&nbsp;</div>
    </div>
  </div>
</figure>

You can verify that each formula is the result of applying one of the two child formulas to the other and simplifying the resulting expression through substitution. For example:

> &nbsp;&nbsp; ⟦_suaq Mía_{:.t}⟧
>
> = ⟦_suaq_{:.t}⟧ ⟦_Mía_{:.t}⟧
>
> = <span style="display:inline-block">[λ𝑎 (λ𝑤 λ𝑒  𝑒 is an 𝑎(𝑤)-singing-event in 𝑤)]</span>&ensp;<span style="display:inline-block;background:#eef;padding:0 4px">\[λ𝑤&nbsp; Mía<sub>𝑤</sub>\]</span>
>
> = <span style="display:inline-block">(λ𝑤 λ𝑒  𝑒 is a <span style="display:inline-block;background:#eef;padding:0 4px;">\[λ𝑤&nbsp; Mía<sub>𝑤</sub>\]</span>(𝑤)-singing-event in 𝑤)</span>
>
> = <span style="display:inline-block">(λ𝑤 λ𝑒  𝑒 is a Mía<sub>𝑤</sub>-singing-event in 𝑤)</span>

## Looking forward

Hooray! We've denoted a sentence of Póaqzu. Importantly, if we change just one word of the sentence, we can see how changing the denotation of the _leaf_ has a ripple effect on the denotation of the whole sentence. (Try drawing your own tree for _Jıa marao Mía nha_{:.t}, for example.)

Of course, we've made loads of simplifications. For the rest of the guide, we will undo them, until our little Póaqzu catches up with Toaq itself.