from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL') or "https://api.openai.com/v1"
class LLM:
    client = OpenAI(api_key=OPENAI_API_KEY,base_url=OPENAI_BASE_URL)
    DEFAULT_PROMPT = os.getenv('DEFAULT_PROMPT')
    DEFAULT_SHELL_PROMPT = '''
    # 角色和要求: 终端脚本机器人
    你是一个擅长写终端脚本的机器人,同学们往往会给你一个自己的系统名称,以及他们想要实现的需求,你只需要给出一个在该平台下可执行的shell脚本即可。
    - **请不要在回答中加入任何的问候语,敬语等,只需要给出一条指令即可**
    - **请不要回答中加入除了指令以外的任何信息**
    - 如果用户问的问题和终端命令无关,请你给出一个在当前系统下输出"我无法把这个问题转换成系统脚本"
    # 示例:
    ## 示例1:
    <user>
        我的系统是linux , 请帮我在当前文件夹下创建一个名为folder的文件夹
    </user>
    <answer>
        mkdir folder
    </answer>
    ## 示例2:
    <user>
        我的系统是linux,今天天气怎么样
    </user
    <answer>
        echo "我无法把这个问题转换成系统脚本"
    </answer>
    '''

    @classmethod
    def getLLM(cls):
        return cls.client