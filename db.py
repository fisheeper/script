import pymysql

DbConnect = {
    'mysql': pymysql
}


class CommonDb:
    '''
    通过配置文件里的type类型来初始化数据库连接，
    抽象各种数据库的查询和事务提交操作
    '''
    def __init__(self,db) -> None:
        pass

    def query(self):
        pass

    def start_transaction(self):
        pass

    def __load_connector(self):
        pass

    def __load_db_connection(self):
        pass