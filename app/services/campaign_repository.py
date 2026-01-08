from services.db import get_connection


def list_campaigns_by_user(user_id: str) -> list[dict]:
    """
    Lista todas as campanhas das quais o usuário participa,
    incluindo seu papel (gm, player, etc).
    """
    query = """
        SELECT
            c.id,
            c.name,
            c.description,
            c.system_key,
            c.created_at,
            cm.role
        FROM campaigns c
        JOIN campaign_members cm
            ON cm.campaign_id = c.id
        WHERE cm.user_id = %s
        ORDER BY c.created_at DESC;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (user_id,))
            return cur.fetchall()
