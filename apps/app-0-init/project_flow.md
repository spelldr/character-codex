# Project Flow

Canonical Cross‑Project Structure
Maintained by Patch Governance Office

---

## 1. Purpose
This document defines the **canonical project flow** within the Patch ecosystem.
It establishes how primary characters, platform avatars, and institutional layers relate in terms of operational sequencing, influence, and dependency.

This file is **not** a narrative artifact.
It is an **operational contract**.

---

## 2. Core Principles

### 2.1 No Hardcoded Directionality
Project flow must **not** assume a universal upstream/downstream hierarchy between platforms.
Flows may vary by context, campaign, or instructional purpose.

### 2.2 DAG‑Based Structure
All flows must form a **Directed Acyclic Graph (DAG)**:
- No cycles
- No self‑references
- No infinite recursion
- Unlimited branching
- Unlimited cross‑platform references

### 2.3 Characters Are Roots
Primary characters (Patch, Kuber Netty, Gordon) serve as **root nodes**.
Avatars and institutions derive from them but never supersede them.

### 2.4 Avatars Are Platform‑Bound
Avatars:
- Represent a single primary character
- Are bound to a single platform
- May reference other avatars
- Must not form cycles

### 2.5 Institutions Are Non‑Narrative
Institutions (e.g., Patch Governance Office) enforce structure but do not participate in narrative flow.

---

## 3. Canonical Flow Definition (Current)

### 3.1 Root Layer
- **Patch** — Root Orchestration Layer
- **Gordon, PPM** — Governance Layer
- **Kuber Netty** — Instructional Layer

### 3.2 Platform Avatars
- **Patreon Avatar** — Long‑form instructional representation
- **TikTok Avatar** — Short‑form instructional representation

### 3.3 Allowed Avatar Relationships
Examples of valid DAG‑based references:
- TikTok Avatar → Patreon Avatar
- Patreon Avatar → TikTok Avatar
- Either → Future Avatars (e.g., YouTube, Website)

### 3.4 Forbidden Structures
- A → B → A
- A → A
- A → B → B
- Any cycle, direct or indirect

---

## 4. Flow Examples

### 4.1 Instructional Funnel (Example)
```
Kuber Netty
 ├── Patreon Avatar
 └── TikTok Avatar → Patreon Avatar
```

### 4.2 Cross‑Platform Echo (Example)
```
Kuber Netty
 ├── TikTok Avatar
 └── Patreon Avatar → TikTok Avatar
```

### 4.3 Multi‑Avatar Expansion (Future‑Safe)
```
Kuber Netty
 ├── Patreon Avatar
 ├── TikTok Avatar
 └── YouTube Avatar → Patreon Avatar → TikTok Avatar
```

All examples remain DAG‑compliant.

---

## 5. Governance Rules

### 5.1 Patch Governance Office Responsibilities
- Validate all flows
- Prevent cycles
- Approve new avatar relationships
- Maintain flow documentation

### 5.2 Update Requirements
Any change to:
- primary characters
- avatar relationships
- platform definitions
- institutional structure

must be reviewed and approved before becoming canonical.

---

## 6. Versioning
**Flow Version:** 1.0
**Status:** Canonical
**Last Updated:** 2026‑02‑16
**Maintainer:** Patch Governance Office

If you'd like me to continue, the next file is:

**`governance/versioning_rules.md`**