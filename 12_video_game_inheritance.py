"""
Your task is to:

Fix the errors in the code developed by your team.

Implement the correct hierarchy.
"""

"""
Requirements:

Enemy must be a subclass of Character.

Player must be a subclass of Character.

Enemy must be a superclass of DifficultEnemy and EasyEnemy.
"""

# Hierarchy:

"""
Character ----> Player , Enemy
Enemy ------> DifficultEnemy , EasyEnemy
"""

class Sprite():
    
    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter
 
 
class Enemy(Sprite):
    
    def __init__(self, x, y, img_file, speed):
        Sprite.__init__(self, x, y, img_file, speed, 5)
        self.message = "I'm here to protect my master"
 
 
class Player(Sprite):
    
    def __init__(self, x, y, img_file, speed=56, life_counter=6):
        Sprite.__init__(self, y, img_file, speed, life_counter)
        
 
 
class DifficultEnemy(Enemy):
    
    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 80)
 
 
class EasyEnemy(Enemy):
    
    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 40)
        self.life_counter = 1