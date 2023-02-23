from random import choice
import matplotlib.pyplot as plt

class PasseioAleatorio:
    '''uma classe para gera passeios aleatórios'''
    def __init__(self, num_points=10000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calcula os pontos do passeio'''
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step ==0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
    
    rw = PasseioAleatorio()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
               edgecolor='none', s=5)
    plt.show()
    plt.figure(figsize=(19.2,10.8))
    running = input("Continuar? s/n: ")
    if running == 'n': 
        break
