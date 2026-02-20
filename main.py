# git init
# git add . 
# git commit -m
import time
import os
import random
from colorama import init, Fore, Style
from models import Robot, WarRobot, MedicRobot
from storage import load_army_robot, save_army_robot, take_random_MedicRobot, take_random_WarRobot, take_alive_robots, take_random_target

init(autoreset=True)
army: list[Robot] = load_army_robot()

if not army:
    for i in range(1,6):
        army.append(WarRobot(f"Terminator-{i}", "Gun"))
        army.append(WarRobot(f"Predator-{i}", "Blade"))
        army.append(MedicRobot(f"Doc-{i}"))
        
    save_army_robot(army)
    
print(Fore.YELLOW + Style.BRIGHT + f"ПОЧИНАЄМО БИТВУ!! УЧАСНИКІВ {len(army)} \n")
time.sleep(1)

round_num = 1

while True:
    alive_army = take_alive_robots(army)
    
    if len(alive_army) <= 1:
        if len(alive_army) == 1:
            print(Fore.CYAN + f"ПЕРЕМОЖЕЦЬ {alive_army[0]} \n")
        else:
            print("Всі здохли... \n")
        break
    
    print(Fore.YELLOW + f"РАУНД {round_num}. В ЖИВИХ ЛИШИЛОСЬ {len(alive_army)} \n")
    
    attacker = take_random_WarRobot(alive_army)
    if attacker:
        target = take_random_target(alive_army, attacker)
        if target:
            print(Fore.RED + f"{attacker.name} атакував {target.name} \n")
            attacker.attack(target)
            
    if random.random() > 0.5:
        medic = take_random_MedicRobot(alive_army)
        if medic:
            target = take_random_target(alive_army, medic)
            if target:
                print(Fore.GREEN + f"{medic.name} лікує {target.name} \n")
                medic.heal_robot(target)
                
    round_num += 1
    time.sleep(1.5)
        

save_army_robot(army)