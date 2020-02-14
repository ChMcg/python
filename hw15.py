#!/usr/bin/env python3.8
import ipaddress as ip

"""
    Написать класс router.
    Должен иметь методы добавить/удалить/вывести список ip address.
    Должен иметь методы добавить/удалить/вывести список ip routes.

    Есть маршруты к непосредственно-подключенным сетям:
    если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
    значит у него должен быть маршрут:
    к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.

    Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
    то надо проверять доступен ли gateway.

    Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
    192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.

    Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
    до которого у нас пока еще нет маршрута, то должен вылетать exception.

    Например:
    Добавляем ip-address 192.168.5.14/24 eth1.
    Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
    Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
    Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.

    Итого - 1 интерфейс и 3 маршрута в таблице.
"""

class Interface():
    def __init__(self, name: str, network: str):
        self.name = name
        self.network = ip.ip_network(network, strict=False)

    def is_ip_reachable(self, ip_to: str) -> bool:
        return ip.ip_address(ip_to) in self.network
    
    def __eq__(self, other) -> bool:
        # if self.name != other.name: return False
        if self.network != other.network: return False
        return True

    def __repr__(self):
        return f'<Interface "{self.name}" at {self.network}>'

class Route():
    def __init__(self, from_ip: str, to_network: str):
        self.from_ip = ip.ip_address(from_ip)
        self.to_network = ip.ip_network(to_network, strict=False)

    def __eq__(self, other) -> bool:
        if self.from_ip != other.from_ip: return False
        if self.to_network != other.to_network: return False
        return True

    def is_ip_reachable(self, ip_to: str) -> bool:
        return ip.ip_address(ip_to) in self.to_network

    def __repr__(self):
        return f'<Route: {self.from_ip.compressed} -> {self.to_network.compressed}>'

class Router():
    def __init__(self):
        self.interfaces = []
        self.routes = []

    def add_interace(self, name: str, network: str):
        temp = Interface(name, network)
        if not temp in self.interfaces:
            self.interfaces.append(temp)
        else:
            print('Interface already exists')
    
    def add_route(self, from_ip: str, to_network: str):
        if not self.is_ip_reachable(from_ip): 
            raise ValueError(f'\'from_ip\' ({from_ip}) can\'t be reached from current routes')
        self.routes.append(Route(from_ip, to_network))

    def is_ip_reachable(self, target_ip: str) -> bool:
        for interface in self.interfaces:
            if interface.is_ip_reachable(target_ip):
                return True
        for route in self.routes:
            if route.is_ip_reachable(target_ip):
                return True
        return False
    
    def print_info(self):
        for i in self.interfaces:
            print(i.__repr__())
        for r in self.routes:
            print(r.__repr__())

        

def main():
    test = Router()
    test.add_interace('eth1', '192.168.5.14/24')
    test.add_route('192.168.5.1', '172.16.0.0/16')
    try:
        test.add_route('192.168.8.1', '172.24.0.0/16')
    except ValueError as e:
        print('Exception catched:', e)
    test.add_route('172.16.8.1', '172.24.0.0/16')
    test.print_info()

if __name__ == "__main__":
    main()
