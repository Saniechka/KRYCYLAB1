import os
from detection_rules import check_file_size, check_pcap

def detection_py_rules(rule, path_list):
    extensions = {"check_file_size": ['evtx', 'json', 'xml', 'txt'], "check_pcap": ['pcap']}

    try:

        if rule == "check_file_size":
            files_to_check = get_files(path_list, extensions[rule])

            action_alert, info = check_file_size(json=files_to_check['json'],
                                                 xml=files_to_check['xml'],
                                                 txt=files_to_check['txt'],
                                                 evtx=files_to_check['evtx'])
            if action_alert is not None:
                print(action_alert) #TODO
                print(info) #TODO

        elif rule == "check_pcap":
            files_to_check = get_files(path_list, extensions[rule])
            
            action_alert, info = check_pcap(pcap=files_to_check['pcap'])
            print("1")
            if action_alert is not None:
                print(action_alert) #TODO
                print(info) #TODO

        elif rule == "all":
            files_to_check_check_pcap = get_files(path_list, extensions["check_pcap"])
            files_to_check_check_file_size = get_files(path_list, extensions["check_file_size"])

            action_alert, info = check_pcap(pcap=files_to_check_check_pcap['pcap'])
            if action_alert is not None:
                print(action_alert)  # TODO
                print(info)  # TODO
            action_alert, info = check_file_size(json=files_to_check_check_file_size['json'],
                                                 xml=files_to_check_check_file_size['xml'],
                                                 txt=files_to_check_check_file_size['txt'],
                                                 evtx=files_to_check_check_file_size['evtx'])
            if action_alert is not None:
                print(action_alert)  # TODO
                print(info)  # TODO

        else:
            print("Error: Provided non-existent rule")
    except Exception as e:
        print(f"{e}")


def get_files(path_list, extensions=['pcap', 'evtx', 'json', 'xml', 'txt']):
    result_files = {'pcap': [], 'json': [], 'xml': [], 'txt': [], 'evtx': []}

    for path in path_list:
        if os.path.isfile(path):
            _, file_extension = os.path.splitext(path)
            if file_extension[1:] in extensions:
                result_files[file_extension[1:]].append(path)
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    _, file_extension = os.path.splitext(file)
                    if file_extension[1:] in extensions:
                        result_files[file_extension[1:]].append(os.path.join(root, file))

    return result_files

def add_to_dict(file_dict, extension, file_path):
    if extension not in file_dict:
        file_dict[extension] = [file_path]
    else:
        file_dict[extension].append(file_path)

if __name__ == "__main__":
    # 'foldertxt/'
    paths = ['foldertxt/', "folderzPCAPAMI/", "folerevtx/"]
    #print(get_files(paths))
    #paths = ['folderzPCAPAMI/new.pcap']
    detection_py_rules("check_file_size", paths)

    #print(selected_files)

