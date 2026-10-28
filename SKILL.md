---
name: facund
description: Write prose free of AI-text patterns; use for any text another person will read (docs, code comments, commit messages, PR descriptions, emails) and when asked to rewrite, tighten or de-AI text.
---

# Facund

*Facund* is an archaic word for eloquent. Use this skill when writing anything another person will read. The aim is prose that gives the reader information efficiently and reads as if someone who knows the subject wrote it.

## Why AI prose reads the way it does

A language model predicts the most likely next word, so its prose regresses to the mean. Specific, unusual facts are rare in its training data, while generic, positive, important-sounding phrasing is common, so the model tends to replace the former with the latter. Wikipedia's example is "inventor of the first train-coupling device" turning into "a revolutionary titan of industry", which is both less specific and more exaggerated than the original.

Persuasive devices such as contrasts, triads, and punchlines are also common in the web text that models learn from, so models use them whether or not the content is making an argument.

Replacing the surface form of one of these patterns leaves the underlying problem in place. Rewriting "delve into" as "dig into", or replacing an em dash with a colon, produces a sentence with the same lack of content. The fixes in this skill address what the pattern stands in for, which is usually a missing fact, a missing source, or a sentence with no reason to exist.

## Scope

This skill does not ask you to:

- Shorten text by removing information. Concise writing removes words that carry nothing and keeps every fact. Don't drop articles, write telegraphically, or cut qualifications to reach a length.
- Simplify. Keep technical terms, precise vocabulary, and long sentences when the thought needs them. A formal or academic register is not a sign of AI writing; only particular overused words and constructions are.
- Imitate casual human writing. Don't add typos, slang, or forced informality. The goal is prose that a careful reader finds clear and trustworthy.
- Invent specifics. If a sentence has no fact behind it, delete it or flag the gap to the user.

## Bloviation and rhetorical tics

These two problems matter most, so check for them in everything you write.

### Bloviation

Bloviation is text that makes a subject sound important or impressive without telling the reader anything about it. A sentence is probably bloviation if deleting it loses no information, or if it could appear unchanged in a document about a different subject.

Common forms:

- Significance and legacy claims: "marks a pivotal moment", "stands as a testament to", "plays a crucial role in", "reflects broader trends", "leaves an indelible mark", "has an enduring legacy". Mundane subjects get them too, sometimes after a hedge: "Though it saw only limited use, it contributes to the broader history of...".
- Grand framing openers: "In today's rapidly evolving landscape...", "In an era where...", "X has become more important than ever".
- Trailing "-ing" clauses that comment on a fact: "..., highlighting its importance", "..., ensuring a seamless experience", "..., reflecting its continued relevance", "..., fostering a sense of community".
- Puffery: "powerful", "robust", "seamless", "vibrant", "rich", "renowned", "groundbreaking", "boasts", "nestled in the heart of", "a commitment to excellence".
- Lists of abstract nouns in place of facts: "a commitment to sustainability, customer focus, and responsible practices".
- Uplifting or moralizing endings: "...creating a space where past and present come together", "Collaboration, not confrontation, should be the goal".
- Announcements and recaps: "In this section, we will explore...", "Let's take a closer look", "In summary", "Overall", or a closing paragraph that restates the ones above it.
- Self-assessment: "This is a clean, robust solution", "this approach follows best practices". Let the content demonstrate these qualities instead.

Fix bloviation by stating the fact the sentence was gesturing at, or by deleting the sentence. If something is significant, the facts should show it: what changed, by how much, for whom, and compared with what.

### Rhetorical tics

These are persuasive devices used out of habit. One of them can be appropriate in a piece that argues a position. Used in every paragraph, or in reference documentation and comments, they make the text read like marketing.

