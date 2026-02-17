# The Codex

Canonical Documentation for the Patch Universe

This repository contains the **canonical, deterministic, schema‑aligned documentation system** for the Patch universe.
All characters, avatars, institutions, schemas, governance rules, and flows are defined here as **operational contracts**, not narrative artifacts.

The structure is intentionally minimal, file‑oriented, and designed for reproducibility across tools such as Obsidian, VS Code, and Jinja‑based renderers.

---

## 1. Repository Structure

```
characters/        # Character codices, avatar codices, and institutional definitions
schemas/           # JSON schemas for validation
flow/              # Canonical project flow definitions
governance/        # Versioning rules, drift management, and governance standards
indexes/           # Index files (optional, generated as needed)
```

Each directory contains deterministic Markdown and JSON files that define the universe’s structure.

---

## 2. Characters

Characters are **primary entities** with full identity, responsibilities, constraints, and narrative function.  
Each character has:

- a Markdown codex (`.md`)  
- a JSON manifest (`.json`)  
- a strict schema (`schemas/character.schema.json`)  
- an embedded reference to its JSON file  

Characters currently defined:

- Patch  
- Gordon, PPM  
- Kuber Netty  

Characters must always be created using the canonical Jinja templates:

```
characters/character_template.md.jinja
characters/character_template.json.jinja
```

---

## 3. Avatars

Avatars are **platform‑bound humanoid shapeshifters** that represent a primary character on a specific platform.  
They are **not** full characters and must not develop personality, autonomy, or narrative function.

Each avatar has:

- a Markdown codex  
- a JSON manifest  
- a strict schema (`schemas/avatar.schema.json`)  

Avatars currently defined:

- Patreon Avatar (for Kuber Netty)  
- TikTok Avatar (for Kuber Netty)  

Avatars must always be created using:

```
characters/avatar_template.md.jinja
characters/avatar_template.json.jinja
```

---

## 4. Institutions

Institutions are **non‑anthropomorphic governance bodies**.  
They enforce structure but do not participate in narrative.

Current institution:

- Patch Governance Office

Schema:

```
schemas/institution.schema.json
```

---

## 5. Schemas

All JSON manifests must validate against the schemas in:

```
schemas/
```

Schemas currently defined:

- `character.schema.json`  
- `avatar.schema.json`  
- `institution.schema.json`  

Schemas define the canonical structure and prevent drift.

---

## 6. Governance

Governance documents define the rules that maintain determinism and prevent drift.

Current governance files:

- `governance/versioning_rules.md`  
- `governance/drift_management.md`  

These documents define:

- semantic versioning rules  
- drift detection and correction  
- schema discipline  
- template discipline  
- flow discipline  

---

## 7. Project Flow

The canonical project flow is defined in:

```
flow/project_flow.md
```

This file establishes:

- DAG‑based flow rules  
- avatar relationship constraints  
- character root‑node structure  
- platform‑specific boundaries  

No cycles are permitted.

---

## 8. Templates

All characters and avatars must be generated using the templates in:

```
characters/character_template.md.jinja
characters/character_template.json.jinja
characters/avatar_template.md.jinja
characters/avatar_template.json.jinja
```

Templates ensure:

- schema alignment  
- deterministic formatting  
- zero drift  
- reproducible generation  

---

## 9. Versioning

Every artifact includes:

- `version`  
- `status`  
- `last_updated`  
- `maintainer`  

Versioning rules are defined in:

```
governance/versioning_rules.md
```

---

## 10. Drift Management

Drift is any deviation from:

- schema  
- ontology  
- templates  
- flow  
- constraints  
- governance doctrine  

Drift rules are defined in:

```
governance/drift_management.md
```

---

## 11. Contribution Rules

All changes must:

- validate against schemas  
- follow versioning rules  
- maintain DAG‑compliant flows  
- avoid narrative contamination  
- preserve deterministic formatting  
- be approved by the Patch Governance Office  

---

## 12. Status

This repository is **canonical** and represents the authoritative structure of the Patch universe.

```
Repository Version: 1.0
Maintainer: Patch Governance Office
