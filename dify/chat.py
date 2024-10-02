import http.client
import json

import requests

from config.DifyConfig import DifyConfig
from utils.printCenter import printByRole


def _printCitation(citlist: []):
    for obj in citlist:
        printByRole('citation', f'''-------------------------------''')
        printByRole('citation', f'''索引文档:{obj['dataset_name']}''')
        printByRole('citation', f'''索引内容:{obj['content']}''')
        printByRole('citation', f'''索引评分:{obj['score']}''')
        printByRole('citation',f'''-------------------------------''')


def _has_retriever_resources(obj):
    # 判断 obj 是否有 "metadata" 属性，并且 "metadata" 中是否有 "retriever_resources"
    if isinstance(obj, dict):
        # 检查 "metadata" 是否在 obj 中
        if "metadata" in obj:
            # 检查 "retriever_resources" 是否在 "metadata" 中，并且它是一个列表
            if "retriever_resources" in obj["metadata"] and isinstance(obj["metadata"]["retriever_resources"], list):
                return True
    return False


def chatWithDify(appName, conversionName,cnt):
    baseurl, user = DifyConfig.get_api_base_url_and_user()
    if not DifyConfig.getConversionID(appName, conversionName):
        # 新对话,展示开始引导
        printByRole('info', f'''进入到新对话{conversionName}''')
        url = f'''{baseurl}/parameters'''
        payload = {}
        headers = {
            'Authorization': f'Bearer {DifyConfig.get_API_KEY(appName)}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = response.json()
        printByRole('system', 'Role:system')
        printByRole('system', json_data['opening_statement'])
    else:
        if cnt == 0 :
            printByRole('info', f'''欢迎回到对话{conversionName}''')
            url = f'{baseurl}/messages?conversation_id={DifyConfig.getConversionID(appName, conversionName)}&user={user}'
            headers = {
                'Authorization': f'Bearer {DifyConfig.get_API_KEY(appName)}'
            }
            response = requests.request("GET", url, headers=headers,data={})
            json_data = response.json()
            for item in json_data['data']:
                printByRole('user','Role:user')
                printByRole('user', f'Content:{item['query']}')
                printByRole('system', "Role:system")
                printByRole('system',f"Content:{item['answer']}")
    query = input('>')
    printByRole('user', 'Role:user')
    printByRole('user', query)
    conn = http.client.HTTPSConnection(baseurl.replace('https://', '').replace('/v1', ''))
    url, payload, headers = DifyConfig.return_chat_request_components('/chat-messages', appName, conversionName, query)
    conn.request("POST", '/v1/chat-messages', json.dumps(payload), headers)
    response = conn.getresponse()
    if response.getheader('Content-Type') == 'text/event-stream; charset=utf-8':
        while True:
            line = response.readline().decode('utf-8')
            # 如果没有更多行，退出循环
            if not line:
                break
            # 检查是否是 data 开头的行
            if line.startswith("data: "):
                # 提取 JSON 数据
                json_str = line[len("data: "):].strip()
                # 解析 JSON 数据
                try:
                    json_data = json.loads(json_str)
                    if json_data['event'] == "message":
                        printByRole('assistant', json_data['answer'], end='')
                    elif json_data['event'] == "message_end":
                        DifyConfig.update_conversion_id(appName,conversionName, json_data['conversation_id'])
                        if _has_retriever_resources(json_data):
                            _printCitation(json_data['metadata']['retriever_resources'])
                except json.JSONDecodeError:
                    pass
        conn.close()
