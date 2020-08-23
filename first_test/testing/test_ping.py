"""
Arquivo de aprendizagem para criação de um package simples.

"""

from pythonping import ping


def test_ping(ip):
    ping(ip, verbose=True)
