from colorama import Fore,Style,init
init (autoreset=True)
def printByRole(role,content,end='\n'):
    if role == 'assistant' or role == 'system':
        print (Fore.YELLOW+content,end=end)
    elif role == 'user':
        print(Fore.CYAN+content,end=end)
    elif role == 'info':
        print(Fore.LIGHTBLUE_EX,'INFO:----------',content,'----------',end=end)
    elif role == 'citation':
        print(Fore.GREEN+content,end=end)
    elif role == 'error':
        print(Fore.RED+content,end=end)