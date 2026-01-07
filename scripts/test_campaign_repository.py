from app.services.campaign_repository import list_campaigns_by_user

# UUIDs do seed
GM_USER_ID = "11111111-1111-1111-1111-111111111111"
PLAYER_USER_ID = "22222222-2222-2222-2222-222222222222"

print("=== Campanhas do GM ===")
gm_campaigns = list_campaigns_by_user(GM_USER_ID)
for c in gm_campaigns:
    print(c)

print("\n=== Campanhas do Player ===")
player_campaigns = list_campaigns_by_user(PLAYER_USER_ID)
for c in player_campaigns:
    print(c)
