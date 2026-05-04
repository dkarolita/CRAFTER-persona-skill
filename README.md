# CRAFTER Persona Skill

An open-source, platform-neutral skill for creating user personas using the CRAFTER 2.0 workflow and thinking.

CRAFTER 2.0 is an LLM-powered persona creation approach that combines human input, context grounding, internal and external taxonomy factors, role-play prompting, structured persona output, and quality review.

## What This Skill Helps With

- Create user personas for requirements engineering, UX research, product discovery, service design, and human-centered design.
- Structure persona inputs using internal and external factors.
- Ground generated personas in interviews, survey summaries, research notes, reviews, or domain context.
- Produce structured persona outputs with narrative, bullet, mixed, quote, taxonomy, assumptions, and quality review.
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
```

## Files

- `SKILL.md`: Main skill instructions.
- `references/crafter-method.md`: CRAFTER workflow, quality criteria, and refinement guidance.
- `references/prompt-template.md`: Portable prompt template for any GenAI tool.
- `agents/openai.yaml`: Codex UI metadata.
- `LICENSE`: MIT license.

## License

MIT License.
