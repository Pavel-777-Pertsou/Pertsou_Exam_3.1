class Tomato:

    stadii = {0: "ничего", 1: 'семя', 2: "зелёный", 3: "спелый"}

    def __init__(self, index):
        self._index = index
        self._stadia = 0

    def grow(self):
        self._change_stadia()

    def is_ripe(self):
        if self._stadia == 3:
            return True
        return False


    def _change_state(self):
        if self._stadia < 3:
            self._stadia += 1
        self._print_stadia()

    def _print_stadia(self):
        print("Помидор",self._index, "еще", Tomato.stadii[self._stadia])


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []



class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Уход за растениями...")
        self._plant.grow_all()
        print("Работа окончена")

    def harvest(self):
        print("Сбор урожая...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Сбор урожая окончен")
        else:
            print("Урожай еще не созрел")

    @staticmethod
    def knowledge_base():
        print("Бывает 3 стадии созревания томатов, еще цветок, зеленый и спелый. Урожай будет собран при полном созревании! ")


if __name__ == '__main__':
    Gardener.knowledge_base()
    tomato_bush = TomatoBush(2)
    gardener = Gardener("Павел", tomato_bush)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.harvest()