#!/usr/bin/env python3
"""Flag common signs of AI writing in prose.

Usage: scan.py [--max N] [--summary] [FILE ...]   (reads stdin when no files are given)

Each hit is a prompt to reread the sentence. The scanner can't detect generic
content or missing specifics, so read the text as well. Fenced code blocks, inline code, and YAML front matter are skipped.
"""
import argparse
import bisect
import re
import sys

I = re.IGNORECASE
M = re.MULTILINE


def alt(*words):
    return r"\b(?:" + "|".join(words) + r")\b"


RULES = [
    ("significance", "state the fact that shows it, or delete", [
        r"\b(?:is|as|stands as) an? (?:testament|reminder)\b",
        r"\btestament to\b",
        r"\b(?:pivotal|crucial|vital|significant|key|central|instrumental) (?:role|moment|turning point|milestone|part in)\b",
        r"\b(?:underscor|highlight|emphasiz|emphasis|reinforc)\w* (?:its|the|their|his|her) (?:importance|significance|role|relevance|value)\b",
        r"\breflect\w* (?:a |the )?(?:broader|wider|larger)\b",
        r"\b(?:enduring|lasting|ongoing|indelible|profound) (?:legacy|impact|influence|mark|relevance|significance|contribution)\b",
        r"\bsetting the stage\b",
        r"\b(?:marking|marks|marked|represent\w*) an? (?:shift|turning point|pivotal|significant|major|new era|watershed)\b",
        r"\b(?:turning point|focal point|indelible mark|deeply rooted)\b",
        r"\b(?:evolving|ever-changing|changing|shifting) landscape\b",
        r"\bbroader (?:context|movement|trend|trends|history|landscape|implications|reflection|debate)\b",
        r"\b(?:shap|defin)(?:e|es|ed|ing) the (?:future|landscape|course)\b",
        r"\bin today's\b",
        r"\bin an (?:era|age|world) (?:where|of|when)\b",
        r"\bmore (?:important|crucial|critical|relevant) than ever\b",
    ]),
    ("trailing -ing", "end the sentence at the fact, or make the claim its own supported sentence", [
        r",\s+(?:further\s+|thereby\s+|thus\s+|ultimately\s+)?(?:highlighting|underscoring|emphasi[sz]ing|ensuring|reflecting|symboli[sz]ing|contributing to|cultivating|fostering|encompassing|enhancing|showcasing|demonstrating|illustrating|solidifying|reinforcing|cementing|streamlining|empowering|enabling|driving|signal(?:l)?ing|embodying|paving the way|positioning|creating an?|offering an?|providing an?|making it an?)\b",
    ]),
    ("puffery", "replace adjectives with checkable details", [
        alt("boasts?", "boasted", "boasting", "vibrant", "nestled", "breathtaking", "renowned", "groundbreaking",
            "world-class", "cutting-edge", "state-of-the-art", "seamless(?:ly)?", "unparalleled", "captivat\\w+",
            "game-chang\\w+", "revolutioni[sz]\\w+", "empower\\w*", "unlock(?:s|ing)? the"),
        r"\bin the heart of\b",
        r"\bdiverse (?:array|range|tapestry|mix)\b",
        r"\brich (?:cultural|history|heritage|tapestry|tradition)\b",
        r"\bnatural beauty\b",
        r"\bcommitment to\b",
        r"\bdedicat\w+ to (?:excellence|quality|providing|delivering)\b",
        r"\b(?:powerful|robust|flexible|intuitive), (?:\w+,? )?and (?:powerful|robust|flexible|intuitive|scalable|easy)\b",
    ]),
    ("ai vocabulary", "usually decorates an empty claim; fix the claim, or use the plain word", [
        alt("align(?:s|ed|ing)? with", "bolster(?:s|ed|ing)?", "crucial(?:ly)?", "deep dive", "delv(?:e|es|ed|ing)",
            "emphasi[sz](?:e|es|ed|ing)", "enduring", "enhanc(?:e|es|ed|ing|ement)", "foster(?:s|ed|ing)?",
            "garner(?:s|ed|ing)?", "highlight(?:s|ed|ing)?", "interplay", "intricac(?:y|ies)", "intricate",
            "landscape", "meticulous(?:ly)?", "multifaceted", "pivotal", "quietly", "robust(?:ly|ness)?", "showcas(?:e|es|ed|ing)", "tapestry",
            "testament", "underscor(?:e|es|ed|ing)", "valuable", "leverag(?:e|es|ed|ing)", "realm",
            "resonat(?:e|es|ed|ing) with", "valuable insights?"),
    ]),
    ("copula avoidance", "try is/are/has", [
        r"\b(?:serves?|served|serving|stands?|stood|functions?|functioned|operates?|operated|acts?|acted) as (?:a|an|the|one)\b",
        r"\b(?:features|offers|maintains)\s+(?:a|an|over|more than|several|numerous|\d+)\b",
        r"\bholds? the distinction\b",
        r"\brefers? to (?:the )?(?:process|practice|concept|idea|act|study|field|phenomenon|geographic)\b",
    ]),
    ("negative parallelism", "state the positive claim directly", [
        r"\bnot (?:just|only|merely|simply|solely)\b[^.;:!?\n]{0,80}?\bbut\b",
        r"\b(?:isn't|aren't|wasn't|weren't|is not|are not|was not|were not|doesn't|does not|don't|do not|(?:it|that|this|there|he|she)'s not|(?:they|you|we)'re not)\b(?: just| only| merely| simply| about)?[^.!?\n,;:]{1,60}[;,:\u2014\u2013]\s*(?:it's|it is|they're|they are|that's|this is|it was|rather)\b",
        r"\b(?:is|are|was|were)\s+not\s+(?:a |an |the )?\w+(?:\s+\w+){0,3},?\s+but\s+(?:a|an|the|in|rather)\b",
        r"[.!?]\s+Rather,",
        r"(?:^|[.!?]\s+)Rather than\b",
        r"\bRather than (?:simply|just|merely)\b",
        r"\b(?:not|no) (?:a |an |the )?\w+(?: \w+)?, (?:not|no) (?:a |an |the )?\w+",
    ]),
    ("corrective framing", "say what the evidence shows; state a real limit as a fact", [
        r"\bshould (?:instead )?be (?:treated|read|understood|seen|viewed|presented|interpreted|regarded|framed|taken) as\b[^.\n]{0,100}?\brather than\b",
        r"\b(?:does not|do not|did not|doesn't|don't|didn't|cannot|can't|could not|couldn't)(?: by itself| on its own| alone| necessarily)? (?:establish|prove|demonstrate|confirm)\b",
        r"\b(?:by itself|on its own|alone),? (?:does not|doesn't|cannot|can't) (?:establish|prove|demonstrate|confirm|mean)\b",
        r"\b(?:should not|shouldn't|not to) be confused with\b",
        r"\b(?:distinction|difference|nuance) (?:matters|is (?:important|crucial|significant|key))\b",
    ]),
    ("rhetorical device", "make the statement instead", [
        r"\bOne might (?:wonder|ask)\b",
        r"(?:^|[.!?]\s+)(?:The result|The answer|The catch|The problem|The kicker|The upshot|The takeaway|The difference|The twist|The reason)\?",
        r"\bHere's (?:the thing|why|what|how)\b",
        r"\b(?:Why|What) does (?:this|that|it) matter\?",
        r"(?:^|[.!?]\s+)(?:This|That|It) matters\b",
        r"\bwhy (?:this|that|it) matters\b",
        r"\bLet that sink in\b",
        r"\bFull stop\.",
        r"\bAnd that's (?:the point|what matters|okay)\b",
    ]),
    ("vague attribution", "name the source and what it said, or drop it", [
        r"\b(?:experts|observers|critics|analysts|scholars|researchers|commentators|historians|many|some|several)\s+(?:have\s+)?(?:argue|argued|note|noted|say|said|suggest|suggested|believe|contend|point(?:ed)? out|agree|describe[ds]?|cite[ds]?|observe[ds]?)\b",
        r"\bindustry (?:reports|observers|experts|analysts|publications)\b",
        r"\b(?:widely|generally|often|commonly|frequently) (?:regarded|considered|recogni[sz]ed|seen|viewed|described|cited|praised|acknowledged|interpreted)\b",
        r"\b(?:studies|research|reports|sources) (?:show|shows|suggest|suggests|indicate|indicates|have shown)\b",
        r"\bdescribed in (?:scholarship|the literature)\b",
        r"\baccording to (?:some|many|several|various) \w+",
        r"\bit is (?:widely |generally |often |commonly )?(?:believed|said|thought|argued|considered)\b",
    ]),
    ("vague connection", "state the actual relationship", [
        r"\b(?:(?:closely|particularly|widely|primarily|principally|often|also|became) )?associated with\b",
        r"\bin (?:connection|association) (?:with|to)\b",
    ]),
    ("notability claims", "report what the source said", [
        r"\b(?:featured|profiled|spotlighted|showcased) (?:in|by|on)\b",
        r"\b(?:independent|significant|widespread|extensive|national|international|regional|media|press) coverage\b",
        r"\b(?:prominent |major |leading )?(?:media|news) outlets?\b",
        r"\btrade publications?\b",
        r"\b(?:active|strong|robust|growing|significant) (?:social media|online|digital) presence\b",
    ]),
    ("challenges formula", "describe real problems with specifics; remove the reassuring turn", [
        r"\bdespite (?:its|their|these|this|the|such)\b[^.\n]{0,60}\b(?:challenges|success|popularity|growth|achievements|prosperity|promise|promising)\b",
        r"\bfaces? (?:several |many |numerous |significant |a number of |various |new |ongoing )?challenges\b",
        r"\bcontinues? to (?:thrive|evolve|grow|flourish|shape|inspire)\b",
        r"\bfuture (?:outlook|prospects|directions)\b",
        r"\bchallenges and (?:opportunities|future|legacy)\b",
    ]),
    ("gap speculation", "say what is known and leave out guesses", [
        r"\b(?:not|isn't|aren't|is not|are not|remains?)\s+(?:widely|well|extensively|publicly|readily|fully)\s+(?:documented|known|available|reported|disclosed|transcribed)\b",
        r"\b(?:details|information|data|specifics)\b[^.\n]{0,30}\b(?:is|are|remain)\s+(?:limited|scarce|sparse|unavailable)\b",
        r"\bbased on (?:the )?(?:available|provided) (?:information|sources|data)\b",
        r"\bas of my (?:last|latest)\b",
        r"\b(?:knowledge|training) (?:cutoff|cut-off|update)\b",
        r"\bmaintains? a low profile\b",
        r"\bin the (?:provided|available) (?:sources|search results|documents)\b",
    ]),
    ("didactic disclaimer", "state the point without the preamble", [
        r"\bit(?:'s| is) (?:important|crucial|critical|essential|vital|worth) (?:to )?(?:note|noting|remember|mention|mentioning|consider|emphasi[sz]e|understand|recogni[sz]e)\b",
        r"\bworth noting\b",
        r"\bit should be noted\b",
        r"\bmay vary\b",
    ]),
    ("summary / meta", "end on the last new point; cut announcements", [
        r"(?:^|[.!?]\s+)(?:In summary|In conclusion|To sum up|To summari[sz]e|In essence|Overall|Ultimately),",
        r"\bin this (?:section|article|document|post|guide|report|README),? (?:we|I) (?:will|'ll)\b",
        r"\bthis (?:article|section|document|guide|post) (?:explores|examines|discusses|delves|will)\b",
        r"\blet's (?:dive|delve|explore|take a (?:closer )?look|break (?:it|this) down)\b",
    ]),
    ("formula heading", "organize sections around the actual material", [
        r"^#{1,6}[ \t]*(?:Key Features|Key Takeaways|Key Highlights|Challenges(?: and [\w ]+)?|Future (?:Outlook|Prospects|Directions)|Legacy(?: and [\w ]+)?|Impact and Legacy|Awards and Recognition|Recognition|Why (?:It|This) Matters|Final Thoughts|Wrapping Up|Conclusion|In Summary)[ \t]*$",
    ]),
    ("stacked transition", "delete, or reorder so the logic is visible", [
        r"(?:^|[.!?]\s+)(?:Additionally|Moreover|Furthermore|Notably|Importantly|Crucially|Interestingly|Consequently),",
    ]),
    ("stiff wording", "use the plain word", [
        alt("utili[sz](?:e|es|ed|ing|ation)", "commenc(?:e|es|ed|ing)", "endeavou?r(?:s|ed)?",
            "facilitat(?:e|es|ed|ing)", "authored", "relocated", "passed away", "prior to", "subsequently",
            "a myriad of", "plethora", "whilst", "aforementioned", "in order to ensure"),
    ]),
    ("chat residue", "delete it", [
        r"\b(?:Certainly|Of course|Absolutely|Great question|Sure thing|Great work|Nice work)!",
        r"\bI hope (?:this|that) helps\b",
        r"\blet me know if\b",
        r"\bfeel free to\b",
        r"\bwould you like (?:me )?to\b",
        r"\bis there anything else\b",
        r"\bhere(?:'s| is) (?:a|an|the|your)\b[^.\n]{0,50}:\s*$",
        r"\bhappy to help\b",
        r"\byou're (?:absolutely )?right\b",
        r"\bI hope this (?:message|email) finds you well\b",
        r"\bas an? (?:AI|large language model|language model)\b",
        r"\b(?:verify|double-check|confirm|fact-check) (?:these|the|all|any|this|each|that)\b[^.\n]{0,60}?\bbefore (?:publishing|publication|submitting|submission|posting)\b",
        r"\bapologi[sz]e for any (?:inconvenience|confusion|trouble)\b",
        r"\b(?:I|we) (?:have )?carefully reviewed\b",
        r"\bplease point (?:them|it|these|those|this) out\b",
    ]),
    ("change-note puffery", "name the concrete change", [
        r"\b(?:improv|enhanc|refin|streamlin)\w* (?:the )?(?:overall )?(?:clarity|flow|readability|tone|consistency|structure|conciseness|maintainability)\b",
        r"\bfor (?:better |improved |greater |enhanced )?(?:clarity|readability|flow|conciseness|consistency|maintainability)\b",
        r"\b(?:while|and) (?:preserving|retaining|maintaining|keeping) (?:the )?(?:original|existing|core|overall)\b",
        r"\bensur\w+ (?:neutrality|consistency|accuracy|compliance|clarity|robustness)\b",
        r"\b(?:follows|adheres to|in line with|in accordance with|in compliance with) (?:the )?(?:best practices|style guide|guidelines)\b",
    ]),
    ("placeholder", "fill it in or ask", [
        r"\[(?:Your|Insert|Add|Describe|Links?|Names?|Company|Date|Year|Title|Author|Article|Founders?|Email|Brief|Specific|Reason)\b[^\]\n]{0,80}\](?![(\[])",
        r"\b20\d\d-(?:XX|xx)-(?:XX|xx)\b",
        r"\bexample\.com/(?:source|article|news|ref|citation)\w*",
        r"\b(?:INSERT|PASTE|SOURCE|ADD)_[A-Z_]+\b",
        r"\((?:Add|Insert|Paste) [^)\n]{0,60}(?:here|if available)\)",
    ]),
    ("tool artifact", "strip it and recheck the claim's source", [
        r"contentReference|oaicite|oai_citation|attributableIndex|ppl-ai-file-upload",
        r"\bturn\d+(?:search|image|news|file)\d+\b",
        r"\[cite:\s*\d",
        r"\[span_\d+\]\((?:start|end)_span\)",
        "【\\d+†",
        r"utm_source=(?:chatgpt\.com|openai|copilot\.com)|referrer=grok\.com",
        r"\[(?:attached_file|web):\d+\]",
        r"grok[_-](?:card|render)",
        r":::writing\{",
    ]),
    ("em dash", "restructure: commas, parentheses, a clause, or two sentences", [
        "\u2014",
        " \u2013 ",
    ]),
    ("markdown formatting", "prose if the items connect; plain items otherwise; no emoji", [
        r"^[ \t]*(?:[-*+•]|\d+[.)])[ \t]+(?:\*\*|__)[^*_\n]{1,60}(?:\*\*|__)[ \t]*:?",
        r"^[ \t]*(?:#{1,6}[ \t]*|[-*+][ \t]+)?[\U0001F300-\U0001FAFF☀-➿⭐✅]",
    ]),
    ("triad (low signal)", "keep only if there really are three things", [
        r"\b[A-Za-z][\w-]*(?: [\w-]+)?, [A-Za-z][\w-]*(?: [\w-]+)?,? (?:and|or) [A-Za-z][\w-]*(?: [\w-]+)?\b",
    ]),
]

