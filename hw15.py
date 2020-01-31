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

class interface():
    def __init__(self, name: str, network: str):
        self.name = name
        self.network = ip.ip_network(network, strict=False)
    
    def __repr__(self):
        return f'<interface "{self.name}" at {self.network}>'

class route():
    def __init__(self, from_ip: ip.IPv4Address, to_ip: ip.IPv4Address):
        self.from_ip = from_ip
        self.to_ip = to_ip

class router():
    def __init__(self):
        self.interfaces = []
        self.routes = []

    def add_interace(self, name: str, network: str):
        self.interfaces.append(interface(name, interface))
    
    def add_route(self, from_ip: str, to_ip: str):
        self.routes.append(route(from_ip, to_ip))
        

def main():
    pass

if __name__ == "__main__":
    main()