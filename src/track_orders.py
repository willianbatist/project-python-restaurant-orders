class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        pedidos_comidas = {}
        for cliente, comida, _ in self.data:
            if cliente == customer:
                pedidos_comidas[comida] = pedidos_comidas.get(comida, 0) + 1
        resultado = max(pedidos_comidas, key=pedidos_comidas.get)
        return resultado

    def get_never_ordered_per_customer(self, customer):
        comida_set = set()
        total_comida_set = set()
        for cliente, comida, _ in self.data:
            if cliente == customer:
                comida_set.add(comida)
            elif cliente != customer:
                total_comida_set.add(comida)
        resultado = total_comida_set - comida_set
        return resultado

    def get_days_never_visited_per_customer(self, customer):
        dias = set()
        dias_totais = set()
        for cliente, _, dia in self.data:
            if cliente == customer:
                dias.add(dia)
            elif cliente != customer:
                dias_totais.add(dia)
        resultado = dias_totais - dias
        return resultado

    def get_busiest_day(self):
        dias = []
        for cliente, _, dia in self.data:
            if cliente == cliente:
                dias.append(dia)
        resultado = max(dias, key=dias.count)
        return resultado

    def get_least_busy_day(self):
        dias = []
        for cliente, _, dia in self.data:
            if cliente == cliente:
                dias.append(dia)
        resultado = min(dias, key=dias.count)
        return resultado
