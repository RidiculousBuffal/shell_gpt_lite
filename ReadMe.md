# shell_gpt Lite 
## 项目介绍
> 这是一个简易版的shellgpt,参考 [shell_gpt](https://github.com/TheR1D/shell_gpt)实现,目前实现了如下几个功能
> - --chat 普通聊天,没有记忆
> - --repl 记忆聊天,会把之前的对话储存在json中
> - --shell 可以生成针对不同平台的shell脚本,并提示执行
> - dify --workflow --conversion 和配置文件中的dify进行交互
## 配置文件说明
```bash
cp .env.example .env
```
```bash
OPENAI_API_KEY:"OPENAI密钥"
OPENAI_BASE_URL:"OPENAI代理地址"
DEFAULT_PROMPT:"默认Prompt"
DEFAULT_MODEL:"默认模型"
DEFAULT_STORE_PATH:"存储repl的路径"
DIFY_CONFIG_PATH:"dify配置文件参考"
```
对于`DEFAULT_STORE_PATH`你只需要填写一个本地路径即可,每一次新的repl会生成一个json如下:
```json
{
    "message": [
        {
            "role": "system",
            "content": "你是一个乐于助人的助手-dhu-shellGPT,专注于解决同学们在编程学习中遇到的各式各样的问题"
        },
        {
            "role": "user",
            "content": "请记住数字4"
        },
        {
            "role": "assistant",
            "content": "好的，我记住数字4了！有什么与这个数字有关的需要帮助的地方吗？"
        },
        {
            "role": "user",
            "content": "现在把这个数字加上4"
        },
        {
            "role": "assistant",
            "content": "数字4加上4等于8。如果你需要进一步的计算或者其他问题，请告诉我！"
        },
        {
            "role": "user",
            "content": "我第一次让你记住的数字是多少"
        },
        {
            "role": "assistant",
            "content": "你第一次让我记住的数字是4。如果还有其他问题或需要帮助的地方，请随时告诉我！"
        }
    ]
}
```
对于`DIFY_CONFIG_PATH`你需要填写一个dify的配置文件路径如:`G:\\dify_config\\config.json`,这个json的格式如下:
```json
{
    "API_BASE_URL": "https://xxx/v1",
    "USER": "xxx",
    "APPS": {
        "APP_NAME": {
            "API_KEY": "应用的api_key",
            "Conversions": {
                "聊天标题,": "conversion_id"
            }
        }
    }
}
```
其中`Conversions`一开始可以为空,当使用
```bash
python dhugpt.py dify --workflow APP_NAME --conversion ConversionName
```
时候,如果ConversionName为空,那么最后会在该app的conversions的对象中自动增加一条记录
# 使用效果
![Snipaste_2024-09-29_23-17-48.png](img%2FSnipaste_2024-09-29_23-17-48.png)
![Snipaste_2024-09-30_00-06-23.png](img%2FSnipaste_2024-09-30_00-06-23.png)
![Snipaste_2024-10-02_13-20-18.png](img%2FSnipaste_2024-10-02_13-20-18.png)
![Snipaste_2024-10-02_13-21-11.png](img%2FSnipaste_2024-10-02_13-21-11.png)
# 使用说明和开发
TODO 待打包后补充