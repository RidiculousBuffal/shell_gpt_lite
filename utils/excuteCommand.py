import subprocess
from colorama import Fore,Style,init
import os
import platform
init(autoreset=True)
def execute_command_with_prompt(command):
    prompt_message = f"\n{Fore.YELLOW}你要执行以下命令嘛:\n{Fore.CYAN}>>>{command}\n{Fore.YELLOW}按Y继续,按任意键取消{Style.RESET_ALL}"
    user_input = input(prompt_message)
    if user_input.lower()=='y':
        try:
            if platform.system().lower()=='windows':
                result = subprocess.run([
                    'powershell',
                    '-Command',
                    command
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            else:
                result = subprocess.Popen(
                    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
                )
            # 输出命令的输出
            print(result.stdout)
        except Exception as e:
            print(Fore.RED,"Error")
            print(Fore.WHITE+e)
    else:
        print(Fore.RED, "命令取消")
