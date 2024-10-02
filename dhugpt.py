import argparse
import os
from chat.chat import NormalChat
import dotenv
from chat.chat import create_store, repl_chat
from utils.JsonUtils import append_json_file
from chat.chat import shell_chat, default_assistant_stream_out
from utils.excuteCommand import execute_command_with_prompt
from utils.platformUtils import get_os_type
from dify.chat import chatWithDify
from utils.printCenter import printByRole

dotenv.load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="dhuGPT")
    group = parser.add_mutually_exclusive_group(required=False)
    # 为解析器添加参数
    group.add_argument("-c", "--chat", help="chat sentence")
    group.add_argument("-repl", "--repl", help="chat with memory")
    group.add_argument("-s", "--shell", help="chat with shell command")
    # 创建子解析器
    subparsers = parser.add_subparsers(dest="command")

    # 创建 --dify 子命令
    dify_parser = subparsers.add_parser("dify", help="Dify mode options")
    dify_parser.add_argument("--workflow", help="choose an workflow")
    dify_parser.add_argument("--conversion", help="make a conversion with dify_workflow")

    args = parser.parse_args()
    if args.command == "dify":
        # 指定工作流没有指定对话
        if not args.workflow or not args.conversion:
            printByRole('error','Please specify both --workflow and --conversion')
        else:
            cnt = 0
            while True:
                chatWithDify(args.workflow, args.conversion,cnt)
                cnt = cnt +1


    elif args.chat:
        if os.environ.get('OPENAI_API_KEY') is None:
            OPENAI_API_KEY = input("Please input your api-key")
            os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        try:
            stream = NormalChat(args.chat, os.getenv("DEFAULT_MODEL"))
            default_assistant_stream_out(stream)
        except Exception as e:
            print(e)
    elif args.repl:
        create_store(args.repl)
        while True:
            message = input("\n> ")
            stream = repl_chat(args.repl, message, os.getenv("DEFAULT_MODEL"))
            str_ = default_assistant_stream_out(stream)
            Directory_path = os.getenv('DEFAULT_STORE_PATH')
            file_path = os.path.join(Directory_path, f'{args.repl}.json')
            append_json_file(file_path, 'assistant', str_, p=False)
    elif args.shell:
        os_type = get_os_type()
        stream = shell_chat(args.shell, os.getenv("DEFAULT_MODEL"), os_type=os_type)
        str_ = default_assistant_stream_out(stream)
        execute_command_with_prompt(str_)
    else:
        pass


if __name__ == "__main__":
    main()
