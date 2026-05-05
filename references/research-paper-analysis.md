# Academic Analysis Of The Persona Taxonomy Paper

## Citation

Karolita, D., Grundy, J., Kanij, T., Obie, H., & McIntosh, J. (2023). What's in a Persona? A Preliminary Taxonomy from Persona Use in Requirements Engineering. In *Proceedings of the 18th International Conference on Evaluation of Novel Approaches to Software Engineering - ENASE*. https://doi.org/10.5220/0011708500003464

This CRAFTER skill also draws on the extended-paper manuscript in which the taxonomy is further evaluated with practitioner feedback.

## Research Question And Significance

The paper investigates what human factors are commonly represented in personas used for requirements engineering, how those factors can be organized into a preliminary persona taxonomy, and whether practitioners find the taxonomy useful for persona creation and presentation.

This matters because personas are widely used in requirements engineering, but persona presentation is not standardized. Prior persona layers and templates often lacked clear guidance about which human factors belong where, and many were not designed specifically for requirements-engineering contexts.

## Methodology

- **Design**: Corpus analysis followed by practitioner evaluation.
- **Dataset**: 98 concrete personas collected from 41 academic publications.
- **Source selection**: Publications were identified from six academic databases and filtered to include papers with concrete persona examples.
- **Domain coverage**: Personas were grouped across 12 domains, including technology for older adults, software development, health, education, sustainable living, culture, technology for children, architecture, finance, law, security, and transportation.
- **Analysis**: Human factors were extracted from persona descriptions, grouped into facets, mapped to broader human-aspect groups, and organized into internal and external persona layers.
- **Evaluation**: 20 software practitioners reviewed the taxonomy and domain-based customization approach and provided feedback.

## Key Findings

1. Text-based personas vary by narration, format, and length. The corpus included narrative and bullet-point personas, unstructured/semi-structured/structured formats, and normal-length or brief personas.
2. Persona information can be usefully separated into internal and external layers. The internal layer captures general information about the represented individual; the external layer captures context- and domain-specific information.
3. Motivation, goals, and pain points are essential persona attributes. Practitioners viewed them as central to understanding behavior, identifying objectives, and recognizing problems users want solved or avoided.
4. Motivation, goals, and pain points should be differentiated internally and externally when possible. Internal versions describe broader human drivers and tensions; external versions describe project-, task-, domain-, or environment-specific drivers and tensions.
5. The relationships between human aspects matter. Practitioners emphasized that taxonomy facets are not independent boxes; factors such as culture, education, technology use, goals, and pain points can influence one another.
6. Practitioners valued concise, well-structured personas, especially bullet-point or structured presentations. However, overly brief personas may remove important context and invite unintended assumptions.

## Significance For CRAFTER

CRAFTER should not only produce a polished persona. It should guide the persona creation process by:

- prompting for both internal and external information;
- requiring motivation, goals, and pain points;
- asking whether each minimum characteristic has internal and external versions;
- explaining how internal and external factors relate;
- customizing external factors to the domain and project context;
- labeling assumptions clearly;
- supporting multiple presentation formats for different audiences.

## Limitations

- The taxonomy is based on personas found in published academic work, so it may not represent all industry persona practices.
- Some domains had fewer collected examples, limiting confidence about domain-specific recommendations.
- Practitioner feedback indicates usefulness, but the taxonomy still needs further empirical validation as a persona creation and evaluation tool.
- Presentation preferences may vary by audience, task, and organizational setting.

## Future Directions

- Evaluate the taxonomy and domain-based customization approach in real persona creation tasks.
- Study how different audiences need different persona detail levels and formats.
- Further investigate relationships between internal and external motivation, goals, and pain points.
- Use the taxonomy as a review/evaluation checklist for generated personas.
- Develop persona generation tools that recommend relevant human factors while allowing users to add, remove, or revise fields.
