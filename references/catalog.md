# Catalog of AI writing patterns

Adapted from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and its [Style](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style) and [Markup](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Markup) subpages (CC BY-SA 4.0), retrieved 2026-11-09. The quoted examples are real text that Wikipedia editors flagged as AI-generated. Wikipedia's page is a field guide for spotting AI text in encyclopedia articles; this file keeps its observations and adds notes on writing around them. Some quoted examples originally contained em dashes, which are omitted here.

Wikipedia's own caveat applies: these are signs of deeper problems (unsupported claims, missing facts, vague sourcing), and fixing only the surface sign leaves the problem in place.

The signs change with each model generation. The page now lists blatant promotional language, knowledge-cutoff statements, and em dashes as historical signs that mostly mark text from older models, and it dates several newer ones. The sections below give dates where the page does. A dated pattern is still poor writing after models stop producing it.

## Contents

1. Content: significance, notability, identification by sources, superficial analysis, promotion, vague connection, vague attribution, the challenges formula, hedging disclaimers, summaries
2. Language: AI vocabulary, copula avoidance, negative parallelism, lead sentences, rule of three, rhetorical questions and slogans, elegant variation
3. Formatting: headings, bold, inline-header lists, tables, emoji, dashes, quotes, markup
4. Chatbot residue: collaborative framing, knowledge cutoffs, placeholders, tool artifacts, citations
5. Change descriptions: edit summaries, commit messages, PR descriptions
6. Comments in discussions
7. What human writing has more of
8. Weak indicators and the limits of detection

## 1. Content

### Significance, legacy, and broader trends

Words to watch: stands/serves as, is a testament/reminder, a crucial/pivotal/vital/significant/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, distinction matters/is important because.

The model puffs up the subject by claiming that some arbitrary aspect of it represents or contributes to something larger. It does this even for etymology or population data, sometimes after conceding the subject is minor. It also situates subjects amid "debates" and "discussions". Since mid-2026 models also editorialize that a particular distinction or nuance is important, usually alongside the hedging disclaimers described below.

> This etymology highlights the enduring legacy of the community's resistance and the transformative power of unity in shaping its identity.

> Though it saw only limited application, it contributes to the broader history of early aviation engineering and reflects the influence of French rotary designs on German manufacturers.

> GriefBots have prompted broader reflection on mortality and memory in a digital age. They blur boundaries between life and data, raising philosophical questions about identity, authenticity, and what it means to "live on" through algorithms.

For species and places, the model overstates ecosystem connections and conservation efforts even when none are documented:

> Currently, there is no specific conservation assessment for Lethrinops lethrinus by the International Union for Conservation of Nature (IUCN). However, the general health of the Lake Malawi ecosystem is crucial for the survival of this and other endemic species.

Writing note: show significance through the fact (first of its kind, adopted by N others, replaced X). If no such fact exists, leave significance out.

### Canned emphasis on notability and media coverage

Words to watch: independent coverage, local/regional/national media outlets, music/business/tech outlets, trade publications, cited/featured/profiled in, written by a leading expert, active social media presence.

The model tries to prove importance by listing where the subject was covered and what kind of outlet each is, often echoing guideline language ("independent coverage", "significant coverage") as if the justification for the text leaked into the text. Search-enabled models attach their own analysis to named sources ("Roger Ebert highlighted the lasting influence") whether or not the source says anything like it.

> Her insights have also been featured in Wired, Refinery29, and other prominent media outlets.

> The mall maintains a strong digital presence, particularly on Instagram, where it actively shares the latest updates and events.

Writing note: summarize what the coverage says. For example, report what The Guardian's 2019 review said about the album instead of noting that the album "has been featured in The Guardian".

### Identification by primary or tertiary sources (2026 on)

Words to watch: databases/records/listings/filings identify/list/describe [subject] as, is listed in, his/her professional profile lists.

