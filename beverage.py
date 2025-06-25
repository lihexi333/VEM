class Beverage:
    def __init__(self):
        self.description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    def getCost(self):
        return 0.0


class Coca(Beverage):
    def __init__(self):
        super().__init__()  # 调用父类构造函数
        self.description = "可乐"

    def getCost(self):
        return 3.0


class Coffee(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "咖啡"

    def getCost(self):
        return 4.0


class Decorator(Beverage):
    def getDescription(self):
        pass


class IceDecorator(Decorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + " + 冰"

    def getCost(self):
        return self.beverage.getCost() + 0.5


class MilkDecorator(Decorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + " + 奶"

    def getCost(self):
        return self.beverage.getCost() + 1.0


class LemonJuice(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "柠檬汁"
    def getCost(self):
        return 3.5


class OrangeJuice(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "橙汁"
    def getCost(self):
        return 4.0


class LemonDecorator(Decorator):
    def __init__(self, beverage):
        self.beverage = beverage
    def getDescription(self):
        return self.beverage.getDescription() + " + 柠檬"
    def getCost(self):
        return self.beverage.getCost() + 0.8
