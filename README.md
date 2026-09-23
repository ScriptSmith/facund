# facund

facund is an agent skill that tells Claude Code, GitHub Copilot CLI, and other agents that read `SKILL.md` files how to write prose without the patterns common in AI-generated text. Its main targets are bloviation (significance claims, puffery, grand openers, recaps) and reflexive rhetorical devices ("not just X, but Y", triads, rhetorical questions, setup lines, slogans).

The guidance is adapted from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), a guide that WikiProject AI Cleanup maintains for spotting AI-generated text in articles. The skill turns its observations into instructions for writing. For each pattern, the agent states the fact the sentence was standing in for or deletes the sentence, and it flags missing details instead of inventing them.

*Facund* is an archaic English word meaning eloquent.

## Contents

- `SKILL.md` is the file the agent loads. It covers bloviation and rhetorical tics, writing steps, conventions for documentation, web copy, code comments, PR descriptions, commit messages, and review comments, a review procedure, a table of other patterns, before-and-after examples, and a final checklist.
- `references/catalog.md` has the full word lists and real examples from the Wikipedia page, with notes on false positives and on the limits of AI-text detection. The agent reads it when doing a thorough review.
- `scripts/scan.py` is a Python 3 script with no dependencies. It lists words and constructions from the skill that appear in a text, with line numbers, and skips code blocks. It finds candidates for revision but can't tell whether a sentence says anything.

## Install

Clone the repository into your agent's skills directory:

```sh
# Claude Code
git clone https://github.com/ScriptSmith/facund ~/.claude/skills/facund

# GitHub Copilot CLI
git clone https://github.com/ScriptSmith/facund ~/.copilot/skills/facund
```

To share one copy between agents, clone it once and symlink the other directory to it. For a single project, clone it into the repository's `.claude/skills/` or `.github/skills/` directory.

## Use

The agent loads the skill when it writes text for other people, such as documentation, comments, PR descriptions, and emails, or when you ask it to rewrite or tighten some text. In Claude Code you can also run it directly with `/facund`.

The scanner also works on its own:

```sh
python3 scripts/scan.py README.md docs/*.md
python3 scripts/scan.py --summary draft.md
python3 scripts/scan.py < draft.txt
```

## License

`SKILL.md` and `references/catalog.md` adapt text and examples from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) by Wikipedia contributors, retrieved 23 September 2026. The adaptation reorganizes the material as writing guidance and adds instructions and examples. Both files are licensed under [CC BY-SA 4.0](LICENSE-CC-BY-SA). `scripts/scan.py` is licensed under the [MIT License](LICENSE-MIT).
