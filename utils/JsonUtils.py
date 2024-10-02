import os
import json
from colorama import Fore,Style,init
from utils.printCenter import printByRole
init (autoreset=True)
def print_single_element(role,content):
    printByRole(role,f'''Role:{role}''')
    printByRole(role,f'''Content:{content}''')
def pretty_print_json(json_data):

    if 'message' in json_data:
        for item in json_data['message']:
            role = item.get('role', 'unknown')
            content = item.get('content', 'no content')
            print_single_element(role,content)
            print(Style.RESET_ALL)  # 重置样式


def read_json_file(file_path):
    # 读取 JSON 文件的内容
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    else:
        print(Fore.RED + "文件不存在！")
        return None

def append_json_file(file_path, role,content,p:bool):
    json_data = read_json_file(file_path)
    new_data = {'role':role,'content':content}
    json_data['message'].append(new_data)
    if p:
        print_single_element(role,content)
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    return