class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return  self
    def display_health(self):
        print self.name + ' | Health: ' + str(self.health)
        return self
class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health +=5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print 'I am a dragon'
        return Animal.display_health(self)

animal1 = Animal('Sir Wellington', 50)
dog1 = Dog('Lupa', 50)
dragon1 = Dragon('Smogg', 50)

animal1.walk().walk().walk().run().display_health()
dog1.walk().walk().walk().run().run().pet().display_health()
dragon1.fly().display_health()