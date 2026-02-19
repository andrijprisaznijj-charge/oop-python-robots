import json
import random
from pathlib import Path
from models import Robot, WarRobot, MedicRobot

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "save_army.json"

def save_army_robot(army_list: list[Robot]):
    print("Зберігаємо армію роботів")
    
    data = []
    
    for bot in army_list:
        data_of_bot = {
            "name": bot.name,
            "model": bot.model,
            "battery": bot.battery,
            "health": bot.health,
            "type": type(bot).__name__
        }
        
        if isinstance(bot, WarRobot):
            data_of_bot["weapon"] = bot.weapon
            
        data.append(data_of_bot)
        
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print("Все збережено")
        
def load_army_robot():
    print("Завантажуємо роботів.....")
    loaded_army = []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data_list = json.load(file)
            for item in data_list:
                
                if item["type"] == "Robot":
                    bot = Robot(item["name"],item["model"])
                elif item["type"] == "WarRobot":
                    weapon = item.get("weapon", "Gun")
                    bot = WarRobot(item["name"],item["model"],weapon)
                else:
                    bot = MedicRobot(item["name"],item["model"])
                    
                bot.health = item["health"]
                bot.battery = item["battery"]
                loaded_army.append(bot)
            print(f"Армію успішно завантажено")
            return loaded_army
    except FileNotFoundError:
        print("Сталася помилка")
        return []
    except json.JSONDecodeError:
        return []
 
def take_alive_robots(list_of_robots : list['Robot']) -> "Robot":
    return [bot for bot in list_of_robots if bot.health > 0]

def take_random_target(list_of_robots: list['Robot'], attacker) -> "Robot":
    target = [bot for bot in list_of_robots if bot.health > 0 and bot != attacker]
    if not target: return None
    return random.choice(target)
    
def take_random_Robot(list_of_robots: list['Robot']) -> "Robot":
    robots = [r for r in list_of_robots if type(r) is Robot]
    if not robots: return None
    return random.choice(robots)
    
def take_random_WarRobot(list_of_robots: list['Robot']) -> "WarRobot":
    wariors = [w for w in list_of_robots if type(w) is WarRobot]
    if not wariors: return None
    return random.choice(wariors)

def take_random_MedicRobot(list_of_robots: list['Robot']) -> "MedicRobot":
    medics = [r for r in list_of_robots if type(r) is MedicRobot]
    if not medics: return None
    return random.choice(medics)
   
