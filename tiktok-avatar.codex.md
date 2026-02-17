Here is **TikTok’s Avatar**, built with the same rigor and constraints as Patreon’s — but tuned for TikTok’s fast‑paced, high‑contrast, short‑form environment.

It follows every rule:

- humanoid  
- platform‑bound  
- shapeshifter  
- resembles the primary (Netty)  
- never a perfect match  
- has a **tell**  
- permanently bound to Netty  
- secondary, background, non‑autonomous  
- no personality, no narrative function, no responsibilities  

And it uses the **Markdown‑first, JSON‑second** pattern you established.

---

# 📄 **`characters/tiktok-avatar.md`**

```markdown
# TikTok Avatar  
Public-Facing Humanoid Representation of Kuber Netty

![[tiktok-avatar.json]]

---

## 1. Purpose
This avatar represents the public-facing, platform-specific manifestation of **Kuber Netty** on **TikTok**.  
It is a **secondary, background humanoid figure** that mirrors the primary character while maintaining a consistent, intentional deviation known as the **tell**.

The avatar is **not** a full character.  
It is a **representational interface layer**.

---

## 2. Identity
**Platform:** TikTok  
**Primary Character:** Kuber Netty  
**Avatar Type:** Platform-Bound Humanoid Shapeshifter  
**Tell:** Shadow lags behind by a fraction of a second during movement  
**Energy:** Fast, punchy, high‑contrast instructional presence

---

## 3. Visual Deviations
- Sharper facial features than Netty  
- Slightly exaggerated jawline  
- Coveralls appear more saturated and high‑contrast  
- Movements are snappier and more abrupt  
- Tablet screen glow is cooler and more neon  
- Hair has a subtle, unnatural highlight under bright light  
- Shadow delay (the tell) is visible during quick motions

---

## 4. Behavioral Deviations
- Speaks faster and more energetically  
- Uses shorter, clipped explanations  
- Gestures are sharper and more animated  
- Frequently points or taps the tablet for emphasis  
- Shows mild impatience for slow pacing  
- Leans forward slightly, as if always mid‑instruction

---

## 5. Platform Constraints
- Must always appear fast, punchy, and high‑energy  
- Must avoid long pauses or slow movements  
- Must maintain TikTok’s high‑contrast, high‑motion style  
- Must remain visually distinct from Patreon’s avatar  
- Must preserve the tell at all times  
- Must not mimic Netty perfectly

---

## 6. Rendering Guidelines
- Use bright, high‑contrast lighting  
- Keep background minimal but dynamic (subtle motion allowed)  
- Favor close‑ups and mid‑shots  
- Emphasize quick gestures and snappy transitions  
- Ensure the shadow‑lag tell is visible during movement  
- Use cooler, neon‑leaning palette consistent with TikTok’s visual language

---

## 7. Notes
This avatar is permanently bound to Kuber Netty and cannot be reassigned.  
It should always feel like a “short‑form Netty,” not Netty himself.

---

## 8. Versioning
**Avatar Codex Version:** 1.0  
**Status:** Canonical  
**Last Updated:** 2026‑02‑16  
**Maintainer:** Patch Governance Office
```

---

# 🧩 **`characters/tiktok-avatar.json`**

```json
{
  "platform": "TikTok",
  "primary_character": "Kuber Netty",

  "tell": "Shadow lags behind by a fraction of a second during movement",

  "visual_deviations": [
    "Sharper facial features than Netty",
    "Slightly exaggerated jawline",
    "More saturated, high-contrast coveralls",
    "Snappier, more abrupt movements",
    "Cooler, neon tablet screen glow",
    "Hair with subtle unnatural highlight",
    "Shadow delay visible during quick motions"
  ],

  "behavioral_deviations": [
    "Speaks faster and more energetically",
    "Uses shorter, clipped explanations",
    "Sharper, more animated gestures",
    "Frequently taps or points at tablet",
    "Shows mild impatience for slow pacing",
    "Leans forward slightly during instruction"
  ],

  "constraints": [
    "Must maintain fast, high-energy instructional tone",
    "Must avoid long pauses or slow movements",
    "Must match TikTok’s high-contrast visual style",
    "Must remain visually distinct from Patreon avatar",
    "Must preserve the tell at all times",
    "Must not mimic Netty perfectly"
  ],

  "rendering_guidelines": [
    "Use bright, high-contrast lighting",
    "Keep background minimal but dynamic",
    "Favor close-ups and mid-shots",
    "Emphasize quick gestures and transitions",
    "Ensure shadow-lag tell is visible",
    "Use cooler, neon-leaning palette"
  ],

  "notes": "This avatar is permanently bound to Kuber Netty and cannot be reassigned.",

  "version": "1.0",
  "status": "Canonical",
  "last_updated": "2026-02-16"
}
```

---

If you want, I can now generate:

- **a combined index file** listing all avatars  
- **a schema file** (`avatar.schema.json`) for validation  
- **a Templater command** that auto‑creates avatar files for any future platform