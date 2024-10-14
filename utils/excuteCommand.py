import platform
import subprocess
import time
from time import sleep

from colorama import Fore, Style, init

from utils.printCenter import printByRole

init(autoreset=True)


def execute_command_with_prompt(command):
    prompt_message = f"\n{Fore.YELLOW}你要执行以下命令嘛:\n{Fore.CYAN}>>>{command}\n{Fore.YELLOW}按Y继续,按任意键取消{Style.RESET_ALL}"
    user_input = input(prompt_message)
    if user_input.lower() == 'y':
        try:
            if platform.system().lower() == 'windows':
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
            print(Fore.RED, "Error")
            print(Fore.WHITE + e)
    else:
        print(Fore.RED, "命令取消")


def generateShellBash(root):
    time_string = time.strftime('%Y-%m-%d-%H-%M-%S')
    with open(f'dhuBot-{time_string}.sh', 'w') as file:
        for child in root:
            # 打印文本内容，去掉多余的空白
            if (child.tag == 'DHUthink'):
                printByRole("assistant", "DHUBOT THINK:")
                content = f"# {child.text.strip() if child.text else '# I dont want to think here :)'}"
                printByRole("assistant", content, end='\n')
                file.write(content)
            else:
                printByRole("assistant", "DHUBOT WRITE:")
                content = f"{child.text.strip() if child.text else '# Nothing to write here :)'}"
                printByRole("assistant", content, end='\n')
                file.write(content)
            sleep(0.5)
    execute_command_with_prompt(f"sudo bash dhuBot-{time_string}.sh")
