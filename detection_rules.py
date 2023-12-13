import ipaddress
from scapy.all import *
from scapy.all import IP,TCP,UDP, ICMP
import os


def check_pcap(ip_network, ip_network1,**kwargs):
    action_alert = 'remote'
    info = ''
    condition = False

    for pcap_file in kwargs['pcap']:
            packets = rdpcap(pcap_file)  # wczytywanie
            MIN_PACKET_LENGTH = 100
            MAX_PACKET_LENGTH = 1600


            NETWORK_TO_CHECK1 = ipaddress.IPv4Network(ip_network)
            NETWORK_TO_CHECK2 = ipaddress.IPv4Network(ip_network1)
            NETWORK_TO_CHECK = [NETWORK_TO_CHECK1, NETWORK_TO_CHECK2]
            

            for packet in packets:
                # Sprawdzenie flag SYN i FIN
                if packet.haslayer(IP) and packet.haslayer(TCP):
                    if packet[TCP].flags & 0x02 or packet[TCP].flags & 0x01:
                        condition = True
                        info += (f'nieoczekiwane polaczenie:{packet}w  pliku {pcap_file}\n')


                # Nieprawidłowe użycie wersji protokołu IP w nagłówku może wskazywać na błędy, anomalie lub próby manipulacji.
                if packet.haslayer(IP) and packet[IP].version != 4:
                    condition = True
                    info+=(f'nieprawidlowa wersja IP w pakecie:{packet}w  pliku {pcap_file}\n')


                # sprawdzenie długosci
                if len(packet) < MIN_PACKET_LENGTH or len(packet) > MAX_PACKET_LENGTH:
                    condition = True
                    info += (f'Anomalia rozmiaru:{packet}w  pliku {pcap_file}\n')

                # próba sprawdzenia dostępnosci
                if packet.haslayer(ICMP) and packet.haslayer(ICMP):
                    condition = True
                    info += (f'Proba sprawdzenia dostepnosci:{packet}w  pliku {pcap_file}\n')

            # sprawdzenie źródłowego adresu IP
                if packet.haslayer(IP) and packet[IP].src:
                    src_ip = ipaddress.IPv4Address(packet[IP].src)
                    if src_ip not in NETWORK_TO_CHECK:
                        condition = True
                        info += (f'Pakiet z nieautoryzowanym ZrOdLowym adresem IP:{packet}w  pliku {pcap_file}\n')


            if not condition:
                action_alert = None
                info = None
            return action_alert, info
    







def check_file_size(max_files_list,**kwargs):
    

    MAX_FILE_SIZE_JSON = max_files_list[0]
    MAX_FILE_SIZE_XML = max_files_list[1]
    MAX_FILE_SIZE_TXT = max_files_list[2]
    MAX_FILE_SIZE_EVTX = max_files_list[3]

    action_alert = 'remote'
    info = ''
    condition = False

    for json_file in kwargs['json']:
        try:
            json_size = os.path.getsize(json_file)  
            if json_size > MAX_FILE_SIZE_JSON:
             condition = True
             info += (f'Size anomaly in  a:{json_file}\n')
        except Exception as e:
            print(f'Error while checking file size: {e}')


    for txt_file in kwargs['txt']:
        try:
            txt_size = os.path.getsize(txt_file) 
            if txt_size > MAX_FILE_SIZE_TXT:
             condition = True
             info += (f'Size anomaly in  a:{txt_file}\n')
        except Exception as e:
            print(f'Error while checking file size: {e}')

    for xml_file in kwargs['xml']:
        try:
            xml_size = os.path.getsize(xml_file)  
            if xml_size > MAX_FILE_SIZE_XML:
                condition = True
                info += (f'Size anomaly in  a:{xml_file}\n')
        except Exception as e:
            print(f'Error while checking file size: {e}')

    for evtx_file in kwargs['evtx']:
        try:
            evtx_size = os.path.getsize(evtx_file)  
            if evtx_size > MAX_FILE_SIZE_EVTX:
                condition = True
                info += (f'Size anomaly in  a:{evtx_file}\n')
        except Exception as e:
            print(f'Error while checking file size: {e}')

    if not condition:
        action_alert = None
        info = None

    return action_alert, info