In writing about a person or organization, such as a biography or a research summary, the model dwells on how a website, database, or record "identifies" the subject, instead of stating the fact and citing it.

> His personal website identifies him as a retired Indian Administrative Service (IAS) officer associated with the 1982 batch...

Writing note: state the fact and cite the source. Put the source in the sentence only when the reader needs to know who is making the claim, as with a self-description, and then say it plainly: "He says he..."

### Superficial analysis

Words to watch: highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., enhancing..., valuable insights, align/resonate with.

Usually a present-participle clause attached to the end of a factual sentence, commenting on its significance or impact.

> Historically, it has been crucial for linking Darbhanga with significant cities like Delhi, Patna, and Kolkata, facilitating the movement of passengers and goods. The station has supported various services, including passenger trains and express trains like the Satyagrah Express and Mithila Express, contributing to the socio-economic development of the region.

> In 2010, Les néologismes dans l'hebdomadaire L'Express (1980) was cited in the Proceedings of the 1st International Congress on Neology in Romance Languages, demonstrating the ongoing relevance of his research on lexical evolution.

The pattern persists when a model is asked to rephrase. Asked for "neutral paraphrases" of one sentence, a 2026 model offered three versions ending in ", reflecting the public image...", ", underscoring the image...", and ", highlighting the image...".

### Promotional language (mostly 2023 to 2025)

Words to watch: boasts a, vibrant, rich, profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, featuring, diverse array.

Older models struggled to hold a neutral tone even when told to, and their output drifted toward travel-guide or press-release prose. They avoided "the best" but stayed consistently positive. Wikipedia now lists this as a historical sign: blatant promotional tone became less common from around 2024 and is rare in newer output unless the user asks for it. Newer output tends to be promotional in what it chooses to include, such as awards and media coverage, more than in its adjectives.

> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and a significant place within the Amhara region.

> Smooth, uninterrupted surfaces and a pronounced A-line accentuate the vehicle's overall length, while a sleek, low tail imparts a sense of refined dynamism.

> CEO Allan Kilavuka emphasized the airline's commitment to sustainability, customer focus, and Africa's prosperity through responsible corporate practices.

### Vague connection

Words to watch: in connection with/to, connected with/to, in association with, associated with.

The model alludes to a link between two things instead of stating the relationship: "sources identified John Doe as being associated with leadership of ExampleCorp" for "John Doe was the CEO of ExampleCorp". It often comes with AI vocabulary ("particularly associated", "widely associated") and with the longer forms of copula avoidance described below. Often the plain relationship is known and sitting nearby:

> He is associated with the Rajhans Orchestra, a multicultural ensemble...

> He later became associated with musical education in Knokke-Heist, where he taught violin, viola and chamber music and conducted local ensembles.

The second sentence already contains the fact ("taught violin"); the "associated with" clause adds nothing.

### Vague attribution and overgeneralized opinion

Words to watch: industry reports, observers have cited, experts argue, some critics argue, several sources/publications (when few are cited), such as (before an exhaustive list).

Opinions get attributed to an unnamed authority, the number of sources gets exaggerated, one or two views are presented as widely held, and complete lists are framed as samples.

> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists.

> Toy industry publications such as The Toy Insider and Mojo Nation have presented Rubik's WOWCube as a STEM-oriented platform... (those two were the only sources)

### The challenges formula

Words to watch: Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook.

A closing section that opens "Despite its [praise], X faces challenges..." and ends with a vague upswing or speculation about initiatives that could help. The sign is the rigid formula; mentioning a problem is fine.

> Despite its industrial and residential prosperity, Korattur faces challenges typical of urban areas, including [...] With its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of the Ambattur industrial zone, embodying the synergy between industry and residential living.

### Hedging disclaimers

Chatbots try to cover perceived gaps in their content by pointing out that the gaps exist, or by adding cautionary disclaimers. The form of the disclaimer has changed with each generation of models.

