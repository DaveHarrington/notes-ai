You are fact-checking a quarterly performance check-in document for accuracy, substantiation, and intellectual honesty.

## Input

The user will provide a link to or paste the check-in draft: $ARGUMENTS

If a Slack link or Obsidian note reference is provided, fetch the content first. If the argument is a person's name, look for their people note in the Obsidian vault (`notes`, folder `People`) and find the most recent check-in section.

## Step 1: Read the draft

Load the full check-in document. Read it carefully, noting every factual claim, metric, date, name, and attribution.

## Step 2: Verify claims in Slack

For each significant claim in the document, search Slack to verify it. This includes:

- **Project names, dates, and timelines** — search project channels to confirm
- **Metrics and quantitative achievements** — find the source messages or dashboards
- **Team member names and roles** — confirm they're correctly stated
- **Product/feature names** — verify against official terminology in channels
- **Incidents or outages** — search incident channels to confirm details

Run searches in parallel where possible. Use `from:@{person}` and channel-specific searches with date filters matching the review period.

## Step 3: Evaluate citation quality

For every hyperlinked citation in the document:

1. Follow the link (read the Slack message)
2. Confirm the linked source actually supports the claim being made
3. Flag any citations where the source says something different than what's claimed

Also flag any significant claims that have NO citation at all.

## Step 4: Check timeline & sequencing

- Verify all dates fall within the stated review period
- Confirm chronology of events is accurate
- Check that "before/after" comparisons are factually correct
- Verify milestone dates against actual delivery dates found in Slack

## Step 5: Verify attribution & ownership

Search Slack to understand who actually did what:
- Was this truly an individual contribution, or was it a team effort?
- Are collaborators correctly identified?
- Is the scope of personal impact honestly represented?
- Is credit appropriately shared?

## Step 6: Check technical accuracy

Verify that:
- Technical terms and concepts are used correctly
- Architecture decisions are described accurately
- Performance improvements are quantified correctly
- Technology stack references are accurate

## Step 7: Run consistency checks

- Do metrics align across different sections?
- Are there contradictory statements about the same project?
- Does the narrative match linked sources?
- Are abbreviations and acronyms consistent?

## Step 8: Red flags scan

Actively investigate these patterns:
- [ ] Round numbers without source (e.g. "improved by 50%" with no citation)
- [ ] Superlatives without evidence ("first ever," "fastest," "best")
- [ ] Vague timeframes ("recently," "soon," "earlier this quarter")
- [ ] Claims about others' work without their confirmation
- [ ] Metrics that seem unusually high or inconsistent with prior data
- [ ] Projects mentioned that aren't reflected in Slack/PR history
- [ ] Dates that fall outside the review period
- [ ] Technical achievements that seem implausible given the timeframe

## Step 9: Output findings

For each issue found, report:

1. **The claim** — quote the exact statement from the draft
2. **Why it's questionable** — what raised a red flag
3. **Verification result** — what you found (or couldn't find) in Slack
4. **Suggested revision** — how to fix it (add citation, reword, correct the fact)

Categorize findings by severity:
- **Incorrect** — factually wrong, must be fixed
- **Unverified** — couldn't confirm, needs citation or rewording
- **Imprecise** — technically true but misleading or vague, should be tightened
- **Attribution issue** — credit or ownership is misrepresented

## Step 10: Summary

Close with:
- **Total claims checked**: N
- **Verified**: N (with existing citations)
- **Verified**: N (citations confirmed accurate)
- **Issues found**: N incorrect / N unverified / N imprecise / N attribution
- **Overall assessment**: Highly accurate / Mostly accurate with gaps / Needs significant corrections
- **Top 3 fixes**: The most important corrections to make

Print all findings to the console. Do not modify the original document.
