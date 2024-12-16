import yaml
import os


def returnConfigPath():
    """
    返回配置文件夹路径555
    :return:
    """
    current_path = os.path.dirname(__file__)
    current_list_path = current_path.split('\\')[0:-1]
    configPath = '/'.join(current_list_path) + '/Config/'
    return configPath


def returnConfigData():
    """
    返回配置文件数据（YAML格式），优先使用.env.Config中的配置
    :return:
    """
    current_path = returnConfigPath()
    
    # 读取.env.Config文件
    env_config_path = current_path + '/.env.Config'
    env_config_data = {}
    if os.path.exists(env_config_path):
        with open(env_config_path, mode='r', encoding='UTF-8') as env_file:
            for line in env_file:
                if line.strip() and not line.startswith('#'):  # 忽略空行和注释
                    key, value = line.strip().split('=', 1)
                    env_config_data[key] = value.strip()
    
    # 读取Config.yaml文件
    configData = yaml.load(open(current_path + '/Config.yaml', mode='r', encoding='UTF-8'), yaml.Loader)
    
    # 合并配置，优先使用.env.Config中的值
    for key, value in env_config_data.items():
        if value:  # 仅当.env.Config中的值不为空时才使用
            configData[key] = value
    
    return configData


def returnFingerConfigData():
    """
    返回指纹配置文件数据
    :return:
    """
    current_path = returnConfigPath()
    configData = yaml.load(open(current_path + '/Finger.yaml', mode='r', encoding='UTF-8'), yaml.Loader)
    return configData


def returnFeishuConfigData():
    """
    返回飞书配置文件数据
    :return:
    """
    current_path = returnConfigPath()
    configData = yaml.load(open(current_path + '/Feishu.yaml', mode='r', encoding='UTF-8'), yaml.Loader)
    return configData


def saveFeishuConfigData(configData):
    """
    保存飞书配置
    :param configData:
    :return:
    """
    current_path = returnConfigPath()
    with open(current_path + '/Feishu.yaml', mode='w') as file:
        yaml.dump(configData, file)


def returnUserDbPath():
    return returnConfigPath() + 'User.db'


def returnRoomDbPath():
    return returnConfigPath() + 'Room.db'


def returnGhDbPath():
    return returnConfigPath() + 'Gh.db'


def returnPointDbPath():
    return returnConfigPath() + 'Point.db'
