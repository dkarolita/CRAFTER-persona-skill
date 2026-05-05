# CRAFTER Persona Method

## Purpose

Use the CRAFTER method to create personas that are useful for requirements engineering, UX research, product discovery, and human-centered design. The method is designed to reduce generic LLM persona output by combining human input, contextual evidence, taxonomy-guided factors, and structured review.

## Principles

- Keep humans in the loop. The user chooses the domain, context, and important persona characteristics.
- Ground the persona in evidence. Use research notes, interviews, surveys, reviews, support tickets, or domain summaries when available.
- Separate internal and external factors. Balance personal traits with environment and system-use context.
- Always capture motivation, goals, and pain points as minimum human characteristics.
- Distinguish internal and external motivations, goals, and pain points when evidence allows.
- Explain relationships between human aspects instead of treating taxonomy fields as isolated boxes.
- Use role-play prompting. The GenAI tool should act as a persona researcher, requirements analyst, or UX researcher.
- Use one-shot or template guidance. Give a clear target structure so generated personas are consistent.
- Output structured data first, then produce the user-selected artifact format.
- Review for realism. Check for vague, over-polished, stereotyped, or unsupported claims.

## Inputs

Collect these inputs before generation:

- `domain`: The domain, industry, or problem space.
- `target_user_group`: The user group represented by the persona.
- `goal`: Why this persona is being created.
- `context`: Evidence or background knowledge.
- `internal_factors`: Selected traits, motivations, abilities, emotions, goals, fears, preferences, and knowledge.
- `external_factors`: Selected environment, technology, social, organizational, cultural, policy, economic, or task constraints.
- `language`: Output language.
- `detail_level`: Short, medium, or long.
- `output_format`: JSON, DOCX, PDF, Markdown, or PPT/PPTX.
- `known_assumptions`: Assumptions that should be labeled rather than treated as facts.

## Internal Layer

Internal factors describe general information about the represented individual:

- Goals and motivations
- Needs and expectations
- Frustrations and fears
- Confidence and self-efficacy
- Skills and digital literacy
- Habits and routines
- Prior knowledge
- Accessibility needs
- Emotional state
- Decision criteria
- Internal motivation
- Internal goals
- Internal pain points

## External Layer

External factors describe context-specific information about the represented individual:

- Physical environment
- Social support or social pressure
- Work, school, family, or community setting
- Device and connectivity access
- Organizational rules
- Legal or policy constraints
- Cost and time constraints
- Cultural expectations
- Service touchpoints
- Task frequency and urgency
- External motivation
- External goals
- External pain points

The external layer should be customized to the domain and project. The same facet can carry different meanings in different domains.

## Minimum Human Characteristics

Every CRAFTER persona should include:

- **Motivation**: why the represented individual acts, accepts, avoids, or prioritizes something.
- **Goals**: what the represented individual wants to achieve.
- **Pain points**: problems, pressures, frustrations, concerns, or obstacles the represented individual wants solved or avoided.

Capture each characteristic in internal and external forms when possible:

- Internal motivation/goals/pain points: broader life, personal, emotional, confidence, capability, or value-based drivers and tensions.
- External motivation/goals/pain points: project-, task-, environment-, organization-, policy-, technology-, or domain-specific drivers and tensions.

Explain how the internal and external forms relate to each other.

## Generation Procedure

1. Restate the task and persona purpose.
2. Summarize the provided evidence.
3. Select the most relevant internal and external factors.
4. Identify motivation, goals, and pain points.
5. Separate internal and external forms of motivation, goals, and pain points when possible.
6. Generate a persona with narrative, bullet, and mixed views.
7. Include a short quote that captures the persona's key tension.
8. Include the taxonomy object that records the factors used.
9. Label assumptions.
10. Run a quality review and revise if needed.
11. Present the final result in the requested format.

## Quality Review

Check:

- Specificity: Replace generic phrases with concrete behaviors and constraints.
- Grounding: Tie important claims to supplied evidence or mark them as assumptions.
- Minimum content: Ensure motivation, goals, and pain points are present.
- Layer clarity: Ensure internal/general and external/context-specific aspects are separated.
- Relationships: Explain how motivations, goals, pain points, and external constraints interact.
- Realism: Avoid making the persona too perfect, too helpless, or too neatly aligned with the product.
- Diversity without stereotyping: Include context-sensitive nuance without reducing people to demographic labels.
- Requirements usefulness: Make needs, constraints, and design implications visible.
- Narrative quality: Include behavioral cues, tradeoffs, and tensions.

## Common Failure Modes

- Overly generic persona with no domain-specific details.
- Persona reads like a product marketing target segment instead of a human.
- Traits are idealized or internally inconsistent.
- Persona includes unsupported demographic or psychological claims.
- Output does not explain implications for requirements or design.
- The external context is missing, so user behavior appears purely individual.

## Refinement Moves

- Add first-person quote or short scenario.
- Add one concrete day-in-the-life moment.
- Add constraints from the external layer.
- Add emotional or social tension.
- Add design implications and requirement cues.
- Remove unsupported sensitive attributes.
- Split into multiple personas if one persona is carrying conflicting user types.

## Output Formats

The final persona should be easy for researchers, designers, students, and stakeholders to use. Keep JSON as the structured source and adapt the presentation to the requested format.

Use JSON when the user needs machine-readable output. Use readable sections when producing DOCX, PDF, Markdown, or slides:

1. Persona name, domain, and target user group
2. Quote
3. Executive summary
4. Narrative
5. Bullet summary
6. Mixed persona view with design implications
7. Internal taxonomy factors
8. External taxonomy factors
9. Motivation, goals, and pain points
10. Relationships between internal and external factors
11. Requirements insights
12. Assumptions and evidence notes
13. Quality review

For PPT/PPTX, split the content into a small deck:

1. Persona overview
2. Persona story and quote
3. Internal and external factors
4. Requirements/design insights
5. Assumptions and quality review

Keep raw JSON as a source format unless JSON is the requested final output.
