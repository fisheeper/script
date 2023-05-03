'''
该代码用于执行sql 文件
参数：
--db 指定数据库名称
--param 指定数据库里的参数。 default.py 里配置了很多默认的时间参数，可以通过#{LAST_DAY}来获取，
--sql_text 只指定sql内容
--sql_file 指定sql文件
python runner.py  --db=wer --param="{'time':#{last1hour}}" --sql_text=delete from aa --sql_file=aaa.sql
'''
import jenkinsapi
import logging
import argparse
import configparser
from db import CommonDb

class Runner(object):
    def __init__(self, db, sql_raw, param_raw):
        self.db = self.__init_db_connection(db)
        assert self.db
        self.sql = self.__load_sql_pattern(sql_raw)
        assert self.sql
        self.param = self.__load_prams(param_raw)

    def __load_prams(self):
        '''
        加载参数, 参数为json格式
        '''
        pass

    def __load_sql_pattern(self, sql_raw):
        '''
        加载sql
        '''
        sql_pattern = None
        try:
            with open(sql_raw) as sql_file:
                sql_pattern = sql_file.read()
        except:
            print(f"{sql_raw} 参数不是文件，是文本！")
            sql_pattern = sql_raw
        try:
            return sql_pattern.format()
        except:
            raise Exception("参数错误")

    def __parse_sql(self):
        '''
        替换sql里的参数，生成完整的待执行sql
        '''
        pass

    def __init_db_connection(self, db_label):
        return CommonDb(db_label)

    def __init_logger(self):
        '''
        生成日志对象
        '''
        pass


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--database')
    parser.add_argument('-text', '--sql_text')
    parser.add_argument('-file', '--sql_file')
    parser.add_argument('-p', '--param')
    args = parser.parse_args()
    print(args)
    return args


if __name__ == '__main__':
    args = get_args()
    kargs = vars(args)
    # Runner(**kargs)