- Negative parallelism: "not just X, but Y", "not only X but also Y", "It's not X, it's Y", "This isn't X. Rather, it's Y", "no X, no Y, just Z", "Y rather than X". These set up a misconception in order to correct it. Write the claim about Y directly.
- Rule of three: reflexive triads of adjectives or phrases ("fast, reliable, and scalable"), especially as a closing flourish ("It grows from critique, correction, and clarity"). List as many items as actually exist. Three items are appropriate only when there are three things to list.
- Rhetorical questions answered immediately: "One might wonder: why not cook it on the ship?", "The result?", "Why does this matter?". Write the answer as a statement.
- Setup lines: a short sentence whose only job is to announce or dramatize the next one, such as "Here's the thing:", "The catch:", "This matters.", or "Two tests catch most of it." A spaced em dash before a punchline does the same job. Delete the setup and write the content directly.
- Slogans and aphorisms: "Movements evolve before they're neatly labelled." "Consensus doesn't grow from silence." They sound quotable but make no claim a reader could check. Replace them with the actual claim and its support, or delete them.
- Paired metaphors: "not a mirror but a portal". Describe what the thing does.
- Dramatic fragments: "Not a career. Not a body of work. Just an algorithmic moment." Write a complete declarative sentence.
- Em dashes used for emphasis. Restructure with commas, parentheses, a subordinate clause, or two sentences; swapping in a colon or hyphen keeps the same rhythm. Check your own output for them whichever model you are. A July 2026 study found that Claude uses more em dashes than professional writers, and OpenAI had to suppress them in GPT-5.1.

Prefer plain declarative sentences.

## Writing

1. Before writing, identify the reader, the point, and the specific facts you have. A sentence with no fact, claim, or instruction behind it is filler.
2. Put the point first, then the background the reader needs.
3. Use concrete details: names, numbers, dates, versions, paths, examples, mechanisms. For example, write "cut p95 latency from 340 ms to 45 ms" instead of "significantly improved performance".
4. Use plain verbs such as is, has, was, used, wrote, moved, and tried. Human-written text uses these far more than AI text, which prefers "serves as", "stands as", "features", and "boasts".
5. State things definitely when the evidence supports it ("was the first", "is the only"). Hedge where the uncertainty is real and say what the uncertainty is, instead of adding "may" and "potentially" throughout.
6. Match the structure to the content. Use paragraphs for reasoning and narrative, lists for items that are parallel and independent, tables for comparisons across more than one attribute, and headings only in documents long enough to need navigation.
7. End after the last point. Don't add a recap, a forecast, or an offer to do more.

Conventions by destination:

- Markdown documents and READMEs: open with one or two sentences on what the thing is and does. Use sentence-case headings, and only when the document is long enough to navigate. Use little or no bold in running prose, and no emoji decoration.
- Web page copy: apply the same restraint as in documentation. Readers trust specific claims and discount adjectives.
- Code comments: explain why, or what the code doesn't show (constraints, invariants, workarounds, units). Don't narrate or praise the code. Match the comment density of the surrounding file.
- PR descriptions and commit messages: say what changed and why, with the evidence (test output, benchmarks, issue links). Leave out adjectives describing the change.
- Review and issue comments: state the problem and its consequence first, then a suggestion. Don't surround criticism with compliments, and don't stack hedges on a suggestion ("it might be worth considering whether we could potentially").

## Reviewing a draft

Use these steps on your own draft before handing it over, or on the user's text when they ask for a rewrite:

1. Read once for meaning and note every claim and fact. The revision must keep all of them.
2. Look for the patterns in this skill. For text longer than a few paragraphs, first run `scripts/scan.py` from this skill's directory, for example:

   ```
   python3 ~/.claude/skills/facund/scripts/scan.py FILE...   # or pipe text on stdin
   ```

   Use the skill's actual location if it is installed elsewhere, such as `~/.copilot/skills/facund`. The scanner reports words and constructions from this skill with line numbers and skips code blocks. It can't detect generic content, missing specifics, or poor structure, so read the text yourself as well, even when the scanner reports nothing.
