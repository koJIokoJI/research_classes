class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Создание нового объекта WizCoin по значениям galleons, sickles и knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # ВНИМАНИЕ: методы __init__() НИКОГДА не содержат команду return.
        
    def value(self):
        """Вся валюта объекта WizCoin в кнутсах"""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + self.knuts
    
    def weightInGrams(self):
        """Возвращает вес моент в граммах"""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
    
    