class Robot:
    
    def __init__(self, name):
        self.name = name
        
        self.weapon = 0
        self.heal = 0
                
        self._battery = 100
        self._health = 100
        
    @property
    def health(self):
        return self._health
        
    @health.setter
    def health(self, amount):
        if amount < 0:
            self._health = 0
        elif amount > 100:
            self._health = 100
        else:
            self._health = amount
            
    @property
    def battery(self):
        return self._battery
    
    @battery.setter
    def battery(self, amount):
        if amount < 0:
            self._battery = 0
        elif amount > 100:
            self._battery = 100
        else:
            self._battery = amount
            
    def __str__(self):
        return f"Робот: {self.name} | Заряд: {self.battery} | Здоровя: {self.health}"
    
    def say_hello(self):
        print(f"Привіт, мене звати {self.name}")
        
    def move(self, distance):
        if distance == self.battery:
            print("Я не побіжу, бо розряджусь в 0")
            return
        elif distance < self.battery:
            print(f"Я пробіг {distance} км")
            self.battery = self.battery - round(distance, 2)
            print(f"Залишилось заряду: {self.battery}")
        else:
            print(f"Недостатньо заряду, потрібно {distance}, є всього {self.battery}")
            return
    
    def transfer_energy(self, other_robot: 'Robot', amount):
        if self.battery > amount:
            if other_robot.battery + amount > 100:
                print(f"Неможливо зарядити більше 100%. Повторіть з кількістю зарядки {round(100 - other_robot.battery, 2)}")
                return
            else:
                other_robot.battery += amount
                self.battery -= amount
                print(f"{self.name} передав {other_robot.name} {amount}% зарядки")
        else:
            print(f"У {self.name} всього {self.battery}% зарядки, він не може передати {amount}% зарядки")
            
class WarRobot(Robot):
    
    def __init__(self, name, weapon):
        super().__init__(name)
        
        self.weapon = weapon
        self.heal = 0
        
    def __str__(self):
        return f"Робот: {self.name}| Здоровя: {self.health} \n Заряд: {self.battery} | Зброя: {self.weapon}"
        
    def attack(self, other_robot: 'Robot'):
        if other_robot.health <= 0:
            print(f"{other_robot.name} уже мертвий, нашо бєш далі")
            return
        else:
            other_robot.health -= 20
            if other_robot.health > 0:
                print(f"{self.name} наніс 20 шкоди {other_robot.name}, у нього залишилось {other_robot.health} здоровя")
            else:
                print(f"{self.name} вбив {other_robot.name}")
                
class MedicRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        
        self.heal = 10
        self.weapon = 0
    
    def __str__(self):
        return f"Робот: {self.name}| Здоровя: {self.health} \n Заряд: {self.battery} | Здатність лікувати: 10"
       
     
    def heal_robot(self, other_robot: 'Robot'):
        if other_robot.health == 0:
            print(f"Ви лікар, а не маг, неможливо воскресити мертвого.")
            return
        
        if other_robot.health + 10 >= 100:
            print(f"В {other_robot.name} {other_robot.health} здоровя.")
            print("Ви не можете полікувати більше 100 здоровя цілі")
            return
        
        if self.battery > 5:
            other_robot.health += 10
            self.battery -= 5
            print(f"{self.name} вилікував {other_robot.name} на 10 очків здоровя за 5% батареї")
            print(f"Ваша батарея: {self.battery}% | Здоровя {other_robot.name}: {other_robot.health}")
        else:
            print(f"Ви не змогли полікувати. Ваша батарея {self.battery}%, потрібно більше 5%")
            return
        