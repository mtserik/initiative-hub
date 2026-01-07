# Logical ER Model — initiative-hub

This document describes the logical ER model in text form.
The visual representation is available in docs/database/er/.

## Entities
- User
- Campaign
- CampaignMember
- Character
- Session

## Associative Entities
- CampaignMember (User ↔ Campaign)

## Conceptual Entities
- RPG System
- Encounter
- Initiative

## Notes
- Character sheets are stored as JSONB
- Initiative is modeled as encounter state
