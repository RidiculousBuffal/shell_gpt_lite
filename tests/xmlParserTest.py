import re
import xml.etree.ElementTree as ET
from time import sleep

# 你的字符串（包含 Markdown 格式）
markdown_string = '''
```xml
<DHUthink>
    To analyze the current performance of a Linux host, I will need to use various tools like `top`, `vmstat`, and `iostat`. There are no additional packages required for these basic commands.
</DHUthink>
<DHUPackage />
<DHUthink>
    The analysis may benefit from knowing the current directory and kernel information, so I will export those environment variables.
</DHUthink>
<DHUenv>
    export current_dir=$(pwd)
    export kernel_info=$(uname -a)
</DHUenv>
<DHUthink>
    To analyze the performance, I should run commands that display system resource usage. I will use `top`, `vmstat`, and `iostat` to gather comprehensive performance metrics.
</DHUthink>
<DHUcommand>
    echo "Current Directory: $current_dir"
    echo "Kernel Information: $kernel_info"
    echo "Analyzing CPU and Memory Usage:"
    top -b -n 1 | head -n 20
    echo "Analyzing Memory Statistics:"
    vmstat 1 5
    echo "Analyzing I/O Statistics:"
    iostat 1 5
</DHUcommand>
```
'''

# 提取 XML 内容
xml_content = re.search(r'```xml\n(.*?)```', markdown_string, re.DOTALL)
if xml_content:
    xml_data = xml_content.group(1)
    # 解析 XML 数据
    root = ET.fromstring(f'<root>{xml_data}</root>')  # 添加根节点以符合 XML 格式

    # 提取信息
    for child in root:
        # 打印文本内容，去掉多余的空白
        if (child.tag == 'DHUthink'):
            print("DHUBOT THINK:")
            print(f"# {child.text.strip() if child.text else '# I dont want to think here :)'} ")

        else:
            print("DHUBOT WRITE:")
            print(f"{child.text.strip() if child.text else '# Nothing to write here :)'}")
        sleep(0.5)
else:
    print("No XML content found.")
