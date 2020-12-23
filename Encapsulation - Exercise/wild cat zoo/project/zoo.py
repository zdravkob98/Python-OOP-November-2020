from project.lion import Lion
from project.cheetah import Cheetah
from project.tiger import Tiger
from project.caretaker import Caretaker
from project.vet import Vet
from project.keeper import Keeper


class Zoo:
    def __init__(self, name: str, budget, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity: #maybe must be > 0
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            type_of_animal = type(animal).__name__
            return f"{animal.name} the {type_of_animal} added to the zoo"
            #return f"{animal.name} the {animal.__class__.__name__} added to the zoo" #here is problem
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            type_of_worker = type(worker).__name__
            return f"{worker.name} the {type_of_worker} hired successfully"
            #return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        if self.workers:
            fired_worker = [w for w in self.workers if w.name == worker_name][0]
            if fired_worker:
                self.workers.remove(fired_worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_needed = sum([w.salary for w in self.workers])
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum([a.needs for a in self.animals])
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']

        result = [f'You have {len(self.animals)} animals']

        result.append(f'----- {len(lions)} Lions:')
        for l in lions:
            result.append(str(l))

        result.append(f'----- {len(tigers)} Tigers:')
        for t in tigers:
            result.append(str(t))

        result.append(f'----- {len(cheetahs)} Cheetahs:')
        for c in cheetahs:
            result.append(str(c))

        return '\n'.join(result)

    def workers_status(self):
        keepers = [p for p in self.workers if isinstance(p, Keeper)]
        caretakers = [p for p in self.workers if isinstance(p, Caretaker)]
        vets = [p for p in self.workers if isinstance(p, Vet)]

        data = [f'You have {len(self.workers)} workers']
        data.append(f'----- {len(keepers)} Keepers:')
        for p in keepers:
            data.append(str(p))

        data.append(f'----- {len(caretakers)} Caretakers:')
        for p in caretakers:
            data.append(str(p))

        data.append(f'----- {len(vets)} Vets:')
        for p in vets:
            data.append(str(p))

        return '\n'.join(data)