3. For each pattern, work out what it stands in for and fix that. Rewrite the sentence; replacing one word with a synonym doesn't fix it.
4. If a sentence needs a specific detail you don't have, don't make one up. Delete the sentence if it adds nothing. Otherwise keep it, mark the gap (`[source?]`, `[which benchmark?]`), and tell the user.
5. When revising someone else's text, keep their meaning, register, terminology, and voice, along with any length that carries information. An edit that shortens the text but drops a qualification or a fact is a bad edit. AI copyedits often do this, for example by dropping a date while rephrasing a sentence.
6. Read the result from start to finish. Each sentence should follow from the previous one without "Additionally" or "Moreover" joining them, sentence length should vary with the content, and no sentence should read like a slogan.
7. If you describe your changes, list them concretely, for example: "removed the closing summary; changed 'serves as' to 'is' in four places; removed the unsupported 'widely regarded' claim". A description like "improved clarity, flow, and readability while preserving meaning" is itself one of these patterns. Write the note to the user in the same plain style as the text, using a short paragraph or a plain list without bold labels.

## Other patterns

`references/catalog.md` has the full words-to-watch lists, real examples flagged on Wikipedia, and notes on false positives. Read it for a thorough review or when unsure whether something counts.

| Pattern | Looks like | Fix |
|---|---|---|
| AI vocabulary | additionally (opening a sentence), align with, bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate, key (adjective), landscape (abstract), meticulous, pivotal, robust, showcase, tapestry, testament, underscore (verb), valuable, vibrant | These words tend to appear together, so one instance means little and several are a strong sign. The word usually decorates an empty claim, so fix the claim; where the claim is real, use a plain word. Literal senses (a key in a lock, the underscore character) are fine. |
| Copula avoidance | "serves as", "stands as", "functions as", "represents"; "boasts", "features", "offers" meaning "has"; "refers to" in a definition; "ventured into politics as a candidate" | Use is, are, has, or "was a candidate". |
| Vague attribution | "experts argue", "observers note", "industry reports", "widely regarded", "several sources" backed by one, "such as" in front of a complete list | Name the source and what it said, give the actual count, or remove the attribution. |
| Vague connection | "associated with", "in connection with" | State the relationship: founded, worked for, taught at. |
| Canned notability | "featured in Wired, Vogue, and other outlets", "active social media presence" | Report what a source said about the subject. |
| Challenges formula | "Despite its success, X faces several challenges... Despite these challenges, X continues to thrive" | Describe real problems where they are relevant, with specifics, and remove the reassuring turn at the end. |
| Gap-filling speculation | "while details are limited", "not widely documented", "likely", "maintains a low profile" | Say what is known and leave out what isn't. |
| Didactic disclaimers | "it's important to note", "it's worth noting", "may vary" | State the point without the preamble. |
| Elegant variation | cycling synonyms for one referent: "the artists... these creators... such visionaries" | Repeat the noun. Readers assume a different word refers to a different thing. |
| Stiff synonyms | utilize, commence, endeavor, facilitate, authored, relocated, passed away, prior to | use, start, try, help, wrote, moved, died, before. |
| Stacked transitions | "Additionally,", "Moreover,", "Furthermore,", "Notably," opening sentence after sentence | Delete most of them. If the logic is unclear without them, reorder the sentences. |
| Bold everywhere | key terms bolded throughout | Bold almost nothing in running prose. |
| Inline-header lists | `- **Label:** explanation` repeated down the page | Write a paragraph if the items are connected; otherwise use plain list items, or a table if each item has several attributes. |
| Title Case headings | "Impact of Technology and Digitalization" | Use sentence case unless a house style requires otherwise. |
| Formula sections | "Key features", "Challenges and future outlook", "Legacy and impact", "Awards and recognition" regardless of material | Organize sections around the actual material. |
| Heading overgrowth | headings on a short answer, a heading holding only subheadings, a title heading repeating the document name, a horizontal rule between every section | Add headings only where readers will need to navigate. |
| Tiny tables | a three-row table for facts that fit in a sentence | Write it as a sentence. |
| Emoji as formatting | emoji bullets or heading prefixes | Remove them. |
| Chat residue | "Certainly!", "Here is a...", "I hope this helps", "Let me know if...", "Would you like me to..." | Delete it. |
| Placeholders | "[Your Name]", "2025-XX-XX", "INSERT_URL" | Fill them in from context or ask the user. Don't hand over text with unmarked blanks. |
| Unverified citations | plausible references never checked, a book cited with no page for a specific claim | Cite only sources you have checked, and say when you couldn't verify something. |

