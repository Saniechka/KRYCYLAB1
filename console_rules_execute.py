import click
from detection import detection_py_rules

@click.group()
def cli():
    pass


@cli.command
@cli.options('--rule', '-r', required=True,  help='Rule for a  you request. Please Choose beetween all, check_pcap,check_file_size')
@click.option('--path_list', '-p',required=True, nargs=-1, multiple=True, help='List of paths')
@click.option('--ip', '-ip', nargs=-1, multiple=True, help='List of IP   for blacklist')
@click.option('--size_list', '-s', nargs=-1, multiple=True, help='List of  File MAX Size in the next order: JSON, XML,TXT,EVTX')
def detection(rule,path, ip,size_list):
    detection_py_rules(rule,path, ip,size_list)



if __name__ == "__main__":
    cli()
