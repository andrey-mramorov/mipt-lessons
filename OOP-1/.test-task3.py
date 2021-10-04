class gameunit.Attacker:
    health = ''
    attack = ''

    def attack(self, target):
        pass

    def is_alive(self):
        if self.health:
            return True
        else:
            return False

class hero.Hero(gameunit.Attacker):
    experience = ''
    name = ''

    def __init__(self, name):
        self.name = name
    def attack(self, target):
        self.target = target

class enemies.Enemy(gameunit.Attacker):
    pass

class enemies.Dragon(enemies.Enemy):
    color = ''
    __answer = ''
    __quest = ''

    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False
    
    def set_answer(self, answer):
        self.answer = answer

    def question(self):
        pass

class enemies.RedDragon(enemies.Dragon):
    def question(self):
        pass

#GreenDragon
#RedDragon
