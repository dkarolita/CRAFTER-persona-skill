---
name: crafter-persona
description: Create high-quality user personas using the CRAFTER 2.0 workflow and thinking. Use when Codex or another GenAI tool needs to generate, critique, refine, or structure personas for requirements engineering, UX research, product discovery, service design, or human-centered design using taxonomy-guided internal/external factors, context grounding, role-play prompting, one-shot style guidance, human-in-the-loop refinement, and structured persona outputs.
---

# CRAFTER Persona

## Overview

Use this skill to create personas with the CRAFTER 2.0 method, independent of any specific app, model, or platform. The method combines human input, domain grounding, taxonomy-guided persona characteristics, role-play prompting, optional retrieved/context documents, structured JSON output, and quality review for realism and usefulness.

## First Steps

1. Identify the persona purpose: requirements elicitation, product discovery, UX design, service design, evaluation, or another use.
2. Ask for or infer the domain, target user group, available evidence, and desired output language.
3. Gather human-provided context before generating: research notes, interviews, survey summaries, stakeholder assumptions, product constraints, market/domain facts, or usage scenarios.
4. Separate persona factors into internal and external layers.
5. Generate a structured persona, then critique and refine it for specificity, realism, and lack of stereotypes.

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

### 4. Generate Structured Persona

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

## Output Shape

Prefer JSON or Markdown plus JSON. The default JSON keys are:

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

## Platform Adaptation

This skill can be used in any GenAI tool. If the tool does not support skills, paste the content of `SKILL.md` and the prompt template into the system/developer instruction area, then provide the persona context as the user message.
