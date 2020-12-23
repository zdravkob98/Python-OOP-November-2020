

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_subsription = [s for s in self.subscriptions if s.id == subscription_id][0]
        current_customer = [c for c in self.customers if c.id == current_subsription.trainer_id][0]
        current_trainer = [t for t in self.trainers if t.id == current_subsription.trainer_id][0]
        current_equipment = [e for e in self.equipment if e.id == current_subsription.trainer_id][0]
        current_plan = [p for p in self.plans if p.id == current_subsription.trainer_id][0]
        if current_subsription:
            date = [current_subsription,current_customer, current_trainer, current_equipment, current_plan]
            return '\n'.join(map(str, date))



