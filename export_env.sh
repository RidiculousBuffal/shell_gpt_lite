#!/bin/bash

# 定义默认值
DEFAULT_OPENAI_API_KEY=""
DEFAULT_OPENAI_BASE_URL=""
DEFAULT_DEFAULT_PROMPT="你是一个乐于助人的助手-dhu-shellGPT,专注于解决同学们在编程学习中遇到的各式各样的问题"
DEFAULT_DEFAULT_MODEL="gpt-4o-mini"
DEFAULT_STORE_PATH=""
DEFAULT_DIFY_CONFIG_PATH=""

# 提示用户输入并设置环境变量
read -p "请输入 OPENAI_API_KEY [默认: $DEFAULT_OPENAI_API_KEY]: " OPENAI_API_KEY
OPENAI_API_KEY=${OPENAI_API_KEY:-$DEFAULT_OPENAI_API_KEY}

read -p "请输入 OPENAI_BASE_URL [默认: $DEFAULT_OPENAI_BASE_URL]: " OPENAI_BASE_URL
OPENAI_BASE_URL=${OPENAI_BASE_URL:-$DEFAULT_OPENAI_BASE_URL}

read -p "请输入 DEFAULT_PROMPT [默认: $DEFAULT_DEFAULT_PROMPT]: " DEFAULT_PROMPT
DEFAULT_PROMPT=${DEFAULT_PROMPT:-$DEFAULT_DEFAULT_PROMPT}

read -p "请输入 DEFAULT_MODEL [默认: $DEFAULT_MODEL]: " DEFAULT_MODEL
DEFAULT_MODEL=${DEFAULT_MODEL:-$DEFAULT_DEFAULT_MODEL}

read -p "请输入 DEFAULT_STORE_PATH [默认: $DEFAULT_STORE_PATH]: " DEFAULT_STORE_PATH
DEFAULT_STORE_PATH=${DEFAULT_STORE_PATH:-$DEFAULT_STORE_PATH}

read -p "请输入 DIFY_CONFIG_PATH [默认: $DEFAULT_DIFY_CONFIG_PATH]: " DIFY_CONFIG_PATH
DIFY_CONFIG_PATH=${DIFY_CONFIG_PATH:-$DEFAULT_DIFY_CONFIG_PATH}

# 创建文件夹
if [ -n "$DEFAULT_STORE_PATH" ]; then
    mkdir -p "$DEFAULT_STORE_PATH"
    echo "文件夹 $DEFAULT_STORE_PATH 已创建。"
fi

if [ -n "$DIFY_CONFIG_PATH" ]; then
    # 创建文件并写入 JSON 内容
    mkdir -p "$(dirname "$DIFY_CONFIG_PATH")"  # 确保目录存在
    cat <<EOF > "$DIFY_CONFIG_PATH"
{
    "API_BASE_URL": "",
    "USER": "dhu_gpt",
    "APPS": {
        "exampleAPP": {
            "API_KEY": "app-xxx",
            "Conversions": {

            }
        }
    }
}
EOF
    echo "文件 $DIFY_CONFIG_PATH 已创建并写入默认配置。"
fi

# 输出设置的环境变量
echo "设置的环境变量:"
echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\""
echo "OPENAI_BASE_URL=\"$OPENAI_BASE_URL\""
echo "DEFAULT_PROMPT=\"$DEFAULT_PROMPT\""
echo "DEFAULT_MODEL=\"$DEFAULT_MODEL\""
echo "DEFAULT_STORE_PATH=\"$DEFAULT_STORE_PATH\""
echo "DIFY_CONFIG_PATH=\"$DIFY_CONFIG_PATH\""

# 导出环境变量
export OPENAI_API_KEY
export OPENAI_BASE_URL
export DEFAULT_PROMPT
export DEFAULT_MODEL
export DEFAULT_STORE_PATH
export DIFY_CONFIG_PATH
export all_proxy=''
export ALL_PROXY=''
echo "环境变量已导出。"

