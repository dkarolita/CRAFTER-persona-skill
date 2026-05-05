---
name: crafter-persona
description: Create high-quality user personas using the CRAFTER 2.0 workflow and thinking with user-selectable outputs such as JSON, DOCX, PDF, Markdown, or PPT/PPTX. Use when Codex or another GenAI tool needs to generate, critique, refine, or structure personas for requirements engineering, UX research, product discovery, service design, or human-centered design using taxonomy-guided internal/external factors, context grounding, role-play prompting, one-shot style guidance, human-in-the-loop refinement, structured persona data, and user-friendly artifacts.
---

# CRAFTER Persona

## Overview

Use this skill to create personas with the CRAFTER 2.0 method, independent of any specific app, model, or platform. The method combines human input, domain grounding, taxonomy-guided persona characteristics, role-play prompting, optional retrieved/context documents, structured persona data, format-specific presentation, and quality review for realism and usefulness.

## First Steps

1. Identify the persona purpose: requirements elicitation, product discovery, UX design, service design, evaluation, or another use.
2. Ask for or infer the domain, target user group, available evidence, and desired output language.
3. Gather human-provided context before generating: research notes, interviews, survey summaries, stakeholder assumptions, product constraints, market/domain facts, or usage scenarios.
4. Separate persona factors into internal and external layers.
5. Generate a structured persona, critique and refine it, then produce the requested output format.

## CRAFTER Workflow

### 1. Frame The Persona Task

Define:

- Domain or industry
- Product, service, system, or research context
- Target user group
- Design or requirements question the persona should help answer
- Persona language
- Desired detail level: short, medium, or long

### 2. Build Context Grounding

Use evidence when available. Good sources include:

- Interview excerpts
- Survey summaries
- Observation notes
- User reviews
- Helpdesk tickets
- Domain reports
- Stakeholder notes
- Existing personas or journey maps

When evidence is missing, mark assumptions clearly and avoid presenting invented details as facts.

### 3. Select Taxonomy Factors

Use two layers:

- Internal layer: traits inside the person, such as goals, motivations, fears, confidence, habits, capabilities, accessibility needs, emotions, prior knowledge, and decision criteria.
- External layer: surrounding context, such as environment, devices, social support, organizational constraints, culture, policies, budget, time pressure, infrastructure, and task setting.

Choose only factors that matter for the current design or requirements problem.

### 4. Generate Structured Persona Data

Use role-play prompting: act as a persona researcher or requirements analyst. Use the user's context as grounding. Produce three complementary views:

- Narrative: a coherent human story.
- Bullet summary: scannable traits, needs, goals, frustrations, and constraints.
- Mixed format: narrative plus structured design implications.

Also include a short quote and a machine-readable taxonomy object.

For a reusable prompt, read `references/prompt-template.md`.

### 5. Review And Refine

Critique the persona before finalizing:

- Is it grounded in provided evidence?
- Does it avoid generic, idealized, or stereotyped traits?
- Does it include concrete goals, constraints, behaviors, and context?
- Does it help elicit or evaluate requirements?
- Does it show enough narrative richness to feel like a plausible person?
- Are assumptions labeled?

For the full method and output schema, read `references/crafter-method.md`.

### 6. Produce The Requested Output

Ask for the user's preferred output format when it is not specified. Supported output options:

- `json`: Best for APIs, databases, repeatable evaluation, and downstream conversion.
- `docx`: Best for reading, reviewing, sharing with stakeholders, and coursework/research deliverables.
- `pdf`: Best for fixed-layout sharing, submission, and printing.
- `ppt` or `pptx`: Best for presenting one or more personas in workshops, classes, or stakeholder meetings.
- `md` or Markdown: Best when the tool cannot create files but the user wants readable text.

Always create or preserve structured persona data first. Then render it into the selected format.

For readable document formats, use this order:

1. Persona title, domain, and target user group
2. Short quote
3. Overview box or summary
4. Narrative persona story
5. Key goals, needs, frustrations, and constraints
6. Internal factors
7. External factors
8. Requirements or design insights
9. Assumptions and evidence notes
10. Quality review

For JSON output, return only the structured JSON unless the user asks for explanation.

For DOCX output in Codex or another coding environment, save the structured JSON first, then convert it with:

```bash
python3 scripts/persona_json_to_docx.py persona.json persona.docx
```

For PDF output, create DOCX or Markdown first, then export/convert to PDF using the available toolchain. If conversion is unavailable, provide print-ready Markdown.

For PPT/PPTX output, create concise slide content: one overview slide, one persona story slide, one taxonomy slide, one requirements/design insights slide, and one assumptions/quality slide. Keep each slide scannable.

When running in a GenAI tool that cannot create files, output clean Markdown and state which requested file format it is ready to be copied into.

## Structured Source Shape

Use structured data as the source of truth before making the DOCX. The default JSON keys are:

```json
{
  "result": {
    "narrative": "...",
    "bullets": "...",
    "mixed": "...",
    "quote": "...",
    "full_name": "..."
  },
  "taxonomy": {
    "domain": { "key": "...", "label": "..." },
    "detail": "...",
    "internal": [],
    "external": []
  },
  "assumptions": [],
  "quality_review": {
    "grounding": "...",
    "realism": "...",
    "risks": [],
    "refinement_suggestions": []
  }
}
```

If integrating with the original CRAFTER 2.0 application contract, use `narative` instead of `narrative`.

## Format Style Guidance

Keep user-facing artifacts easy to scan:

- Use clear headings.
- Keep paragraphs short.
- Use bullets for goals, needs, frustrations, constraints, and insights.
- Put internal and external taxonomy factors in separate sections.
- Include assumptions and quality review so readers can judge trustworthiness.
- Avoid dumping raw JSON into document, PDF, or slide outputs unless the user requests it.
- For slides, prefer concise bullets and strong section titles over long paragraphs.

## Platform Adaptation

This skill can be used in any GenAI tool. If the tool does not support skills, paste the content of `SKILL.md` and the prompt template into the system/developer instruction area, then provide the persona context as the user message. Specify the desired output format: JSON, DOCX, PDF, Markdown, or PPT/PPTX.
