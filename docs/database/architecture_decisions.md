# Architecture Decisions — Database

This document records key architectural decisions related to the database design.

---

## ADR-001 — Use of JSONB for Character Sheets
**Decision:**  
Character data will be stored using JSONB fields.

**Reasoning:**  
RPG systems vary significantly in attributes, rules, and progression mechanics.

**Consequences:**  
- Application-level schema validation is required
- Database schema remains flexible

---

## ADR-002 — Campaign Defines RPG System
**Decision:**  
Each campaign must be associated with a single RPG system.

**Reasoning:**  
All characters, rules, and encounters depend on system definitions.

**Consequences:**  
- Characters inherit system constraints from the campaign
- RPG system cannot be changed after campaign creation

---

## ADR-003 — Initiative as Temporal State
**Decision:**  
Initiative will not be modeled as a standalone table.

**Reasoning:**  
Initiative is temporary, repeatable, and contextual to encounters.

**Consequences:**  
- Initiative is stored as part of encounter state
- Historical initiative data is not preserved initially

---

## ADR-004 — Separation of Domain and Storage
**Decision:**  
Conceptual entities may exist without corresponding database tables.

**Reasoning:**  
Not all domain concepts require persistence at the same level.

**Consequences:**  
- Database remains simpler
- Domain complexity is managed at the application layer
