import collections
import copy


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


def create_cargo(name, dict_route):
    route = copy.deepcopy(dict_route)[name]
    return Cargo(name, route)


def create_truck(cargo, station):
    destination = Transport.create_transport(cargo, station)
    return Truck(cargo, list(destination.values())[0], list(destination.values())[0]*2)


def create_ship(cargo, station):
    destination = Transport.create_transport(cargo, station)
    return Ship(cargo, list(destination.values())[0], list(destination.values())[0]*2)


def plus_hour(transport):
    transport.delivery_time -= 1
    transport.available -= 1


A = collections.deque([{'truck': 1}, {'ship': 4}])
B = collections.deque([{'truck': 5}])
Route = {'A': A, 'B': B}

Total_time = 0
truck_station = Truck_station(2)
port = Port(1)

delivery = []
returning = []
DELIVERED = []
cargo_to_deliver = input()
quantity = len(cargo_to_deliver)
for c_ in cargo_to_deliver:
    cargo = create_cargo(c_, Route)
    if list(cargo.route[0].keys())[0] == 'truck':
        truck_station.queue.append(cargo)
    else:
        port.queue.append(cargo)

while quantity != len(DELIVERED):
    while truck_station.availavle_transport and truck_station.queue:
        cargo = truck_station.queue.popleft()
        delivery.append(create_truck(cargo, truck_station))
    while port.availavle_transport and port.queue:
        cargo_to_ship = port.queue.popleft()
        delivery.append(create_ship(cargo_to_ship, port))
    to_del = []
    for transport in delivery:
        if transport.delivery_time-1 != 0:
            plus_hour(transport)
        else:
            transport.delivery_time -= 1
            returning.append(transport)
            to_del.append(transport)
            cargo_delivered = transport.cargo
            if cargo_delivered.route:
                destination = cargo_delivered.route[0]
                if list(destination.keys())[0] == 'truck':
                    truck_station.queue.append(cargo_delivered)
                else:
                    port.queue.append(cargo_delivered)
            else:
                DELIVERED.append(cargo_delivered)

    if to_del:
        for i in to_del:
            delivery.remove(i)
    to_del_return = []
    for transport in returning:
        transport.available -= 1
        if transport.available == 0:
            to_del_return.append(transport)
            if isinstance(transport, Truck):
                truck_station.availavle_transport += 1
            else:
                port.availavle_transport += 1
    if to_del_return:
        for i in to_del_return:
            returning.remove(i)
    Total_time += 1
print(Total_time)
