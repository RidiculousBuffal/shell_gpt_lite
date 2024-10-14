import os
import dotenv
import json
dotenv.load_dotenv()
class DifyConfig:

    @classmethod
    def _load_config_data(cls):
        # 从环境变量获取配置文件路径
        Dify_config_path = os.getenv('DIFY_CONFIG_PATH')
        if Dify_config_path is None:
            raise ValueError("DIFY_CONFIG_PATH is not set in the environment.")

        # 尝试读取并解析 JSON 文件
        try:
            with open(Dify_config_path, 'r', encoding='utf-8') as config_file:
                config_data = json.load(config_file)
            return config_data
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at: {Dify_config_path}")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the configuration file.")

    @classmethod
    def get_API_KEY(cls, app_name):
        config_data = cls._load_config_data()  # 调用辅助方法

        # 获取 API_KEY
        try:
            api_key = config_data["APPS"][app_name]["API_KEY"]
            return api_key
        except KeyError:
            raise KeyError(f"API_KEY for app '{app_name}' not found in the configuration.")

    @classmethod
    def getConversionID(cls, appName, conversionName):
        config_data = cls._load_config_data()  # 调用辅助方法

        # 获取指定应用程序的 Conversions
        try:
            conversions = config_data["APPS"][appName]["Conversions"]
        except KeyError:
            raise KeyError(f"App '{appName}' not found in the configuration.")

        # 根据 conversionName 获取 conversionId
        try:
            conversion_id = conversions[conversionName]
            return conversion_id
        except KeyError:
            return None

    @classmethod
    def get_api_base_url_and_user(cls):
        config_data = cls._load_config_data()  # 调用辅助方法

        # 获取 API_BASE_URL 和 USER
        try:
            api_base_url = config_data["API_BASE_URL"]
            user = config_data["USER"]
            return api_base_url, user
        except KeyError as e:
            raise KeyError(f"{str(e)} not found in the configuration.")
    @classmethod
    def return_chat_request_components(cls,endpoint,appName,conversionName,query,response_mode="streaming"):
        url,user = cls.get_api_base_url_and_user()
        headers = {'Authorization': f'Bearer {cls.get_API_KEY(appName)}','Content-Type': 'application/json'}
        payload = {
            "user" : user,
            "query": query,
            "response_mode":response_mode,
            "inputs":{}
        }
        if cls.getConversionID(appName,conversionName):
            payload['conversation_id'] = cls.getConversionID(appName,conversionName)
        return  url+f'{endpoint}',payload,headers

    @classmethod
    def _save_config_data(cls, config_data):
        # 从环境变量获取配置文件路径
        Dify_config_path = os.getenv('DIFY_CONFIG_PATH')

        # 尝试将更新后的数据写入 JSON 文件
        try:
            with open(Dify_config_path, 'w', encoding='utf-8') as config_file:
                json.dump(config_data, config_file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise IOError(f"Error writing to configuration file: {e}")

    @classmethod
    def update_conversion_id(cls, appName, conversionName, conversionId):
        config_data = cls._load_config_data()  # 调用辅助方法

        # 获取指定应用程序的 Conversions
        try:
            conversions = config_data["APPS"][appName]["Conversions"]
        except KeyError:
            raise KeyError(f"App '{appName}' not found in the configuration.")

        # 更新 conversionId
        conversions[conversionName] = conversionId

        # 将更新后的数据写入配置文件
        cls._save_config_data(config_data)

