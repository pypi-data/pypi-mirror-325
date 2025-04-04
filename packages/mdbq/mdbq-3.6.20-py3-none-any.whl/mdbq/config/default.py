# -*- coding: UTF-8 –*-
import os
import json
import platform
import getpass
import socket
import logging
from mdbq.mysql import mysql

if platform.system() == 'Windows':
    support_path = r'C:\同步空间\BaiduSyncdisk\自动0备份\py\数据更新\support'
elif platform.system() == 'Darwin':
    support_path = f'/Users/{getpass.getuser()}/数据中心/自动0备份/py/数据更新/support'
else:
    support_path = '数据中心/数据更新/support'  # 没有用可以删
logger = logging.getLogger(__name__)


def return_host(conf_data):
    """
    从配置文件数据中获取: username, password, host, port
    :param conf_data:
    :return:
    """
    return conf_data['username'], conf_data['password'], conf_data['host'], conf_data['port']


def return_one_engine(conf_data):
    """
    返回一个 engine
    """
    username, password, host, port = return_host(conf_data)
    return mysql.MysqlUpload(username=username, password=password, host=host, port=port, charset='utf8mb4')


def get_hostname(platform, hostname, sql, local):
    """
    返回一个主机的: username, password, host, port
    """
    config_file = os.path.join(support_path, 'my_config.txt')
    with open(config_file, 'r', encoding='utf-8') as f:
        conf = json.load(f)
    conf_data = conf[platform][hostname][sql][local]
    return return_host(conf_data)


def get_engine():
    if not os.path.isdir(support_path):
        print(f'缺少配置文件，无法读取配置文件： {file}')
        return
    config_file = os.path.join(support_path, 'my_config.txt')

    with open(config_file, 'r', encoding='utf-8') as f:
        conf = json.load(f)

    if socket.gethostname() == 'company' or socket.gethostname() == 'Mac2.local':
        conf_data = conf['Windows']['xigua_lx']['mysql']['remoto']
        m_engine = return_one_engine(conf_data=conf_data)
        conf_data = conf['Windows']['company']['mysql']['local']
        company_engine = return_one_engine(conf_data=conf_data)
        username, password, host, port = return_host(conf_data)  # 顺序不能乱
        conf_data = conf['Windows']['xigua_ts']['mysql']['remoto']
        ts_engine = return_one_engine(conf_data=conf_data)
    elif socket.gethostname() == 'xigua_lx' or socket.gethostname() == 'xigua1' or socket.gethostname() == 'MacBookPro':
        conf_data = conf['Windows']['xigua_lx']['mysql']['local']
        m_engine = return_one_engine(conf_data=conf_data)
        username, password, host, port = return_host(conf_data)  # 顺序不能乱
        conf_data = conf['Windows']['company']['mysql']['remoto']
        company_engine = return_one_engine(conf_data=conf_data)
        conf_data = conf['Windows']['xigua_ts']['mysql']['remoto']
        ts_engine = return_one_engine(conf_data=conf_data)

    else:
        conf_data = conf['Windows']['xigua_lx']['mysql']['remoto']
        m_engine = return_one_engine(conf_data=conf_data)
        username, password, host, port = return_host(conf_data)  # 顺序不能乱
        conf_data = conf['Windows']['company']['mysql']['remoto']
        company_engine = return_one_engine(conf_data=conf_data)
        conf_data = conf['Windows']['xigua_ts']['mysql']['remoto']
        ts_engine = return_one_engine(conf_data=conf_data)

    return m_engine, company_engine, ts_engine, (username, password, host, port)


def write_back(datas):
    """ 将数据写回本地 """
    if not os.path.isdir(support_path):
        print(f'缺少配置文件，无法读取配置文件： {file}')
        return
    file = os.path.join(support_path, 'my_config.txt')
    with open(file, 'w+', encoding='utf-8') as f:
        json.dump(datas, f, ensure_ascii=False, sort_keys=False, indent=4)



if __name__ == '__main__':
    pass
