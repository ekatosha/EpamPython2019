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
        self.delivery_time = delivery_time
        self.available = available

    @staticmethod
    def create_transport(cargo, station):
        if isinstance(cargo, Cargo):
            station.availavle_transport -= 1
            return cargo.route.popleft()
        else:
            raise TypeError


class Truck(Transport):
    def __init__(self, cargo=None, delivery_time=0, available=0):
        super().__init__(cargo, delivery_time, available)


class Ship(Transport):
    def __init__(self, cargo=None, delivery_time=0, available=0):
        super().__init__(cargo, delivery_time, available)


class Station:
    def __init__(self, num):
        self.queue = collections.deque()
        self.availavle_transport = num


class Port(Station):
    def __init__(self, num):
        super().__init__(num)


class Truck_station(Station):
    def __init__(self, num):
        super().__init__(num)


class Cargo:
    def __init__(self, name, route):
        self.name = name
        self.route = route


class Delivery:
    def __init__(self, *stations):
        self.delivery_in_process = []
        self.returning = []
        self.delivered = []
        self.clean_delivery = set()
        self.clean_return = set()
        self.stations = stations

    def start(self, transport):
        self.delivery_in_process.append(transport)

    def deliver_one_step(self):
        for transport in self.delivery_in_process:
            if transport.delivery_time - 1 != 0:
                transport.delivery_time -= 1
                transport.available -= 1
            else:
                transport.delivery_time -= 1
                self.returning.append(transport)
                self.clean_delivery.add(transport)
                if transport.cargo.route:
                    for i in self.stations:
                        if isinstance(i, Truck_station) and list(transport.cargo.route[0].keys())[0] == 'truck':
                            i.queue.append(transport.cargo)
                        elif isinstance(i, Port) and list(transport.cargo.route[0].keys())[0] == 'ship':
                            i.queue.append(transport.cargo)
                else:
                    self.delivered.append(transport.cargo)
                    print('cargo {} is delivered'.format(transport.cargo.name))

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
            transport.available -= 1
            if transport.available == 0:
                self.clean_return.add(transport)
                for station in self.stations:
                    if isinstance(station, Truck_station) and isinstance(transport, Truck):
                        station.availavle_transport += 1
                    elif isinstance(station, Port) and isinstance(transport, Ship):
                        station.availavle_transport += 1


def create_cargo(name, dict_route):
    route = copy.deepcopy(dict_route)[name]
    return Cargo(name, route)


def cargo_to_stations(cargo_list, route, *stations):
    for _ in cargo_list:
        cargo = create_cargo(_, route)
        for station in stations:
            if list(cargo.route[0].keys())[0] == 'truck' and isinstance(station, Truck_station):
                station.queue.append(cargo)
            elif list(cargo.route[0].keys())[0] == 'ship' and isinstance(station, Port):
                station.queue.append(cargo)


def create_truck(cargo, station):
    destination = Transport.create_transport(cargo, station)
    return Truck(cargo, list(destination.values())[0], list(destination.values())[0] * 2)


def create_ship(cargo, station):
    destination = Transport.create_transport(cargo, station)
    return Ship(cargo, list(destination.values())[0], list(destination.values())[0] * 2)


A = collections.deque([{'truck': 1}, {'ship': 4}])
B = collections.deque([{'truck':5}])
Route = {'A': A, 'B': B}

# инициализируем станции и с количеством транспорта на каждой
truck_station = Truck_station(2)
port = Port(1)

# вводим груз, который нужно доставить
cargo_to_deliver = input()
quantity =  len(cargo_to_deliver)

'''раскидываем груз в очереди у станций(сделано для того, чтобы была возможность 
начинать доставку как из порта, так и со станции грузовиков)'''
cargo_to_stations(cargo_to_deliver, Route, truck_station, port)

# инициализируем сегодняшнюю доставку
today_delivery = Delivery(truck_station, port)
today = GlobalTime()
while quantity != len(today_delivery.delivered):
    while truck_station.availavle_transport and truck_station.queue:
        cargo = truck_station.queue.popleft()
        today_delivery.start(create_truck(cargo, truck_station))
    while port.availavle_transport and port.queue:
        cargo_to_ship = port.queue.popleft()
        today_delivery.start(create_ship(cargo_to_ship, port))
    today_delivery.deliver_one_step()
    today_delivery.check_for_delivered()
    today_delivery.returning_one_step()
    today_delivery.check_for_returned()
    today.an_hour_has_passed()
print('Total delivery time:', today.time_has_passed)
