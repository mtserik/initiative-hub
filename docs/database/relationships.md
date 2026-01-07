# Entity Relationships — initiative-hub

This document defines the relationships and cardinalities between domain entities.
No SQL or physical constraints are defined at this stage.

---

## User ↔ Campaign (via CampaignMember)

**Relationship:**  
A User participates in Campaigns through CampaignMember.

**Cardinality:**
- A User can participate in 0..N Campaigns
- A Campaign can have 1..N Users
- A CampaignMember belongs to exactly one User and one Campaign

**Rules:**
- A user may have only one role per campaign
- Roles are defined at the CampaignMember level

**Notes:**
- This relationship controls permissions and access

---

## Campaign ↔ CampaignMember

**Relationship:**  
A Campaign groups its participants through CampaignMember.

**Cardinality:**
- A Campaign must have at least one CampaignMember
- At least one CampaignMember must have the role of Game Master

---

## Campaign ↔ Session

**Relationship:**  
A Campaign contains Sessions.

**Cardinality:**
- A Campaign can have 0..N Sessions
- A Session belongs to exactly one Campaign

**Rules:**
- Sessions cannot be shared across campaigns

---

## Campaign ↔ Character

**Relationship:**  
A Campaign contains Characters.

**Cardinality:**
- A Campaign can have 0..N Characters
- A Character belongs to exactly one Campaign

**Rules:**
- Characters inherit the RPG system from the campaign
- Characters cannot move between campaigns

---

## User ↔ Character

**Relationship:**  
A User owns or controls Characters.

**Cardinality:**
- A User can control 0..N Characters
- A Character is controlled by exactly one User

**Rules:**
- Game Masters may control NPC-like characters
- Ownership is independent of campaign membership

---

## Campaign ↔ RPG System (conceptual)

**Relationship:**  
A Campaign is defined by an RPG System.

**Cardinality:**
- A Campaign must have exactly one RPG System
- An RPG System can be used by 0..N Campaigns

**Rules:**
- RPG system is selected during campaign creation
- RPG system cannot be changed after creation

---

## Session ↔ Encounter (conceptual)

**Relationship:**  
A Session groups Encounters.

**Cardinality:**
- A Session can have 0..N Encounters
- An Encounter belongs to exactly one Session

**Rules:**
- Encounters are ordered temporally within a session
- Encounters may be active or archived

---

## Encounter ↔ Initiative (state)

**Relationship:**  
An Encounter maintains an Initiative state.

**Cardinality:**
- An Encounter has 0..1 active Initiative state at a time
- Initiative may be recalculated multiple times during an Encounter

**Rules:**
- Initiative is ephemeral
- Initiative history is not persisted in the initial version
