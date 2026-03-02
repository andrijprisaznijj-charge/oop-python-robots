def write_log(message: str):
    with open("battle_history.txt", "a", encoding="utf-8") as file:
        file.write(f"{message} \n")
        
def start_battle():
    with open("battle_history.txt", "w", encoding='utf-8') as f:
        f.write("---НОВА БИТВА ПОЧАЛАСЬ---")