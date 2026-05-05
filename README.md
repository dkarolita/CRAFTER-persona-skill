# CRAFTER Persona Skill

An open-source, platform-neutral skill for creating user personas using the CRAFTER 2.0 workflow and thinking. Users can choose the output format they prefer: JSON, DOCX, PDF, Markdown, or PPT/PPTX.

CRAFTER 2.0 is an LLM-powered persona creation approach that combines human input, context grounding, internal and external taxonomy factors, role-play prompting, structured persona data, readable artifacts, and quality review.

## What This Skill Helps With

- Create user personas for requirements engineering, UX research, product discovery, service design, and human-centered design.
- Structure persona inputs using internal and external factors.
- Ground generated personas in interviews, survey summaries, research notes, reviews, or domain context.
- Produce personas as JSON, DOCX, PDF, Markdown, or presentation-ready slide content.
- Adapt the CRAFTER workflow to Codex, ChatGPT, Claude, Gemini, Copilot, or another GenAI tool.

## Use In Codex

Copy this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R crafter-persona ~/.codex/skills/crafter-persona
```

Then ask Codex:

```text
Use the CRAFTER Persona skill to create a persona for elderly users of a mobile health app in Indonesia.
```

When Codex can create files, ask:

```text
Create the final persona as a DOCX file.
```

Or choose another format:

```text
Create the persona as JSON.
Create the persona as a PDF.
Create the persona as a PPTX presentation.
```

## Use In Any GenAI Tool

If your AI tool does not support Codex skills, open:

- `SKILL.md`
- `references/prompt-template.md`

Paste the prompt template into your AI tool and fill in:

```text
Domain:
Target user group:
Goal:
Evidence and context:
Internal factors:
External factors:
Language:
Detail level:
```

If the tool supports file generation, ask it to create your preferred format. If it does not, ask for Markdown that is ready to copy into Word, Google Docs, slides, or another editor.

## Example

```text
Use the CRAFTER workflow to create a persona.

Domain: Digital health
Target user group: Older adults in Indonesia using a medication reminder app
Goal: Identify requirements for improving trust and daily use
Evidence and context: Users may rely on family support, have limited digital confidence, and worry about forgetting medication.
Internal factors: motivation, health anxiety, daily routines, digital literacy
External factors: family support, smartphone access, internet reliability, clinic advice
Language: English
Detail level: medium
Output format: DOCX
```

## Output Format Options

- `JSON`: Best for developers, APIs, databases, or later conversion.
- `DOCX`: Best for reading and stakeholder review.
- `PDF`: Best for fixed sharing or submission.
- `PPT/PPTX`: Best for workshops, presentations, and classroom discussion.
- `Markdown`: Best when the AI tool cannot create files.

## Convert Persona JSON To DOCX

If you have a persona JSON file, use the bundled converter:

```bash
python3 scripts/persona_json_to_docx.py persona.json persona.docx
```

The script uses only Python's standard library, so it does not require installing extra packages.

## Files

- `SKILL.md`: Main skill instructions.
- `references/crafter-method.md`: CRAFTER workflow, quality criteria, and refinement guidance.
- `references/prompt-template.md`: Portable prompt template for any GenAI tool.
- `scripts/persona_json_to_docx.py`: Convert structured persona JSON into a readable DOCX file.
- `agents/openai.yaml`: Codex UI metadata.
- `LICENSE`: MIT license.

## License

MIT License.