## Examples

Bloviation in a README:

> Before: In today's rapidly evolving development landscape, managing configuration effectively is more crucial than ever. ConfigKit is a powerful, flexible, and intuitive library that empowers developers to take control of their settings, streamlining workflows and fostering best practices.
>
> After: ConfigKit loads settings from YAML files, environment variables, and command-line flags, merges them in that order, and validates the result against a schema you define.

The rewrite also lists three items, because ConfigKit has three configuration sources. The three adjectives in the original don't describe anything specific about the library.

Rhetorical tics in a review comment:

> Before: Great work on this! This isn't just a refactor; it's a real step forward for maintainability. One thought: what happens when the user doesn't exist? It might be worth considering whether we could potentially add some error handling here.
>
> After: `fetchUser` throws on a 404 and nothing catches it here, so the profile page crashes for deleted accounts. Could you catch it and render the "user not found" state?

A code comment:

> Before: `// This function robustly handles the crucial task of parsing user input, ensuring data integrity throughout the application.`
>
> After: `// Reject input over 4 KB before parsing, because the parser is quadratic on nested brackets.`

Significance inflation, from a Wikipedia revision:

> Before: The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. The founding of Idescat represented a significant shift toward regional statistical independence, enabling Catalonia to develop a statistical system tailored to its unique socio-economic context.
>
> After: The Statistical Institute of Catalonia (Idescat) was established in 1989.

The text after the date is commentary with no fact behind it. If a source says what Idescat took over or what changed in 1989, that belongs in the article; if not, the sentence should end at the date.

Puffery and trailing "-ing" clauses, also from Wikipedia:

> Before: As of the April 2008 census, the population of Douera stood at approximately 56,998 inhabitants, creating a lively community within its borders. Situated in the central-north region of the country, Douera enjoys close proximity to the capital city, Algiers, further enhancing its significance as a dynamic hub of activity and culture.
>
> After: Douera had 56,998 inhabitants at the April 2008 census. It is in north-central Algeria, near Algiers.

The rewrite keeps both facts. The original's "approximately" in front of an exact census figure adds nothing.

An AI copyedit of plain human prose, with the human original first:

> Human: Gallery 825 on La Cienega Boulevard, which was purchased in 1958, is LAAA's exhibition arm for contemporary art. There are four individual gallery spaces.
>
> AI copyedit: Gallery 825 on La Cienega Boulevard serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces.

The copyedit replaced "is" with "serves as" and "there are" with "features", and it dropped the 1958 purchase date.

A sentence that needs no revision:

> The allocator returns memory to the OS only when an entire 2 MiB arena is free, so one long-lived allocation can pin an arena and inflate RSS.

It is long and technical, and every word in it carries information.

## Final check

Before handing text over, confirm that:

- Every sentence has a fact, claim, or instruction behind it and would lose something if deleted.
- No sentence asserts that something is significant without showing why.
- There are no reflexive contrasts, triads, rhetorical questions, setup lines, slogans, or trailing "-ing" clauses.
- Verbs are plain, using is and has where they fit.
- Attributions name their sources, and counts are accurate.
- There are no em dashes and no runs of sentences opening with transitions.
- Formatting suits the content and the destination, with little bold and few headings.
- There is no chat framing and there are no placeholders.
- Nothing is invented, and gaps are flagged.
- When revising, all of the original's facts, qualifications, and technical detail remain.