SMALL_WORDS = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor", "of", "on", "or", "the", "to",
               "vs", "via", "with", "from", "into", "is"}


def compile_rules():
    compiled = []
    for name, hint, patterns in RULES:
        compiled.append((name, hint, [re.compile(p.replace("'", "['\u2019]"), M | I) for p in patterns]))
    return compiled


def mask(text):
    """Blank out front matter, fenced code, and inline code, keeping offsets."""
    out = list(text)

    def blank(start, end):
        for i in range(start, end):
            if out[i] != "\n":
                out[i] = " "

    fm = re.match(r"---\n.*?\n---\n", text, re.S)
    if fm:
        blank(0, fm.end())
    for m in re.finditer(r"^(```|~~~).*?^\1[^\n]*$", text, re.S | M):
        blank(m.start(), m.end())
    for m in re.finditer(r"`[^`\n]+`", text):
        blank(m.start(), m.end())
    for m in re.finditer(r"https?://[^\s)>\]]+", text):
        blank(m.start(), m.end())
        for t in re.finditer(r"utm_source=[\w.]+|referrer=grok\.com|example\.com/(?:source|article|news|ref|citation)\w*",
                             m.group(0)):
            out[m.start() + t.start():m.start() + t.end()] = t.group(0)
    return "".join(out)


