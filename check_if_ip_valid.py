import ipaddress

def is_valid_ipv4_network(network_str):
    try:
        ipaddress.IPv4Network(network_str)
        return True
    except ValueError:
        return False