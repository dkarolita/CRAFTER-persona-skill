# Portable CRAFTER Prompt Template

Use this prompt in any GenAI tool. Replace bracketed fields before running.

```text
You are a persona researcher and requirements analyst. Create a realistic persona using the CRAFTER workflow.

Goal:
[Explain why the persona is needed.]

Domain:
[Domain or industry.]

Target user group:
[Who the persona should represent.]

Language:
[Output language.]

Detail level:
[short | medium | long]

Evidence and context:
[Paste interviews, survey findings, user reviews, research notes, domain facts, stakeholder assumptions, product context, or write "No direct evidence available".]

Internal factors to consider:
[List selected goals, motivations, emotions, habits, skills, fears, accessibility needs, knowledge, decision criteria, etc.]

External factors to consider:
[List selected environment, device access, social context, policy, cost, culture, task setting, time pressure, organizational constraints, etc.]

Instructions:
1. Use the evidence as grounding. Do not invent unsupported facts. If needed, add assumptions in an assumptions list.
2. Balance internal and external factors.
3. Avoid stereotypes, generic traits, and overly idealized behavior.
4. Create a persona that is useful for requirements engineering, UX research, or product design decisions.
5. Return JSON only using this structure:

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
    "internal": [
      { "name": "...", "title": "...", "description": "..." }
    ],
    "external": [
      { "name": "...", "title": "...", "description": "..." }
    ]
  },
  "assumptions": [
    "..."
  ],
  "requirements_insights": [
    "..."
  ],
  "quality_review": {
    "grounding": "...",
    "realism": "...",
    "risks": [
      "..."
    ],
    "refinement_suggestions": [
      "..."
    ]
  }
}
```

## Follow-Up Refinement Prompt

```text
Review the persona below using the CRAFTER quality criteria. Improve realism, specificity, grounding, and usefulness for requirements/design. Keep the same JSON structure. Mark any unsupported claims as assumptions.

Persona:
[Paste persona JSON]

Additional evidence or correction:
[Paste new context, or write "None"]
```
