import click
from detection import detection_py_rules
from check_if_ip_valid import    is_valid_ipv4_network

@click.group()
def cli():
    pass


@cli.command()
@click.option('--rule', '-r', required=True,  help='Rule for a  you request. Please Choose beetween all, check_pcap,check_file_size')
@click.option('--path_list', '-p',required=True, nargs=-1, multiple=True, help='List of paths')
@click.option('--ip_network', '-ip', required=True,help='First IP  Network  for blacklist')
@click.option('--ip_network1', '-ip1',required=True, help='Second IP  Network  for blacklist')
@click.option('--size_list', '-s', nargs=4, type=click.INT, help='List of File MAX Size in the order: JSON, XML, TXT, EVTX in bytes') # można dopisać że to obowiązkowe
def detection(rule,path, ip_network,ip_network1,size_list):
    if not is_valid_ipv4_network(ip_network) or not is_valid_ipv4_network(ip_network1):
        click.echo("Invalid IP Network provided.")
        return
    
    size_list = size_list or [1000000, 1000000, 1000000, 1000000]
    detection_py_rules(rule,path, ip_network,ip_network1,size_list)



if __name__ == "__main__":
    cli()
