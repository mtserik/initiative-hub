from app.services.db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT current_database(), current_user;")
print(cur.fetchone())

cur.close()
conn.close()
