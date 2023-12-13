from Evtx.Evtx import Evtx
from Evtx.Views import evtx_record_xml_view

def evtx_to_txt(evtx_path, txt_path):
    with Evtx(evtx_path) as evtx:
        records = [record.xml() for record in evtx.records()]

    # Save each XML record to a text file
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for xml_record in records:
            txt_file.write(xml_record + '\n')

# Example usage:
evtx_file_path = '1.evtx'
txt_output_path = '1.txt'
evtx_to_txt(evtx_file_path, txt_output_path)
