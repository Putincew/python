class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)



# print(__name__)
__autor__ = 'Andrey'

if __name__ == '__main__':
    print(f'Module {__name__} autor: {__autor__}')
