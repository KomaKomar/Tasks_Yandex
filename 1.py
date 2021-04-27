#Задачка Робот
#Робот, который принимает текст-команду, для определения своего движения
class Robot:
    def __init__(self, pos): #принимает начальную позацию робота
        self.x = pos[1]
        self.y = pos[0]
        self.hod = [pos]
    def move(self, slovo):
        self.hod = [(self.y, self.x)] #координаты перемещения робота
        for i in list(slovo):
            if i == 'N':
                if self.x == 100: #проверка ограничителя площади 100*100
                    continue;
                else:
                    self.x = self.x + 1;
            if i == 'S':
                if self.x == 0:
                    continue;
                else:
                    self.x = self.x - 1;
            if i == 'E':
                if self.y == 100:
                    continue;
                else:
                    self.y = self.y + 1;
            if i == 'W':
                if self.y == 0:
                    continue;
                else:
                    self.y = self.y - 1
            self.hod.append((self.y, self.x)) #возврат координат
        return (self.x, self.y)
    def path(self):
        return self.hod


r = Robot((0, 0)) #Начальые координаты
print(r.move('NENW')) #Направление для движения
print(*r.path()) #маршрут