# Database Entities — initiative-hub

This document describes the core domain entities and conceptual elements of the initiative-hub project.
At this stage, entities are described semantically, without database columns or SQL definitions.

---

## User
**Description:**  
Represents a person using the platform.

**Responsibilities:**
- Authenticate into the system
- Participate in campaigns
- Act as Game Master or Player

**Notes:**
- Roles are campaign-scoped, not global

---

## Campaign
**Description:**  
Represents a RPG campaign. A campaign is the main container for all gameplay elements.

**Responsibilities:**
- Define the RPG system used
- Group players, characters, and sessions
- Maintain narrative continuity

**Notes:**
- A campaign must be associated with exactly one RPG system

---

## CampaignMember
**Description:**  
Represents the relationship between a User and a Campaign.

**Responsibilities:**
- Define the role of a user within a campaign
- Control campaign-level permissions

**Notes:**
- This is an associative entity

---

## Character
**Description:**  
Represents a playable character within a campaign.

**Responsibilities:**
- Store character attributes and progression
- Participate in sessions and encounters

**Notes:**
- Character data is system-dependent
- Character sheet is stored as JSONB

---

## Session
**Description:**  
Represents a single game meeting within a campaign.

**Responsibilities:**
- Group encounters
- Store narrative summaries and notes

**Notes:**
- A campaign can have multiple sessions

---

# Conceptual Entities (Not Implemented as Tables)

## RPG System
**Description:**  
Represents a ruleset that defines how a campaign and its characters behave.

**Responsibilities:**
- Define character sheet structure
- Define rules for encounters and actions

**Notes:**
- Selected during campaign creation
- Cannot be changed after campaign creation

---

## Encounter
**Description:**  
Represents a structured scene within a session, such as combat or social interaction.

**Responsibilities:**
- Control turn-based flow
- Maintain initiative state

**Notes:**
- May occur multiple times within a session
- Not implemented as a table in the initial version

---

## Initiative
**Description:**  
Represents the current turn order and combat state within an encounter.

**Responsibilities:**
- Track initiative order
- Track current round and turn

**Notes:**
- Modeled as part of the Encounter state
- Can be rolled multiple times per encounter

---

## NPC
**Description:**  
Represents a non-player character.

**Responsibilities:**
- Act as allies, enemies, or neutral entities in encounters

**Notes:**
- Conceptually similar to Character
- May share the same schema structure
