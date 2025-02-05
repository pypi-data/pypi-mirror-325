# -*- coding: utf-8 -*-
"""
@ Created on 2025-02-05 14:08
---------
@summary: 
---------
@author: XiaoBai
"""
import functools
import time
from nbclass.log import logger


def retry(retry_times=3, interval=0, tag=False):
    """
    普通函数的重试装饰器
    Args:
        retry_times: 重试次数
        interval: 每次重试之间的间隔
        tag: 自定义的异常返回值
    Returns:

    """

    def _retry(func):
        @functools.wraps(func)  # 将函数的原来属性付给新函数
        def wrapper(*args, **kwargs):
            for i in range(retry_times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(
                        "函数 {}:{} 执行失败 重试 {} 次. error {}".format(func.__name__, e.__traceback__.tb_lineno, i, e)
                    )
                    time.sleep(interval)
                    if i >= retry_times:
                        return tag

        return wrapper

    return _retry


def singleton(cls):
    # 将类变为单例类
    instances = {}

    def wrapper(*args, **kwargs):
        # 将参数转化为不可变的元组（因为列表不可作为字典的键）
        key = (args, frozenset(kwargs.items()))
        if key not in instances:
            instances[key] = cls(*args, **kwargs)
        return instances[key]

    return wrapper