#### Didactic disclaimers (2023 to 2024)

Words to watch: it's important/critical/crucial to note/remember/consider, worth noting, may vary.

Older models often gave an imagined reader advice about safety or controversial topics, or noted that something varies between places or jurisdictions. OpenAI's GPT-4 system card gives several such disclaimers as examples of "partial refusals".

> However, it's important to note that these caucuses operate outside the formal ANC structure and their influence on policy decisions may vary.

> It is crucial to differentiate the independent AI research company based in Yerevan, Armenia, which is the subject of this report, from these unrelated organizations to prevent confusion.

#### Speculation about gaps in sources (2024 to 2025)

Words to watch: while specific details are limited/scarce, not widely available/documented/disclosed, in the provided/available sources/search results, based on available information.

When a model with web search can't find information it says so, then guesses what the information "likely" is. The claim that something is "not documented" is itself a guess. For people it often claims they "maintain a low profile" or "keep personal details private", which is also a guess.

> Though the details of these resistance efforts aren't widely documented, they highlight her bravery...

> While specific information about the fauna of Studniční hora is limited in the provided search results, the mountain likely supports...

#### Corrective framing (mid-2026 on)

Words to watch: [claim] should be treated/presented as... rather than..., does not by itself establish, should not be confused with.

Since mid-2026, chatbots often add disclaimers about how a source should be used, which a September 2026 Graphite study calls "corrective framings". The page describes three patterns:

- A "rather than" construction warning that a source or claim should be read as speculative, subjective, or symbolic instead of definitive or verified.
- A caution that the available information does not establish some firm conclusion.
- A statement that the topic "should not be confused" with another. This one is the least reliable of the three.

The page says the pattern was almost unknown before mid-2026, roughly when GPT-5.6 came out in July, so a disclaimer of this kind in text from before July 2026 is much weaker evidence of AI use.

> [...] claims concerning its miraculous suspension should be treated as religious tradition rather than as archaeological explanation.

> The Victor Evidence website describes VictorMind and Victor Evidence as research systems undergoing testing and evaluation, rather than validated production or clinical systems.

> The guidance explains why subsurface conditions require separate attention from visible planting. It does not establish that Benjakitti has a particular contamination problem or groundwater configuration.

Writing note: say what the source shows. If a limit on a claim matters, state the limit as a fact (sample size, date range, who made the claim) and let the reader draw the conclusion. Disambiguate only when two things are easy to confuse.

### Section summaries and conclusions (mostly older models)

Words to watch: In summary, In conclusion, Overall.

Paragraphs and sections end by restating their main idea; long outputs grow a "Conclusion" section.

> In summary, the educational and training trajectory for nurse scientists typically involves a progression from a master's degree in nursing to a Doctor of Philosophy in Nursing, followed by postdoctoral training in nursing research.

## 2. Language

### AI vocabulary

Studies show these words became far more frequent after 2022. They co-occur: where there is one there are usually others, and an edit introducing many of them is one of the strongest tells.

Additionally (especially opening a sentence), align with, boasts (meaning "has"), bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, landscape (abstract noun), meticulous/meticulously, pivotal, robust, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant.

The set shifts between model generations:

- 2023 to mid-2024 (GPT-4): additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate, interplay, key (adjective), landscape, meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant.
- Mid-2024 to mid-2025 (GPT-4o): align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant.
- Mid-2025 to mid-2026 (GPT-5): emphasizing, enhance, highlighting, showcasing, plus the notability and media-coverage phrasing above.
- Mid-2026 on (GPT-6): challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally, with more periods and commas and shorter sentences of about 8 to 20 words. The page's only source for this entry is a September 2026 review of ChatGPT-6 Astra on the Intellectual Lead site, so treat it as provisional.
- Grok favors pseudo-scientific words (causal, empirical, correlate) and still overuses "underscore" in 2026.