def title_case_headings(text):
    for m in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, M):
        words = [w for w in re.findall(r"[A-Za-z][\w'-]*", m.group(1))]
        content = [w for w in words[1:] if w.lower() not in SMALL_WORDS]
        if content and all(w[0].isupper() for w in content) and not all(w.isupper() for w in content):
            yield m.start(1), m.end(1)


def scan(text, rules):
    masked = mask(text)
    hits = {}
    for name, hint, patterns in rules:
        spans = []
        for p in patterns:
            for m in p.finditer(masked):
                g = m.group(0)
                lead = len(g) - len(g.lstrip(".!?;: \t\n"))
                if g.strip():
                    spans.append((m.start() + lead, m.end()))
        if spans:
            spans.sort()
            deduped = [spans[0]]
            for s in spans[1:]:
                if s[0] >= deduped[-1][1]:
                    deduped.append(s)
            hits[name] = (hint, deduped)
    tc = list(title_case_headings(masked))
    if tc:
        hits["title case heading"] = ("use sentence case unless the words are proper nouns", tc)
    return masked, hits


def snippet(text, line_starts, start, end, width=90):
    line = bisect.bisect_right(line_starts, start) - 1
    ls = line_starts[line]
    le = text.find("\n", ls)
    le = len(text) if le == -1 else le
    lo = max(ls, start - max(0, (width - (end - start)) // 2))
    hi = min(le, max(end, lo + width))
    s = text[lo:hi].replace("\t", " ").strip()
    return line + 1, start - ls + 1, ("..." if lo > ls else "") + s + ("..." if hi < le else "")


def report(label, text, rules, max_hits, summary_only):
    masked, hits = scan(text, rules)
    nwords = len(re.findall(r"\b\w+\b", masked)) or 1
    line_starts = [0] + [m.end() for m in re.finditer(r"\n", text)]
    bold = len(re.findall(r"\*\*[^*\n]+\*\*|__[^_\n]+__", masked))
    headings = len(re.findall(r"^#{1,6}\s", masked, M))
    rules_hr = len(re.findall(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$", masked, M))
    curly = len(re.findall("[“”‘’]", masked))

    print(f"== {label} ({nwords} words)")
    ordered = sorted(hits.items(), key=lambda kv: (kv[0].endswith("(low signal)"), -len(kv[1][1])))
    for name, (hint, spans) in ordered:
        print(f"\n{name} ({len(spans)}): {hint}")
        if summary_only:
            continue
        for start, end in spans[:max_hits]:
            ln, col, s = snippet(text, line_starts, start, end)
            print(f"  L{ln}:{col}  {s}")
        if len(spans) > max_hits:
            print(f"  ... and {len(spans) - max_hits} more")

    strong = {k: v for k, v in hits.items() if not k.endswith("(low signal)")}
    total = sum(len(v[1]) for v in strong.values())
    print(f"\nsummary: {total} hits in {len(strong)} categories, {100 * total / nwords:.1f} per 100 words"
          " (low-signal categories excluded)")
    extras = []
    if bold:
        extras.append(f"bold spans {bold} ({100 * bold / nwords:.1f}/100 words)")
    if headings:
        extras.append(f"headings {headings} (one per {nwords // headings} words)")
    if rules_hr:
        extras.append(f"horizontal rules {rules_hr}")
    if curly:
        extras.append(f"curly quotes {curly}")
    if extras:
        print("formatting: " + ", ".join(extras))
    print("Each hit is a prompt to reread the sentence. Several categories together are stronger evidence than"
          " one category repeated. The scanner can't detect generic content, so read the text as well.")


def main():
    ap = argparse.ArgumentParser(description="Flag common signs of AI writing in prose.")
    ap.add_argument("files", nargs="*", help="files to scan (default: stdin)")
    ap.add_argument("--max", type=int, default=12, help="max hits shown per category (default 12)")
    ap.add_argument("--summary", action="store_true", help="show category counts only")
    args = ap.parse_args()
    rules = compile_rules()
    if not args.files:
        report("stdin", sys.stdin.read(), rules, args.max, args.summary)
        return
    for i, path in enumerate(args.files):
        if i:
            print()
        with open(path, encoding="utf-8", errors="replace") as f:
            report(path, f.read(), rules, args.max, args.summary)


if __name__ == "__main__":
    main()
