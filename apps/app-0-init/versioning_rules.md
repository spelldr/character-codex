# Versioning Rules

Canonical Standards for Version Control
Maintained by Patch Governance Office

---

## 1. Purpose
This document defines the **canonical versioning rules** for all Patch‑universe artifacts, including:

- Character codices
- Avatar codices
- JSON manifests
- Schemas
- Governance documents
- Flow definitions
- Templates

These rules ensure deterministic evolution, traceability, and zero drift.

---

## 2. Version Format
All artifacts must use the following semantic structure:

```
MAJOR.MINOR
```

### 2.1 MAJOR Version
Increment when:
- A schema changes
- A field is added or removed
- A structural rule changes
- A character or avatar ontology changes
- A governance rule changes
- A flow definition changes

### 2.2 MINOR Version
Increment when:
- Content is clarified
- Wording is improved
- Examples are added
- Non‑breaking corrections are made
- Visual or behavioral notes are refined
- Metadata is updated

---

## 3. Approval Requirements

### 3.1 Minor Version Changes
May be approved by:
- Patch Governance Office
- Gordon, PPM

### 3.2 Major Version Changes
Require:
- Patch Governance Office approval
- Explicit justification
- Updated schema (if applicable)
- Updated flow documentation (if applicable)

No major version change may occur without a corresponding governance note.

---

## 4. Versioning Rules by Artifact Type

### 4.1 Characters
- Must increment MAJOR when identity, constraints, or ontology change
- Must increment MINOR when descriptive content changes

### 4.2 Avatars
- Must increment MAJOR when platform rules or avatar ontology change
- Must increment MINOR when deviations or rendering guidelines change

### 4.3 Schemas
- Must increment MAJOR for any structural change
- Must increment MINOR for clarifications or comments

### 4.4 Governance Documents
- Must increment MAJOR when rules change
- Must increment MINOR when examples or explanations change

### 4.5 Templates
- Must increment MAJOR when template structure changes
- Must increment MINOR when formatting or comments change

---

## 5. Changelog Requirements
Every version increment must include:

- Version number
- Date
- Summary of changes
- Approver
- Impact assessment (breaking / non‑breaking)

Changelogs must be stored adjacent to the artifact or embedded within it.

---

## 6. Enforcement
The Patch Governance Office is responsible for:

- Reviewing all version increments
- Rejecting improper version changes
- Ensuring consistency across artifacts
- Maintaining the canonical version registry

No artifact may be considered canonical without an approved version.

---

## 7. Versioning Metadata
All artifacts must include:

- **version**
- **status**
- **last_updated**
- **maintainer**

These fields must be updated with every version increment.

---

## 8. Versioning Philosophy
Version numbers are not decorative.
They are **operational signals** that communicate:

- Stability
- Compatibility
- Intent
- Change impact

Versioning is a governance tool, not a narrative one.

---

## 9. Current Version
**Versioning Rules Version:** 1.0
**Status:** Canonical
**Last Updated:** 2026‑02‑16
**Maintainer:** Patch Governance Office

If you'd like me to continue, the next file is:

**`governance/drift_management.md`**