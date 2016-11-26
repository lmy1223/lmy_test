#!/usr/bin/python
# coding=utf-8
# -*- coding : utf-8 -*-
__author__ = ''
import os
import traceback
from ConfigParser import SafeConfigParser


def init_storage_config(main_dir, env_name):
    config_dir = os.path.join(main_dir, 'config', env_name)
    target_dir = os.path.join(main_dir, 'storage', 'config')

    nos_conf_files = ["credentials.properties", "host.properties", "log4j.properties"]
    source_config_files = [os.path.join(config_dir, nos_conf_files) for nos_conf in nos_conf_files]
    target_config_files = [os.path.join(target_dir, nos_conf) for nos_conf in nos_conf_files]
    for source, target in zip(source_config_files, target_config_files):
        with open(source) as s, open(target) as t:
            t.write(s.read())


# 初始化环境
def init_runtime_env():
    parser = SafeConfigParser(allow_no_value=True)
    try:
        main_dir = os.path.split(os.path.realpath(__file__))[0]
        parser.read(os.path.join(main_dir, "env.cfg"))
        env_name = parser.get('env', 'environment')
        init_storage_config(main_dir, env_name)
    except Exception as e:
        traceback.format_exc()
        raise Exception("init environment error :{0}".format(e))


if __name__ == '__main__':
    init_runtime_env()