Several words in the mid-2026 list (practical, clearer, steady, challenge) are ordinary in technical writing, and only a cluster of them means much.

Take the list literally. Overuse of a word doesn't implicate its synonyms, and literal senses (the underscore character, film underscore, a landscape photo) are fine.

> Somali cuisine is an intricate and diverse fusion of a multitude of culinary influences, drawing from the rich tapestry of Arab, Indian, and Italian flavours. This culinary tapestry is a direct result of Somalia's longstanding heritage of vibrant trade and bustling commerce.

### Avoiding "is" and "are"

Words to watch: serves as/stands as/marks/functions as/operates as/represents [a], boasts/features/maintains/offers [a], refers to.

One study found use of "is" and "are" in academic writing fell by over 10% in 2023 with no prior trend, and GPT-3.5 asked to "revise" 10,000 abstracts cut them further. AI copyedits "improve" text this way. Newer models use longer detours that shade into vague connection: "ventured into politics as a candidate" for "was a candidate", "began his career as" for "was". (Don't confuse this with "has" in the present perfect, as in "has been featured".)

Human original, then AI copyedit:

> It is Malaysia's first Malay daily afternoon tabloid [...] The Harian Metro was established in March 1991 and is the first and oldest Malay-language tabloid.

> It was established in March 1991 as Malaysia's first Malay-language afternoon tabloid [...] Harian Metro holds the distinction of being the first and oldest Malay-language tabloid.

### Negative parallelism

The text reads as if correcting a misconception nobody voiced. Common in human "myths busted" listicles, and a stereotypical AI sign.

"Not just X, but also Y":

> Self-Portrait by Yayoi Kusama [...] constitutes not only a work of self-representation, but a visual document of her obsessions, visual strategies and psychobiographical narratives.

> According to Yoo, the film's popularity derives not only from its digital animation and visual spectacle, but also from its ability to make a traditional mythological figure meaningful to contemporary audiences.

"Not X, but Y" and "no X, no Y, just Z":

> Kusama's self-portrait is not a mirror but a portal: not a representation of self, but a mechanism for its constant reinvention.

> This dispersal is not dissolution. Rather, it constitutes what Deleuze might describe as "becoming".

> Not a career, not a body of work, not sustained relevance [...] just an algorithmic moment.

"Y rather than X" (common in recent output from several models, not only Grok):

> Chiang's strategy emphasized military suppression of these holdouts to enforce subordination, prioritizing empirical consolidation of power amid fragmented loyalties rather than ideological purity.

> Rather than introducing a new decompiler, REA acts as an interface between AI agents and established analysis tools [...] Cyber Security News described the software as a bridge between AI coding agents and existing reverse-engineering tools rather than a replacement for conventional disassemblers.

Since mid-2026 this construction also carries the corrective framing described under hedging disclaimers ("should be treated as X rather than Y").

Across sentences, with "however" setting up a contrast that isn't one:

> He hailed from the esteemed Duse family, renowned for their theatrical legacy. Eugenio's life, however, took a path that intertwined both personal ambition and familial complexities.

### Lead sentences about the title

For subjects whose title isn't a proper name, the first sentence defines the title itself as if it were an entity, or uses "refers to":

> The "List of songs about Mexico" is a curated compilation of musical works...

> Catchment area (health) refers to the geographic area from which a health facility... draws its patients.

Writing note: define the subject directly. "A catchment area is the region a hospital draws its patients from."

### Rule of three

"Adjective, adjective, adjective" or "phrase, phrase, and phrase", often used to make a superficial analysis look comprehensive. Strongest where nobody would bother with a flourish, such as edit summaries and commit messages.

> The film preserves core elements such as Nezha's mythological image, magical weapons, and spirit of resistance while reshaping them through contemporary values, modern aesthetics, and digital animation technology.

> Heavy-Duty Rotary Saws: Designed for tougher materials such as tiles, metals, and plastics.

### Rhetorical questions and slogans

These appear throughout the page's examples of AI-written comments and articles:

> One might wonder: if it's a "travel food," why not just cook it on the ship?

> And consensus doesn't grow from silence [...] it grows from critique, correction, and clarity.

> Movements evolve before they're neatly labelled.

> Collaboration, not confrontation, should be the goal.

None of them makes a claim a reader could check. The last three also use negative parallelism or a triad.

### Elegant variation (mostly older models)

Older models had a repetition penalty, so they cycle synonyms for a single referent. In one article the same idea appeared as "the constraints of socialist realism", "the challenging climate of Soviet artistic constraints", "the confines of state-imposed artistic norms", "the constraints imposed by the Soviet regime", and "the artistic norms of their time", while the artists were in turn "non-conformist artists", "like-minded artists", "Russian avant-garde artists", and "the diverse yet united front of non-conformist artists".

Some writers are taught to avoid repetition (Italian schools, for instance), so this alone doesn't prove AI use. In expository writing it still causes confusion, because readers assume a new term refers to a new thing.

## 3. Formatting

- Title case headings. Chatbots capitalize all main words in section headings ("Impact of Technology and Digitalization").
- Title heading. A heading repeating the document's name at the top, when the page already shows its title.
- Headings containing only headings. A heading with no text of its own, just subheadings.
- Skipped or odd levels. Starting sections at level 3, or using level-1 headings for every section.
- Formula headings. "X and Y" headings, especially "Awards and recognition", "Challenges and future directions", "Legacy and impact".
- Thematic breaks. A horizontal rule (`---` or `----`) between every section, common in Markdown output.
- Bold overuse. Emphasizing every instance of chosen terms in a "key takeaways" style, a habit inherited from READMEs, slide decks, sales pitches, and listicles.

  > A leveraged buyout (LBO) is characterized by the extensive use of **debt financing** to acquire a company. This financing structure enables **private equity firms** and **financial sponsors** to control businesses...

- Inline-header vertical lists. A list marker followed by a bold header, a colon, and a description, repeated. Sometimes the colon is missing and each "item" is a bold phrase followed by a paragraph.
- Small tables. Minimal tables for information that reads better as a sentence, such as a four-row table of executives and titles.
- Emoji as formatting. Emoji in front of headings or bullets ("🧠 Cognitive Dissonance Pattern:"). Rarer now, but still seen.
- Em dashes (2022 to September 2026). LLMs use em dashes more than non-professional human writers of the same genre, in places where people would use commas, parentheses, or colons, and often in a formulaic, punched-up way that over-emphasizes a clause or a parallelism. AI em dashes are usually spaced. OpenAI suppressed them in GPT-5.1; a July 2026 study found Claude was the only current model using more em dashes than professional writers. On its own this is a weak sign, and Wikipedia now lists it as historical: older models still produce em dashes, but the newest ones (from September 2026) are reported to suppress them entirely.
- Flat punctuation. The page reports that models trained against em dashes now avoid other punctuation as well, so their text uses more commas and periods than human text and little else. This claim is marked "citation needed". The mid-2026 vocabulary entry above also mentions short sentences of about 8 to 20 words.
- Curly quotes. ChatGPT and DeepSeek typically produce curly quotes and apostrophes, sometimes mixed with straight ones. Gemini and Claude typically don't. Word processors and typesetting also produce curly quotes, so this is weak too.
- Markdown in the wrong place. Markdown pasted into a non-Markdown target, such as wikitext, a plain-text email, or a form field: `**asterisks**` for bold, `##` for headings, `[text](url)` links, `---` rules, and fenced code blocks. On Wikipedia, `##` headings render as numbered lists, and fenced code blocks labelled `wikitext` survive the paste. Markdown by itself is not a sign, since many people write it.

## 4. Chatbot residue

### Collaborative framing

Words to watch: I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., is there anything else, let me know, more detailed breakdown, here is a, [check/verify/confirm]... before [publishing/submitting].

Text written as correspondence, prewriting, or advice to the chatbot's user ends up in the deliverable, in the text itself or in hidden comments:

> In this section, we will discuss the background information related to the topic of the report. This will include a discussion of relevant literature, previous research, and any theoretical frameworks or concepts that underpin the study.

> Here's a template for your wiki user page. You can copy and paste this onto your user page and customize it further.

Drafting notes can survive as an outline of hidden comments under each heading, addressed to whoever writes the final text:

> `<!-- LEAD: expand to two short paragraphs once the body exists. No honorifics anywhere in this article. Do not use "Dr". -->`

Also: advice-to-the-user text left in place ("Delete this section before submission", "verify these figures before publishing"), and explicit statements that the text is meant for Wikipedia or follows its guidelines.

### Knowledge-cutoff disclaimers and refusals (2022 to 2023)

"As of my last knowledge update in January 2022, I don't have specific information about...", "As an AI language model, I can't...". Also abrupt cut-offs mid-sentence where the output hit a length limit.

### Placeholders

Fill-in-the-blank templates the user forgot to fill: "[Describe the specific section or content that needs editing]", "[Your Name]", "[Year]", "[Founder Names]", "[link to the revised article]", "(Add your channel URL here)", access dates like "2025-XX-XX", fields like `INSERT_SOURCE_URL_30` or `PASTE_SPOTIFY_TRACK_URL_HERE`, and comments like "<!-- Add if available with citation -->".

URL placeholders: citation links to made-up subpages of example.com, such as `https://example.com/source1`, `https://example.com/article`, or `https://example.com/news`. Plain `example.com` is a legitimate placeholder in documentation; the sign is a citation that points at it.

### Tool artifacts

Internal markup that leaks when chatbot output is copied:

- ChatGPT: `:contentReference[oaicite:0]{index=0}`, `oai_citation`, `citeturn0search0` (the number rising through the text), `turn0image0`, `({"attribution":{"attributableIndex":"1009-1"}})`, "Example+1" style link residue, and `utm_source=chatgpt.com` or `utm_source=openai` on URLs.
- Gemini: `[cite: 1]`, `[span_1](start_span)`.
- Grok: `<grok-card data-id=... data-type="citation_card">`, `grok_render_citation_card_json`, `referrer=grok.com`.
- DeepSeek: `【29†L582-L589】`.
- Perplexity: `[attached_file:1]`, `[web:1]`, `ppl-ai-file-upload` in URLs.
- Copilot: `utm_source=copilot.com`.
- Unclassified: `:::writing{variant="document" id="68427"}`.
- A "↩" character around footnotes.

### Citations

- Several dead links in one new page, especially links that archive sites never saw.
- ISBNs with invalid checksums; DOIs that don't resolve or resolve to unrelated papers.
- Book citations with no page number, or a page that doesn't contain the claim, typically for a general, frequently cited book with no URL.
- References defined but never used, or used but never defined.
- Hallucinated category or template names that sound plausible.

Writing note: cite only sources you have opened and checked. If you couldn't verify something, say so.

## 5. Change descriptions

Wikipedia's observations about AI edit summaries apply directly to commit messages and PR descriptions. An AI-written summary strongly suggests the change itself was AI-written, since few people would use AI for the summary but not for the edit.

- Canned assurances of compliance. Words to watch: ensured that... adheres to, refined, enhanced, enriched, streamlined, improved, in compliance/complies with, verifiability, neutrality, neutral tone, clarity, flow. A human says "removed excessive links per MOS:OVERLINK"; the AI version is longer and less specific: "revised for clarity and compliance with the Manual of Style". The more assurances stacked in one summary, the stronger the sign.
- Mentions of what wasn't changed. Words to watch: preserved, retained, avoided, ensured, aimed to. "Removed promotional language [...] while preserving the original meaning and technical details." People rarely describe what they didn't touch; a model prompted to "change X but preserve Y" reports exactly that.
- Emphasis on sourcing over content. "Added sourced information, references, and internal/external links." A human writes "added info about the artist's debut".
- Granular markup detail. Itemized parameter and template names, "added inline citations", "corrected infobox parameters (image_size)".
- Stating the obvious. "Addressing reviewer feedback by...", which goes without saying after a review.

Older AI edit summaries were often in the first person and had the usual signs of older output (AI vocabulary, emoji, lists, Markdown). Newer ones are more likely to be exhaustively procedural about the editing process and how it complies with the rules.

Developer equivalents: "Refactored for improved readability and maintainability while preserving existing behavior", "Enhanced error handling to ensure robustness". Say which function changed and what it now does.

## 6. Comments in discussions

AI-written discussion comments, beyond the patterns above, tend to:

- misquote policies or cite rule shortcuts that don't exist;
- split a comment into titled sections, in Markdown or as subheadings;
- itemize assurances that the author made an effort to follow the rules;
- ask critics to spell out exactly what to improve;
- open with "I hope this message finds you well" or "I am writing to...".

Many read as if written by a clerk or a customer service representative. The author says they "carefully reviewed" their work, apologizes for any inconvenience they "may have" caused, and closes with something like "If there are specific issues that need to be resolved, please point them out to me, and I will try to resolve them." The page suggests this is because AI writing tools are often marketed for use at work.

Writing note: answer the point in plain paragraphs, and cite a rule only after checking that it says what you claim.

## 7. What human writing has more of

Measured over 25 years of Wikipedia text, human writing uses these more than AI text does:

- Simple "is" and "has" phrases, such as "there is a" and "it has a".
- Plain words where AI picks a stiff or euphemistic synonym: wrote (authored), moved (relocated), used (utilized), tried (attempted), died (passed away).
- Superlative and definitive statements, such as "one of the best", "is the only", "was the first".
- Qualifiers and intensifiers, such as "very", "perhaps", "tends to".
- Some wordy constructions: "as a result of", "in order to", "all of the", "a part of", "the fact that".

The last two points argue against trimming by reflex. Ordinary human prose contains some slack and some honest hedging. Remove slack when it obscures the point, and leave sentences their natural variety.

Each model also has its own idiolect. ChatGPT and Grok dwell on broader context more than Gemini and Claude, whose answers tend to be more concise.

## 8. Weak indicators and the limits of detection

Useless or weak on their own:

- Perfect grammar, since many people write well.
- Mixed casual and formal registers, or prose that sounds both clinical and emotional.
- "Bland" or "robotic" prose. AI output skews positive and verbose, which doesn't necessarily read as robotic.
- Formal, academic, or fancy vocabulary in general. Only specific words are overused.
- Isolated transition words. "Additionally" or "Consequently" once is normal essay style.
- Unsourced content. Most uncited Wikipedia text predates LLMs, and modern chatbots do cite, if not always accurately.

Calibration:

- Humans without much LLM exposure detect AI text at about chance. In a 2025 preprint, a subset of "expert" annotators who use LLMs heavily flagged 90% of AI-generated texts correctly and misidentified 3.3% of human-written texts as AI-generated.
- Automated detectors beat chance but have real error rates and are fooled by paraphrasing and formatting changes.
- Text written before ChatGPT's public launch on 30 November 2022 can be treated as human.
- Human writing is converging on LLM style, including in speech, so single features prove less every year. The convergence is slow and uneven, and it goes one way: LLM output is not becoming more like human writing.
- A sudden shift in someone's style is more telling than any one word. Someone who has used AI for years tends to write like the models of each year: their 2023 text reads like 2023 output, and their 2025 text like 2025 output.
- Many different kinds of signs together are strong evidence; one kind repeated is weak evidence.
