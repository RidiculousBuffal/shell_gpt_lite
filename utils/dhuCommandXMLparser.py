import re
import xml.etree.ElementTree as ET


def parseXML(markdown_string):
    xml_content = re.search(r'```xml\n(.*?)```', markdown_string, re.DOTALL)
    if xml_content:
        xml_data = xml_content.group(1)
        # 解析 XML 数据
        root = ET.fromstring(f'<root>{xml_data}</root>')  # 添加根节点以符合 XML 格式
        return root
    else:
        return None
