# {{ platform | title }} Avatar  
Public-Facing Humanoid Representation of {{ primary_character }}

![[{{ json_filename }}]]

---

## 1. Purpose
This avatar represents the public-facing, platform-specific manifestation of **{{ primary_character }}** on **{{ platform }}**.  
It is a **secondary, background humanoid figure** that mirrors the primary character while maintaining a consistent, intentional deviation known as the **tell**.

The avatar is **not** a full character.  
It is a **representational interface layer**.

---

## 2. Identity
**Platform:** {{ platform }}  
**Primary Character:** {{ primary_character }}  
**Avatar Type:** Platform-Bound Humanoid Shapeshifter  
**Tell:** {{ tell }}  
**Energy:** {{ energy }}

---

## 3. Visual Deviations
{% for item in visual_deviations %}
- {{ item }}
{% endfor %}

---

## 4. Behavioral Deviations
{% for item in behavioral_deviations %}
- {{ item }}
{% endfor %}

---

## 5. Platform Constraints
{% for item in constraints %}
- {{ item }}
{% endfor %}

---

## 6. Rendering Guidelines
{% for item in rendering_guidelines %}
- {{ item }}
{% endfor %}

---

## 7. Notes
{{ notes }}

---

## 8. Versioning
**Avatar Codex Version:** {{ version }}  
**Status:** {{ status }}  
**Last Updated:** {{ last_updated }}  
**Maintainer:** Patch Governance Office

=======================================

Here is the **Avatar JSON Manifest Template**, built to match the structure and rigor of your character JSON template while respecting the *strict limitations* of avatars as secondary, platform‑bound, non‑autonomous entities.

This is the file you will save as:

```
characters/avatar_template.json.jinja
```

It is:

- deterministic  
- VS Code–legible  
- Jinja‑safe  
- schema‑aligned  
- avatar‑appropriate (no personality, no archetype, no narrative function, etc.)  

And it follows the **Markdown‑first, JSON‑second** precedent of your character codex system.

---

# ✅ **AVATAR JSON MANIFEST TEMPLATE (JINJA)**

```jinja
{
  "platform": "{{ platform }}",
  "primary_character": "{{ primary_character }}",

  "tell": "{{ tell }}",

  "visual_deviations": [
  {% for item in visual_deviations %}
    "{{ item }}"{% if not loop.last %},{% endif %}
  {% endfor %}
  ],

  "behavioral_deviations": [
  {% for item in behavioral_deviations %}
    "{{ item }}"{% if not loop.last %},{% endif %}
  {% endfor %}
  ],

  "constraints": [
  {% for item in constraints %}
    "{{ item }}"{% if not loop.last %},{% endif %}
  {% endfor %}
  ],

  "rendering_guidelines": [
  {% for item in rendering_guidelines %}
    "{{ item }}"{% if not loop.last %},{% endif %}
  {% endfor %}
  ],

  "notes": "{{ notes }}",

  "version": "{{ version }}",
  "status": "{{ status }}",
  "last_updated": "{{ last_updated }}"
}
```

---

## Why this template is correct

### ✔ Mirrors your character JSON structure  
But only includes fields avatars are *allowed* to have.

### ✔ Enforces avatar ontology  It has 
- Bound to a single platform  
- Bound to a single primary character  
- Must have a tell  
- Must list deviations  
- Must follow platform constraints  
- Must remain non‑autonomous

### ✔ No forbidden fields  
Avatars **cannot** have:

- personality  
- archetype  
- tone  
- responsibilities  
- capabilities  
- narrative function  
- email signature  
- relationships  

This template prevents drift by design.

---

If you want, I can now generate **Patreon’s avatar** or **TikTok’s avatar** using this schema and the Markdown template you approved.