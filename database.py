import sqlite3

conn = sqlite3.connect("arena.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS robots(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TXT,
    health INTEGER,
    damage INTEGER,
    battery INTEGER
)
""")

conn.commit()

# cursor.execute("INSERT INTO robots (name, health, damage, battery) VALUES ('Terminator', 100, 50, 100)")
# cursor.execute("INSERT INTO robots (name, health, damage, battery) VALUES ('Excavator', 80, 20, 100)")
# conn.commit()

cursor.execute("UPDATE robots SET health = 50 WHERE name = 'Terminator'")
conn.commit()

cursor.execute("UPDATE robots SET health = health - 15 WHERE name = 'Excavator'")
conn.commit()

cursor.execute("DELETE FROM robots")

cursor.execute("SELECT * FROM robots")
my_robots = cursor.fetchall()

for bot in my_robots:
    print(f"Мої роботи додані в базу данних: {bot}")

conn.close()

print(f"База даних arena.db та таблиця robots успішно створені.!")