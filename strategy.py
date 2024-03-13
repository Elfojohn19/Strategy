
class AttackStrategy:
    def attack(self):
        pass


class MovementStrategy:
    def move(self):
        pass


class SoldierAttack(AttackStrategy):
    def attack(self):
        return "El soldado ataca con una espada."

class ArcherAttack(AttackStrategy):
    def attack(self):
        return "El arquero ataca con un arco."

class KnightAttack(AttackStrategy):
    def attack(self):
        return "El caballero ataca con una lanza."


class SoldierMovement(MovementStrategy):
    def move(self):
        return "El soldado se mueve a pie."

class ArcherMovement(MovementStrategy):
    def move(self):
        return "El arquero se mueve a pie."

class KnightMovement(MovementStrategy):
    def move(self):
        return "El caballero se mueve a caballo."


class MilitaryUnit:
    def _init_(self, attack_strategy, movement_strategy):
        self.attack_strategy = attack_strategy
        self.movement_strategy = movement_strategy

    def attack(self):
        return self.attack_strategy.attack()

    def move(self):
        return self.movement_strategy.move()


soldier = MilitaryUnit(SoldierAttack(), SoldierMovement())
archer = MilitaryUnit(ArcherAttack(), ArcherMovement())
knight = MilitaryUnit(KnightAttack(), KnightMovement())


print(soldier.attack())  
print(soldier.move())    
print(archer.attack())  
print(archer.move())     
print(knight.attack())   
print(knight.move())     