#!/usr/bin/env python # syntax highlightning

from twisted.application import internet, service

from opennsa import setup
from opennsa.backends import dud


TOPOFILE = 'local-topo.owl'

NETWORK_NAME = 'Aruba'
PORT = 9080


proxy = dud.DUDNSIBackend(NETWORK_NAME)
factory = setup.createService(NETWORK_NAME, open(TOPOFILE), proxy, PORT)

application = service.Application("OpenNSA-A")
internet.TCPServer(PORT, factory, interface='localhost').setServiceParent(application)

