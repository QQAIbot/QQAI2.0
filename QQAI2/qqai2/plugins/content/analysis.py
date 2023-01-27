import re
from QQAI2.qqai2.plugins.content.record import *
def AnalysisNews(News: str, command='', symbol='\|', division:bool=True):
    """

    :param News: 文本内容
    :param command: 触发命令
    :param symbol: 可选参数 分离符号不可为空格默认为|
    :param division: 分割可选参数用于执行相关参数的分割，默认为true
    :return:
    """
    Len = re.findall(re.compile('\|'), News)
    if division:
        if len(Len) != 0:
            if len(re.findall(re.compile(symbol), News)) != 0:
                data = News.replace(' ', '')[len(command):len(News.replace(' ', ''))]
                return re.split(symbol, data)
        else:
            return News.replace(command, '').replace(' ', '')
    else:
        return News.replace(' ', '')[len(command):len(News.replace(' ', ''))]
