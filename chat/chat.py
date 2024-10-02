from models.OpenAIClient import LLM
import os
import dotenv
from utils.JsonUtils import read_json_file,pretty_print_json,append_json_file
import json
from colorama import Fore,Style,init

from utils.printCenter import printByRole

init (autoreset=True)
dotenv.load_dotenv()
def NormalChat(message:str,model:str):
    llm = LLM.getLLM()
    completions = llm.chat.completions.create(
            model=model,
            messages=[
                {'role':'system','content':LLM.DEFAULT_PROMPT},
                {'role':'user','content':message}
            ],
        stream=True
    )
    return completions
def memChat(messages,model):
    llm = LLM.getLLM()
    completions = llm.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )
    return completions
def shell_chat(message,model,os_type):
    llm = LLM.getLLM()
    completions = llm.chat.completions.create(
        model=model,
        messages=[
            {'role':'system','content':LLM.DEFAULT_SHELL_PROMPT},
            {'role':'user','content':f'''我的系统是${os_type}'''},
            {'role':'user','content':message}
        ],
        stream=True
    )
    return completions
def create_store (conversionName:str):
    Directory_path = os.getenv('DEFAULT_STORE_PATH')
    file_path = os.path.join(Directory_path, f'{conversionName}.json')
    data = {'message':[{'role':'system','content':LLM.DEFAULT_PROMPT}],}
    if os.path.exists(file_path):
        json_data = read_json_file(file_path)
        if json_data:
            printByRole('info',f'''进入到{conversionName}''')
            pretty_print_json(json_data)
            return json_data
    else:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)  # 写入 JSON 文件
        printByRole('info',f"JSON 文件已创建：{file_path}")
        printByRole('info',f'''进入到{conversionName}''')
        return
def repl_chat (conversionName,content,model):
    Directory_path = os.getenv('DEFAULT_STORE_PATH')
    file_path = os.path.join(Directory_path, f'{conversionName}.json')
    append_json_file(file_path,"user",content,p=True)
    messages = read_json_file(file_path)['message']
    return memChat(messages,model)

def default_assistant_stream_out(stream):
    printByRole('assistant',f"Role: assistant")
    printByRole('assistant',f"Content:")
    str_ = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            str_ += chunk.choices[0].delta.content
            printByRole('assistant',chunk.choices[0].delta.content,end='')
    return str_
