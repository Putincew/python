class Student:
    def __init__(self, name):
        self.name = name
        self.nb = self.Notebook()

    def show(self):
        n = self.nb.swow()
        print(self.name, '=>', n)


    class Notebook:
        def __init__(self):
            self.model = 'HP'
            self.proc = 'i7'
            self.op = 16

        def swow(self):
            return f'{self.model}, {self.proc}, {self.op}'



priz1 = Student('Roman')
priz1.show()
priz2 = Student('Vladimir')
priz2.show()

