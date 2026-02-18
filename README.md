# KNLK Project Repository

This repository contains the complete governance, SDLC execution, character system, and operational oversight structure for the KNLK project — the Kubernetes Batting‑Cage Training System.

The repository is organized around three governing layers:

1. **Strategic Layer** — Project Charter  
2. **Operational Layer** — SDLC Execution  
3. **Reference Layer** — SDLC Starter Kit Templates  

It also includes the character system and Gordon’s client onboarding kit, which define the roles, responsibilities, and governance routines used throughout the project.

---

# 1. Strategic Layer — Project Charter

## `./SDLC/KNLK-Project-Charter.md`

The Project Charter defines:

- the purpose of the KNLK project  
- the stakeholder (Kuber Netty)  
- the contracted roles (Gordon, Patch)  
- the scope and constraints  
- the governance model  
- the SDLC structure  
- the approval and escalation paths  

This document is the **highest authority** in the repository.  
All other documents derive from it.

---

# 2. Operational Layer — SDLC Execution

## `./SDLC/KNLK-SDLC-Execution.md`

This document executes the SDLC phases for the KNLK project:

- Planning  
- Requirements  
- Design  
- Development  
- Testing  
- Deployment  
- Maintenance  

It defines the deliverables, workflows, and responsibilities for each phase.  
It is the operational contract that governs how the project is executed.

---

# 3. Reference Layer — SDLC Starter Kit

## `./SDLC/SDLC Starter Kit Packet.md`

This packet contains **generic, reusable SDLC templates**, including:

- Project Plan  
- SRS  
- HLD  
- LLD  
- Test Plan  
- Deployment Plan  
- Maintenance Plan  

These templates are not project‑specific.  
They serve as a reference library for any future project.

---

# 4. Character System

## `./SDLC/Characters/`

This directory contains:

- **Character template** — the universal onboarding template  
- **Gordon, PPM** — governance and oversight  
- **Kuber Netty, SRE** — stakeholder and content architect  
- **Patch** — runtime and infrastructure engineer  

Each character is an **independent corporate entity** with its own responsibilities and constraints.

---

# 5. Gordon’s Client Onboarding Kit

## `./SDLC/Characters/Gordon Client Onboarding Kit Templates/`

This folder contains:

- Gordon’s onboarding kit  
- Daily oversight checklist template  
- Weekly oversight checklist template  
- Monthly oversight checklist template  
- Quarterly oversight checklist template  
- Annual oversight checklist template  

Gordon maintains the templates.  
The project owner maintains the generated files in their project space.

These checklists support Gordon’s governance‑as‑a‑service model.

---

# 6. Folder Structure Summary

```
./SDLC/
    Characters/
        Character template.md
        Gordon, PPM.md
        Kuber Netty, SRE.md
        Patch.md
        Gordon Client Onboarding Kit Templates/
            Gordon Client Onboarding Kit.md
            Gordon Daily Oversight Routine Checklist Template.md
            Gordon Weekly Oversight Routine Checklist Template.md
            Gordon Monthly Oversight Routine Checklist Template.md
            Gordon Quarterly Oversight Routine Checklist Template.md
            Gordon Annual Oversight Routine Checklist Template.md
    KNLK-Project-Charter.md
    KNLK-SDLC-Execution.md
    SDLC Starter Kit Packet.md
```

---

# 7. Governance Hierarchy

1. **Project Charter** — defines the project  
2. **SDLC Execution** — runs the project  
3. **Oversight Templates** — govern the project  
4. **Character Files** — define the actors  
5. **Starter Kit** — provides reusable templates  

This hierarchy ensures clarity, traceability, and audit‑ready governance.

---

# 8. Purpose of This Repository

This repository is designed to:

- externalize the KNLK project’s governance  
- maintain strict SDLC discipline  
- support character‑based operational modeling  
- provide audit‑grade documentation  
- ensure long‑term scalability and zero drift  

It is the authoritative source of truth for the KNLK project.