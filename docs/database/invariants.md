# Domain Invariants

This document defines rules that must always be true within the domain, independent of implementation.

---

## User
- A user may participate in multiple campaigns

---

## Campaign
- A campaign must have at least one Game Master
- A campaign must be associated with exactly one RPG system
- The RPG system of a campaign cannot be changed after creation

---

## CampaignMember
- A user can have only one role per campaign

---

## Character
- A character belongs to exactly one campaign
- A character cannot exist without a campaign
- A character must follow the schema defined by the campaign's RPG system

---

## Session
- A session must belong to a campaign
- A session cannot exist without a campaign
