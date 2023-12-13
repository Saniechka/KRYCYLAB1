from xml.etree import ElementTree
from Evtx.Evtx import Evtx
from Evtx.Views import evtx_record_xml_view

def evtx_to_xml(evtx_path, xml_path):
    with Evtx(evtx_path) as evtx:
        records = [record.xml() for record in evtx.records()]

    # Save each XML record to an XML file
    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write('<?xml version="1.0" encoding="utf-8"?>\n<Records>\n')
        for xml_record in records:
            xml_file.write(xml_record + '\n')
        xml_file.write('</Records>')

# Example usage:
evtx_file_path = '1.evtx'
xml_output_path = 'xmlevtx.xml'
evtx_to_xml(evtx_file_path, xml_output_path)
