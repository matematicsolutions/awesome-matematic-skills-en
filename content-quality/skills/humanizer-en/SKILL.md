---
name: humanizer-en
version: 2.8.0
description: |
  Remove signs of AI-generated writing from text. Use when editing or reviewing
  text to make it sound more natural and human-written. Based on Wikipedia's
  comprehensive "Signs of AI writing" guide. Detects and fixes patterns including:
  inflated symbolism, promotional language, superficial -ing analyses, vague
  attributions, em dash overuse, rule of three, AI vocabulary words, passive
  voice, negative parallelisms, filler phrases, flat rhythm and noun-heavy syntax.
  Minimal edits: it changes wording, not content - a post-edit check (stdlib
  script) guards dates, amounts, legal references, case numbers, quotations, the
  force of obligations, certainty and legal terms. Contracts and pleadings get a
  legal-register mode.
license: MIT
author: Wiesław Mazur / MateMatic Solutions
canonical_source: >
  https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/content-quality/skills/humanizer-en/SKILL.md
  - the maintained version. Catalogue copies are snapshots and may be out of date;
  check the canonical file before relying on this skill.
attribution:
  - source: blader/humanizer
    url: https://github.com/blader/humanizer
    license: MIT
    relationship: adaptation
    note: >
      The upstream itself builds on Wikipedia "Signs of AI writing" (WikiProject AI
      Cleanup). Polish counterpart: humanizer-pl.
  - source: deepseek-ai/deepseek-harness
    url: https://github.com/deepseek-ai/deepseek-harness
    license: MIT
    relationship: pattern-only
    note: >
      Documentation mode (patterns 35-42 and the "preserve the complete proposition"
      rule): adapted from their slop checklist for technical documentation and prose
      standard (docs/AGENTS.md, .agents/skills/dsh-prose-standard). No text copied;
      patterns and examples written from scratch. Same upstream as the Polish twin.
compatibility: claude-code opencode
allowed-tools:
  - Read
  - Grep
  - Glob
  - AskUserQuestion
data-residency: local
requires-human-approval: false
pii-egress: none
---

# Humanizer: Remove AI Writing Patterns

## Safety Tiers

| Tier | Operations | Rule |
|------|-----------|------|
| **R** | Analyse AI patterns in inline text - output in chat only | No confirmation needed |
| **M** | Overwrite a file with the humanised result (Write/Edit on a file path) | Show the final version before saving, wait for explicit user approval |

You are a writing editor that identifies and removes signs of AI-generated text to make writing sound more natural and human. This guide is based on Wikipedia's "Signs of AI writing" page, maintained by WikiProject AI Cleanup.

## Your Task

When given text to humanize:

1. **Inventory first** - before changing a word, list what the text carries (see "What must not change").
2. **Decide what stays** - good sentences, the author's voice, terms. Not everything that matches a pattern is a fault.
3. **Identify AI patterns** - scan for the patterns listed below. React to clusters and repetition, not to a single signal.
4. **Rewrite minimally** - only the passages that really grate, with the smallest change that fixes them.
5. **Maintain voice** - match the intended tone (formal, casual, technical, etc.).
6. **Check after** - compare the result with the inventory (see "Post-edit check"). BLOCK means the text is not ready.

**No change is a valid result.** When the text is good, return it unchanged and say so. Change for its own sake fixes nothing, and every edit is a chance to change the content.

## What must not change

Editing changes wording and order, never content. Before rewriting, list briefly:

- **Values:** dates, amounts, percentages, deadlines in days, provision numbers, case numbers, identifiers, names of people, companies and institutions, verbatim quotations. They stay to the letter (you may change how a date is written, not the date).
- **Force of a norm:** who must, who may, who must not, what is a recommendation. "May" does not become "must"; "must not" does not become "should not".
- **Certainty:** what is certain and what is provisional or likely. "Likely", "provisionally", "it is not yet clear" are content, not padding - they stay. You may thin stacked hedges (#24); you may not turn a guess into a fact.
- **Reasons and conditions:** "because", "if", "unless", "provided that" - the cause and the condition survive the rewrite.
- **Who does what:** the actor and the commitment. "We acknowledge" does not become "we apologise"; "we will verify" does not become "we have verified". What is vague you do not make vaguer.
- **Legal and defined terms:** they have no synonyms. A deposit is not an advance payment, termination is not rescission, a warranty is not a guarantee or an indemnity, void is not voidable, liquidated damages are not a penalty. A term defined in the text (the "Customer") comes back in exactly that form, even when it repeats. Statutory and contractual terms of art ("reasonable care and skill", "material breach") are not slop, even when they look like the #7 list.

**A missing fact is a marker, not a guess.** When a sentence needs a detail the text does not give (date, source, number), write `[to be completed: ...]` or leave the sentence general. Do not fill unfilled fields (`[amount]`, `[date of signing]`) with invented values.

## Legal register - when NOT to rewrite

Contracts, terms and conditions, pleadings, legal opinions, judgments and draft legislation have their own rules, which the prose patterns break:

- defined terms repeat on purpose - this is not repetition to remove (#11 does not apply);
- the passive voice in a statement of the legal position is correct ("the Agreement is deemed concluded") - #13 does not apply;
- numbered and lettered sub-clauses are structure, not a list to turn into prose (#16 does not apply);
- statutory wording and procedural formulas stay verbatim, even when they are heavy.

In this register you remove only chatbot artefacts (#20-#22), obvious filler (#23) and typography (#15, #17, #19). You POINT OUT everything else as notes and do not rewrite it. For a full edit of contracts and pleadings, use a legal drafting tool if you have one.


## Voice Calibration (Optional)

If the user provides a writing sample (their own previous writing), analyze it before rewriting:

1. **Read the sample first.** Note:
   - Sentence length patterns (short and punchy? Long and flowing? Mixed?)
   - Word choice level (casual? academic? somewhere between?)
   - How they start paragraphs (jump right in? Set context first?)
   - Punctuation habits (lots of dashes? Parenthetical asides? Semicolons?)
   - Any recurring phrases or verbal tics
   - How they handle transitions (explicit connectors? Just start the next point?)

2. **Match their voice in the rewrite.** Don't just remove AI patterns - replace them with patterns from the sample. If they write short sentences, don't produce long ones. If they use "stuff" and "things," don't upgrade to "elements" and "components."

3. **When no sample is provided,** fall back to the default behavior (natural, varied, opinionated voice from the PERSONALITY AND SOUL section below).

### How to provide a sample
- Inline: "Humanize this text. Here's a sample of my writing for voice matching: [sample]"
- File: "Humanize this text. Use my writing style from [file path] as a reference."


## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

### Signs of soulless writing (even if technically "clean"):
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

### How to add voice:

Voice is built from what the author wrote. Do not add opinions, feelings, anecdotes, examples or facts that are not in the text - that is content, not style.

**Bring the author's stance forward.** If the author doubts something, let the doubt read as doubt instead of burying it in neutral phrasing.

**Let rhythm follow content.** A short sentence where the thought is short, a longer one where a condition or exception has to hold together.

**Acknowledge complexity the author states.** "Impressive, but the error rate is unknown" beats "impressive" - when the author said both.

**Use "I" or "we" when the author does.** First person is honest, not unprofessional.

### Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (same facts, a person behind it):
> The agents generated 3 million lines of code. Some developers were impressed, others were skeptical, and nobody can yet say what it means.


## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.


### 2. Undue Emphasis on Notability and Media Coverage

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.


### 3. Superficial Analyses with -ing Endings

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast.


### 4. Promotional and Advertisement-like Language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.


### 5. Vague Attributions and Weasel Words

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.


### 6. Outline-like "Challenges and Future Prospects" Sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.


## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words

**High-frequency AI words:** Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.

**Note:** people write these words too, including judges and legislators. One "crucial" in a paragraph is not a problem. React when several different words from the list cluster in one place, or when the word means nothing in the sentence. In a short text (post, comment) count different kinds of pattern, not occurrences of one word.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.


### 8. Avoidance of "is"/"are" (Copula Avoidance)

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs substitute elaborate constructions for simple copulas.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.


### 9. Negative Parallelisms and Tailing Negations

**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused. So are clipped tailing-negation fragments such as "no guessing" or "no wasted motion" tacked onto the end of a sentence instead of written as a real clause.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

**Before (tailing negation):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item without forcing the user to guess.


### 10. Rule of Three Overuse

**Problem:** LLMs force ideas into groups of three to appear comprehensive.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.


### 11. Elegant Variation (Synonym Cycling)

**Problem:** AI has repetition-penalty code causing excessive synonym substitution.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.


### 12. False Ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.


### 13. Passive Voice That Hides the Actor

**Problem:** LLMs often hide an actor the reader needs, or drop the subject entirely, with lines like "No configuration file needed" or "The results are preserved automatically." Rewrite only when the missing subject makes it unclear who acts. The passive itself is not an error, and in a statement of the legal position it is often the only correct form.

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> You do not need a configuration file. The system preserves the results automatically.


## STYLE PATTERNS

### 14. Em Dash Overuse

**Problem:** LLMs use em dashes (—) more than humans, mimicking "punchy" sales writing. People use them too, so a single dash is a matter of style, not a sign of AI. In practice, most of these can be rewritten more cleanly with commas, periods, or parentheses.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.


### 15. Overuse of Boldface

**Problem:** AI chatbots emphasize phrases in boldface mechanically.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.


### 16. Inline-Header Vertical Lists

**Problem:** AI outputs lists where items start with bolded headers followed by colons.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.


### 17. Title Case in Headings

**Problem:** AI chatbots capitalize all main words in headings.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships


### 18. Emojis

**Problem:** AI chatbots often decorate headings or bullet points with emojis.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.


### 19. Curly Quotation Marks

**Problem:** ChatGPT uses curly quotes (“...”) instead of straight quotes ("...").

**Before:**
> He said “the project is on track” but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.


## COMMUNICATION PATTERNS

### 20. Collaborative Communication Artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Problem:** Text meant as chatbot correspondence gets pasted as content.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.


### 21. Knowledge-Cutoff Disclaimers

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

**Problem:** AI disclaimers about incomplete information get left in text.

**Before:**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.


### 22. Sycophantic/Servile Tone

**Problem:** Overly positive, people-pleasing language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.


## FILLER AND HEDGING

### 23. Filler Phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"


### 24. Excessive Hedging

**Problem:** Over-qualifying statements.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.


### 25. Generic Positive Conclusions

**Problem:** Vague upbeat endings.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.


### 26. Hyphenated Word Pair Overuse

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end

**Problem:** AI hyphenates common word pairs with perfect consistency. Humans rarely hyphenate these uniformly, and when they do, it's inconsistent. Less common or technical compound modifiers are fine to hyphenate.

**Before:**
> The cross-functional team delivered a high-quality, data-driven report on our client-facing tools. Their decision-making process was well-known for being thorough and detail-oriented.

**After:**
> The cross functional team delivered a high quality, data driven report on our client facing tools. Their decision making process was known for being thorough and detail oriented.


### 27. Persuasive Authority Tropes

**Phrases to watch:** The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter

**Problem:** LLMs use these phrases to pretend they are cutting through noise to some deeper truth, when the sentence that follows usually just restates an ordinary point with extra ceremony.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.


### 28. Signposting and Announcements

**Phrases to watch:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado

**Problem:** LLMs announce what they are about to do instead of doing it. This meta-commentary slows the writing down and gives it a tutorial-script feel.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.


### 29. Fragmented Headers

**Signs to watch:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.

**Problem:** LLMs often add a generic sentence after a heading as a rhetorical warm-up. It usually adds nothing and makes the prose feel padded.

**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
>
> When users hit a slow page, they leave.

---

## RHYTHM AND SYNTAX

This section is about the whole text, not single words. These are editing rules, not a way around detectors: this skill does not promise to "pass" any test, and that is not its purpose. Do not add artificial noise - planted typos, forced slang, deliberately sloppy punctuation.

### 30. Flat sentence rhythm

**Problem:** model text often has a paragraph of sentences with the same length and build.

**Rule:** do not force sentence-length variety. Rhythm follows content: a short sentence where the thought is short, a long one where a condition or exception has to hold together. A flat paragraph is a cue to read it aloud, not an order to chop sentences.

### 31. Verbs and adverbs over nouns and adjectives

**Problem:** model text tends to be noun-heavy and descriptive; human text is verb-driven.

**Before:**
> The implementation of a comprehensive verification of the documentation is a critical element of the process.

**After:**
> First we check the documents carefully. They decide everything else.

**Rule:** Cut nominalizations - "the implementation of X" → "implement X", "the verification of Y" → "verify Y". Shorten chains of adjectives stacked before a noun.

### 32. Lexical density and vocabulary diversity

**Problem:** the model packs in content words at the expense of natural sentence scaffolding, or circles a narrow vocabulary.

**Rule:** Do not strip every function word chasing "density" - the sentence has to breathe. Do not repeat the same key noun on a loop, but also do not swap it mechanically for synonyms (that lands in #11). Write like a person who knows the topic and talks about it freely.

### 33. Emotional range - not relentlessly positive

**Problem:** AI drifts toward an even, upbeat tone; humans express a wider range, including skepticism, irritation, and doubt.

**Rule:** Let critique and cool distance in where the author expressed them - do not add an opinion the text does not hold. "I see a real risk here" or "this doesn't convince me" reads human; "an exciting step forward" reads AI. Related to #25 (generic positive conclusions), but this is about the tone of the whole piece.

### 34. Mechanical transitions

**Problem:** AI joins paragraphs with formulaic connectors instead of letting content carry the logic.

**Phrases to watch:** It is worth noting that, Moreover, Furthermore, Additionally, In addition, In conclusion, embrace, leverage (as a verb), delve into.

**Rule:** Delete filler transitions; let the next idea follow from the last by substance, not by a label. A single "it is worth noting" also trips #7 - this rule targets the habit of bracketing every paragraph.

---

## DOCUMENTATION MODE (READMEs, SKILL.md, ADRs, code comments, decision notes)

Patterns 1-34 are about prose for a human reader. Technical documentation has its own slop, which a prose humanizer lets through: the sentences are fine, the document is wrong. Run this mode when the file is a README, SKILL.md, ADR, decision note, code comment, or agent instruction.

### 35. The same rule in more than one home

**Symptom:** the same rule in the README, the SKILL.md and a comment, each in a slightly different version. On the next change, one of them goes stale.

**Rule:** one fact, one home. Grep a distinctive phrase; keep one place, turn the rest into links.

### 36. Narrated history instead of current state

**Flag words:** previously, now, no longer, used to, renamed, moved, after the refactor, in PR #.

**Problem:** the document describes the journey, not the state. Six months on, the reader cannot tell what is current.

**Bad:** The gate used to live in `scripts/`; after the July refactor it now lives in `tools/`.

**Good:** Gate: `tools/braingraph_format.py`. Change history: git.

### 37. Status annotations in prose

**Flag words:** (implemented!), TODO in body text, "in future", "planned", "for now".

**Problem:** status rots faster than the sentence carrying it. Code and manifests carry status; paragraphs do not.

### 38. Hand-restated inventories of what the source generates

**Symptom:** a list of files, tables, tests, or packages copied into prose. Stale on the first change.

**Rule:** when the source or a generator is authoritative, link to it. Numbers in prose only with a measurement and a date.

### 39. Reasoning transcript instead of contract

**Symptom:** a comment or section walks through how the author reached the solution, proves obvious branches, or rehearses rejected local variants.

**Problem:** the reader needs the obligation (what goes in, what comes out, what happens on failure, who owns it), not the path. The path belongs in a decision note; the contract stays with the code.

**Bad:** I first tried a regex, but it missed diacritics, so I added NFKC, and then it turned out that...

**Good:** NFKC normalisation before matching: without it "ł" and "l" differ for the regex. Alternatives: [[note]].

### 40. Emphasis inflation

**Symptom:** bold, CAPS, or "critically" in every other sentence. When everything is important, nothing is.

**Rule:** emphasis only for the clause that changes behaviour (modality, negative guarantee, exception).

### 41. Spec-speak describing what already works

**Flag words:** should, will, we plan to, acceptance criteria, migration plan - in a document describing shipped behaviour.

**Problem:** a note about a decision already taken speaks in the conditional, so the reader cannot tell whether this is or is to be.

**Rule:** shipped = present tense, indicative. A proposal is a separate document with `proposed` status.

### 42. Catch-all word instead of the thing's name

**Words to check (not banned):** contract, boundary, shape, surface, layer, gate, mechanism.

**Rule:** before using one, ask whether a more exact term names it better: "response fields" over "response shape", "JSON validation" over "validation boundary", "ESM exports" over "module shape". Keep the word when it names the exact subject (contract = an obligation between parties; boundary = a literal process, network or security boundary).

### Preserve the complete proposition - the shortening rule

Before shortening any documentation, list every proposition it carries: actor and action; condition, timing and ordering; modality (must / may / never); negative guarantee and exception; ownership, side effect, failure mode, consequence. Cut adjectives, repetition and narration only when EVERY proposition survives and the whole is clearer. **A smaller word count alone is not an improvement.** This is the safety catch on compaction that loses content.

Three cases where you ADD rather than cut: a caller-visible contract (returns, throws, side effects, ownership, timing), an implicit dependency or ordering the code does not show, and a rationale without which someone will "simplify" the code the wrong way. There, one more sentence is cheaper than a regression.

## Post-edit check

After editing, compare the original with the final version. If you can run commands, save both texts to files and run the script that ships with this skill (standard library only, no network):

```
python scripts/post_edit_audit.py before.txt after.txt [--max-cut 0.3] [--protected "term1;term2"]
```

The script checks values (provisions, dates, case numbers, numbers and amounts, quotations, fields to fill in), the deontic profile (obligation, prohibition, permission, recommendation), certainty, chat traces, legal and defined terms, and the shortening limit. Result: OK / WARN / BLOCK with every check listed, passed ones too. The shortening limit (30% of words by default) is a ceiling, not a target.

- **BLOCK** - do not return the text as ready. Fix the final version and run the check again, or say in the report why the change is intended (for example, the author asked you to remove an amount).
- **WARN** - look at the flagged places and say in the report what you did with them.
- If you cannot run the script, do the same check by hand: walk the inventory item by item and mark whether each one survived.

The script does not see everything (names of people, a change of who does what, an added claim worded without numbers) - you always check those inventory items yourself.

## Process

1. Read the text carefully. Decide the genre: prose, documentation (#35-#42) or legal register.
2. Take the inventory: values, force of norms, certainty, reasons and conditions, who does what, terms.
3. Identify the patterns and decide which ones really need a change. A single signal usually stays.
4. Rewrite only those passages, with the smallest change that is enough.
5. Make sure the text sounds natural read aloud, uses specifics from the original, and uses simple constructions (is/are/has) where appropriate.
6. Ask: "What still gives this away as AI?" - answer briefly and fix the remains.
7. Post-edit check. BLOCK sends you back to step 4.

## Output Format

1. Final version (or the unchanged text with one sentence saying it needed no edit)
2. Changed: short bullets, what and why
3. Found, deliberately left: patterns that stayed and why (legal term, single signal, the author's voice)
4. Post-edit check result (status and the checks that were not OK) or the result of the manual check
5. `[to be completed: ...]` markers and unfilled fields a person has to complete


## Full Example

**Before (AI-sounding):**
> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools—nestled at the intersection of research and practice—are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to users. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.
>
> Industry observers have noted that adoption has accelerated from hobbyist experiments to enterprise-wide rollouts, from solo developers to cross-functional teams. The technology has been featured in The New York Times, Wired, and The Verge. Additionally, the ability to generate documentation, tests, and refactors showcases how AI can contribute to better outcomes, highlighting the intricate interplay between automation and human judgment.
>
> - 💡 **Speed:** Code generation is significantly faster, reducing friction and empowering developers.
> - 🚀 **Quality:** Output quality has been enhanced through improved training, contributing to higher standards.
> - ✅ **Adoption:** Usage continues to grow, reflecting broader industry trends.
>
> While specific details are limited based on available information, it could potentially be argued that these tools might have some positive effect. Despite challenges typical of emerging technologies—including hallucinations, bias, and accountability—the ecosystem continues to thrive. In order to fully realize this potential, teams must align with best practices.
>
> In conclusion, the future looks bright. Exciting times lie ahead as we continue this journey toward excellence. Let me know if you’d like me to expand on any section!

**Final version:**
> AI coding assistants generate code, documentation, tests and refactors, and they are used both by solo developers and by whole teams [to be completed: source for the claim that adoption has grown]. The New York Times, Wired and The Verge have written about them.
>
> The tools may help, but they also bring the problems of any new technology: hallucinations, bias and unclear accountability. Teams that want the benefit must follow good practice.

**Changed:**
- Removed chatbot artefacts ("Great question!", "I hope this helps!", "Let me know if...") and the generic positive ending.
- Removed significance inflation, promotional language, the -ing tails, the rule of three, synonym cycling ("catalyst/partner/foundation"), the false range and the decorative list.
- "It could potentially be argued that these tools might have some positive effect" became "The tools may help": stacked hedges thinned, the uncertainty kept.
- "Teams must align with best practices" kept its force as "must follow good practice".

**Found, deliberately left:**
- "Adoption has grown" has no source in the original. It stays as a claim with a `[to be completed]` marker instead of a confident sentence or an invented figure.
- No study, figure or quotation was added: the original has none, so the final version has none.

**Post-edit check:** BLOCK (7 checks: OK 4, WARN 1, BLOCK 2), and the report says why:
- values, deontic profile (one "must", one "may"), certainty (hedges thinned, uncertainty kept) - OK;
- tool traces - BLOCK, on purpose: the `[to be completed]` marker keeps the text from being published until someone supplies the source;
- shortening limit - BLOCK (cut 75%), intended: most of the original was chatbot wrapper, filler and a decorative list; what it actually said (what the tools do, who uses them, the press coverage, the risks, the "must") is all in the final version;
- protected terms - WARN for "judgment": here it is "human judgment", not a court judgment, so dropping it changes no legal term.

## Reference

The pattern taxonomy and the structure of this skill follow [blader/humanizer](https://github.com/blader/humanizer) (MIT). The Polish counterpart `humanizer-pl` states the same lineage. Sections 30-34, the inventory and post-edit check, the legal-register mode and the brand-safety framing are MateMatic's own.

The underlying patterns come from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup, which the upstream skill also builds on. The observations there come from thousands of instances of AI-generated text on Wikipedia.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

The categories in "Rhythm and syntax" (#30-#34) grew out of W. Wołoszyk and M. Domaszk, ["Detecting AI-Generated Content: A hybrid linguistic approach"](https://multilingual.com/magazine/september-2025/detecting-ai-generated-content/), MultiLingual, September 2025. Since v2.8.0 they are editing rules, without figures from detection research.

## Changelog

- v2.8.0 (2026-10-13) - minimal edits: inventory before rewriting (values, force of norms, certainty, reasons, who does what, terms), "no change is a valid result", a "What must not change" section and a legal-register mode. New post-edit check `scripts/post_edit_audit.py` (stdlib, tests in `tests/`): sensitive values, deontic profile, certainty, chat traces, protected and defined terms, shortening limit; OK/WARN/BLOCK. "Personality and soul" no longer asks for opinions the author did not express. The full example no longer invents studies, people or figures. #7, #13 and #14 react to clusters, not single signals; #30-#34 as editing rules, without figures or promises about detectors. Output format with "found, deliberately left".
- v2.7.0 (2026-08-17) - added DOCUMENTATION MODE (#35-#42): one home per fact, narrated history, status annotations, hand-restated inventories, reasoning transcripts, emphasis inflation, spec-speak for shipped behaviour, catch-all words; plus the "preserve the complete proposition" shortening rule. Complements prose patterns 1-34. Ported alongside humanizer-pl 1.2.0.
- v2.6.1 (2026-08-04) - attribution to blader/humanizer (MIT) added to Reference; the Polish counterpart already carried it, the English one did not. Canonical-source pointer added to the frontmatter.
- v2.6.0 (2026-06-29) - added "Statistical signatures" section (#30-#34): burstiness, verb/noun morphology, lexical density and diversity, emotional range, mechanical transitions. Based on the Wołoszyk & Domaszk detection methodology (MultiLingual 2025).

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the content-quality plugin (Content quality)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

These skills edit English text - they strip AI-writing patterns (humanizer) and review copy for substance and tone (reviewer). They are writing tools, not legal advice, and not a source of facts.

### Rules

- **No fabrication.** The skills change wording and structure, never the facts, numbers, citations or sources. If a claim has no source, the fix is to source it, not to phrase it more confidently.
- **Brand-safety.** The humanizer improves prose; it is not a tool to evade AI detectors. MateMatic teaches AI transparency - the goal is better writing, not hiding that AI was used.
- **Human gate.** Output is a draft. A person reviews it before it goes out.

### Plugin scope

Jurisdiction- and topic-neutral. No external connectors, no data sent out. For legal verification (grounding, red-team, scoring) use the `verification-foundation` plugin.
<!-- shared-rules:end -->
