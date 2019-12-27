import collections
import copy


class GlobalTime:
    def __init__(self):
        self.time_has_passed = 0

    def an_hour_has_passed(self):
        self.time_has_passed += 1


class Transport:
    def __init__(self, cargo=None, delivery_time=0, available=0):
        self.cargo = cargo
        self.station = None
        self.delivery_time = delivery_time
        self.available = available


    def load_transport(self, cargo):
        if isinstance(cargo, Cargo):
            self.cargo = cargo
            destination = cargo.route.popleft()
            self.delivery_time = list(destination.values())[0]
            self.available = list(destination.values())[0] * 2
        else:
            raise TypeError

    def unload_transport(self):
        self.cargo = None
        self.delivery_time = 0

    def an_hour_on_the_route(self):
        if self.delivery_time:
            self.delivery_time -= 1
        if self.available:
            self.available -= 1


class Truck(Transport):
    def __init__(self, cargo=None, delivery_time=0, available=0):
        super().__init__(cargo, delivery_time, available)

    def load_transport(self, cargo):
        super().load_transport(cargo)

    def unload_transport(self):
        super().unload_transport()

    def an_hour_on_the_route(self):
        super().an_hour_on_the_route()


class Ship(Transport):
    def __init__(self, cargo=None, delivery_time=0, available=0):
        super().__init__(cargo, delivery_time, available)

    def load_transport(self, cargo):
        super().load_transport(cargo)

    def unload_transport(self):
        super().unload_transport()

    def an_hour_on_the_route(self):
        super().an_hour_on_the_route()


class Station:
    def __init__(self, num):
        self.queue = collections.deque()
        self.transport_quantity = num
        self.transport_available = collections.deque()

    def create_transport_for_station(self):
        for i in range(self.transport_quantity):
            transport = Transport()
            transport.station = self
            self.transport_available.append(transport)


class Port(Station):
    def __init__(self, num):
        super().__init__(num)

    def create_transport_for_station(self):
        for i in range(self.transport_quantity):
            transport = Ship()
            transport.station = self
            self.transport_available.append(transport)


class Truck_station(Station):
    def __init__(self, num):
        super().__init__(num)

    def create_transport_for_station(self):
        for i in range(self.transport_quantity):
            transport = Truck()
            transport.station = self
            self.transport_available.append(transport)


class Cargo:
    def __init__(self, name, route):
        self.name = name
        self.route = route

    @staticmethod
    def create_cargo(name, dict_route):
        copy_route = copy.deepcopy(dict_route)[name]
        route = collections.deque()
        for i in copy_route:
            new_dict = {}
            for key, value in i.items():
                new_dict[stations[key]] = value
                route.append(new_dict)
        return Cargo(name, route)


class Delivery:
    def __init__(self):
        self.delivery_in_process = set()
        self.returning = set()
        self.delivered = []
        self.clean_delivery = set()
        self.clean_return = set()

    def start(self, transport):
        self.delivery_in_process.add(transport)

    def deliver_one_step(self):
        for transport in self.delivery_in_process:
            if not transport.delivery_time - 1:
                check_cargo = transport.cargo
                transport.unload_transport()
                self.returning.add(transport)
                self.clean_delivery.add(transport)
                if check_cargo.route:
                    list(check_cargo.route[0].keys())[0].queue.append(check_cargo)
                else:
                    self.delivered.append(check_cargo)
                    print('cargo {} is delivered'.format(check_cargo.name))
            else:
                transport.an_hour_on_the_route()

    def check_for_delivered(self):
        for transport in self.clean_delivery:
            self.delivery_in_process.remove(transport)
        self.clean_delivery.clear()

    def check_for_returned(self):
        for transport in self.clean_return:
            self.returning.remove(transport)
        self.clean_return.clear()

    def returning_one_step(self):
        for transport in self.returning:
            transport.an_hour_on_the_route()
            if not transport.available:
                self.clean_return.add(transport)
                transport.station.transport_available.append(transport)


def cargo_to_stations(cargo_list, route):
    for _ in cargo_list:
        cargo = Cargo.create_cargo(_, route)
        list(cargo.route[0].keys())[0].queue.append(cargo)


# инициализируем станции и с количеством транспорта на каждой
truck_station = Truck_station(2)
port = Port(1)
temp = [truck_station, port]
stations = {id(station): station for station in temp}

# Cоздаем транспорт для наших станций
for station in temp:
    station.create_transport_for_station()

# Создаем маршруты
A = collections.deque([{id(truck_station): 1}, {id(port): 4}])
B = collections.deque([{id(truck_station): 5}])
Route = {'A': A, 'B': B}

# вводим груз, который нужно доставить
cargo_to_deliver = input()
quantity = len(cargo_to_deliver)

'''раскидываем груз в очереди у станций(сделано для того, чтобы была возможность
начинать доставку как из порта, так и со станции грузовиков)'''
cargo_to_stations(cargo_to_deliver, Route)

# инициализируем сегодняшнюю доставку
today_delivery = Delivery()
today = GlobalTime()
while quantity != len(today_delivery.delivered):
    for station in stations.values():
        while station.transport_available and station.queue:
            cargo = station.queue.popleft()
            transport = station.transport_available.popleft()
            transport.load_transport(cargo)
            today_delivery.start(transport)
    today_delivery.deliver_one_step()
    today_delivery.check_for_delivered()
    today_delivery.returning_one_step()
    today_delivery.check_for_returned()
    today.an_hour_has_passed()
print('Total delivery time:', today.time_has_passed)
