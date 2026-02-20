import sqlite3
import random
from pathlib import Path
from models import Robot, WarRobot, MedicRobot

BASE_DIR = Path(__file__).parent

BASE_DB = BASE_DIR / ("arena.db")

def init_db():
    conn = sqlite3.connect(BASE_DB)
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS robots(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        health INTEGER,
        damage INTEGER,
        heal INTEGER,
        battery INTEGER,
        robot_type TEXT
        )"""
        )
    
    conn.commit()
    conn.close()
    
init_db()

def save_army_robot(army_list: list['Robot']):
    print("Зберігаємо армію роботів")
    conn = sqlite3.connect(BASE_DB)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM robots")
    
    for bot in army_list:
        bot_type = bot.__class__.__name__
        
        cursor.execute("""INSERT INTO robots (name, health, damage, heal, battery, robot_type)
                       VALUES (?, ?, ?, ?, ?, ?)
                       """, (bot.name, bot.health, bot.weapon, bot.heal, bot.battery, bot_type))
        
    conn.commit()
    conn.close()
    
    print(f"Армію успішно збережено")
    
    
def load_army_robot():
    print("Завантажуємо роботів.....")
    conn = sqlite3.connect(BASE_DB)
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM robots")
    
    rows = cursor.fetchall()
    
    army = []
    
    for row in rows:
        name = row["name"]
        health = row["health"]
        battery = row["battery"]
        damage = row["damage"]
        heal = row["heal"]
        robot_type = row["robot_type"]
        
        if robot_type == "MedicRobot":
            bot = MedicRobot(name)
        elif robot_type == "WarRobot":
            bot = WarRobot(name, damage)
        else:
            bot = Robot(name)
        
        bot.weapon = damage
        bot.heal = heal
        bot.battery = battery
        bot.health = health
        
        army.append(bot)
        
    conn.close()
    if army:
        print(f"Успішно відновлено {len(army)} бійців з бази даних")
        
    return army
            
    
def take_alive_robots(list_of_robots : list['Robot']) -> "Robot":
    return [bot for bot in list_of_robots if bot.health > 0]

def take_random_target(list_of_robots: list['Robot'], attacker) -> "Robot":
    target = [bot for bot in list_of_robots if bot.health > 0 and bot != attacker]
    if not target: return None
    return random.choice(target)

def take_random_WarRobot(list_of_robots: list['Robot']) -> "WarRobot":
    wariors = [w for w in list_of_robots if type(w) is WarRobot]
    if not wariors: return None
    return random.choice(wariors)

def take_random_MedicRobot(list_of_robots: list['Robot']) -> "MedicRobot":
    medics = [r for r in list_of_robots if type(r) is MedicRobot]
    if not medics: return None
    return random.choice(medics)
   
