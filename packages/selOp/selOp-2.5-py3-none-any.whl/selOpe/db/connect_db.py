import sqlite3
import os


class SQLiteHelper:
    def __init__(self, db_name, create_tables_sql=None, crud_sql=None):
        """
        初始化数据库连接
        :param db_name: 数据库文件名
        :param create_tables_sql: 可选参数，传入自定义建表语句
        :param crud_sql: 可选参数，传入自定义增删改查 SQL 语句字典
        """
        self.db_name = db_name
        self.create_tables_sql = create_tables_sql
        self.crud_sql = crud_sql if crud_sql else {}
        self.connection = None
        self.cursor = None
        self._connect()

    def _connect(self):
        """初始化数据库连接"""
        if not os.path.exists(self.db_name):
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"数据库'{self.db_name}'不存在，已创建并连接。")
            if self.create_tables_sql:
                self._create_tables()
        else:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"数据库'{self.db_name}'已存在，已连接。")

    def _create_tables(self):
        """创建表格，使用外部传入的建表语句"""
        if self.create_tables_sql:
            for sql in self.create_tables_sql:
                self.cursor.execute(sql)
            self.connection.commit()

    def execute_crud(self, action, table, data=None, where=None):
        """
        执行增删改查操作
        :param action: 操作类型 ('insert', 'select', 'update', 'delete')
        :param table: 操作的表名
        :param data: 插入或更新时需要的数据（字典格式）
        :param where: 删除或更新时的条件（字典格式）
        :return: 查询结果或操作成功与否
        """
        # 获取对应的 SQL 语句
        if action not in self.crud_sql or table not in self.crud_sql[action]:
            print(f"未定义{action}操作的SQL语句")
            return None

        sql = self.crud_sql[action].get(table)
        if not sql:
            print(f"未找到表'{table}'的{action}操作 SQL")
            return None

        # 参数化处理
        if action == 'insert':
            # 插入操作
            columns = ', '.join(data.keys())
            placeholders = ', '.join('?' * len(data))
            sql = sql.format(columns=columns, placeholders=placeholders)
            self.cursor.execute(sql, tuple(data.values()))
            self.connection.commit()
            return True

        elif action == 'select':
            # 查询操作
            where_clause = " AND ".join([f"{k} = ?" for k in where.keys()]) if where else ""
            if where_clause:
                sql += f" WHERE {where_clause}"
            self.cursor.execute(sql, tuple(where.values()) if where else ())
            return self.cursor.fetchall()

        elif action == 'update':
            # 更新操作
            set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
            where_clause = " AND ".join([f"{k} = ?" for k in where.keys()])
            sql = sql.format(set_clause=set_clause, where_clause=where_clause)
            self.cursor.execute(sql, tuple(data.values()) + tuple(where.values()))
            self.connection.commit()
            return True

        elif action == 'delete':
            # 删除操作
            where_clause = " AND ".join([f"{k} = ?" for k in where.keys()])
            sql += f" WHERE {where_clause}"
            self.cursor.execute(sql, tuple(where.values()))
            self.connection.commit()
            return True

        return None

    def close(self):
        """关闭数据库连接"""
        if self.connection:
            self.connection.close()
            print(f"数据库'{self.db_name}'已关闭。")


"""示例
# 外部传入建表语句
create_tables_sql = [
    '''
    CREATE TABLE IF NOT EXISTS browsers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        version TEXT NOT NULL,
        os TEXT NOT NULL,
        driver_version TEXT NOT NULL
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS test_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        duration INTEGER,
        browser_id INTEGER,
        FOREIGN KEY (browser_id) REFERENCES browsers(id)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS operations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_case_id INTEGER,
        step_number INTEGER NOT NULL,
        action TEXT NOT NULL,
        element TEXT NOT NULL,
        result TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        duration INTEGER NOT NULL,
        log TEXT,
        FOREIGN KEY (test_case_id) REFERENCES test_cases(id)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation_id INTEGER,
        log_type TEXT NOT NULL,
        message TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (operation_id) REFERENCES operations(id)
    );
    '''
]

# 创建SQLiteHelper实例，并传入建表语句
db = SQLiteHelper('selenium_automation.db', create_tables_sql=create_tables_sql)

------增删改查
# 外部传入增删改查 SQL 语句模板
crud_sql = {
    'insert': {
        'browsers': 'INSERT INTO browsers ({columns}) VALUES ({placeholders})',
        'test_cases': 'INSERT INTO test_cases ({columns}) VALUES ({placeholders})',
        'operations': 'INSERT INTO operations ({columns}) VALUES ({placeholders})',
        'logs': 'INSERT INTO logs ({columns}) VALUES ({placeholders})',
    },
    'select': {
        'browsers': 'SELECT * FROM browsers',
        'test_cases': 'SELECT * FROM test_cases',
        'operations': 'SELECT * FROM operations',
        'logs': 'SELECT * FROM logs',
    },
    'update': {
        'browsers': 'UPDATE browsers SET {set_clause} WHERE {where_clause}',
        'test_cases': 'UPDATE test_cases SET {set_clause} WHERE {where_clause}',
        'operations': 'UPDATE operations SET {set_clause} WHERE {where_clause}',
        'logs': 'UPDATE logs SET {set_clause} WHERE {where_clause}',
    },
    'delete': {
        'browsers': 'DELETE FROM browsers',
        'test_cases': 'DELETE FROM test_cases',
        'operations': 'DELETE FROM operations',
        'logs': 'DELETE FROM logs',
    }
}
------插入数据
db = SQLiteHelper('selenium_automation.db', create_tables_sql=create_tables_sql, crud_sql=crud_sql)

# 插入一条浏览器数据
data = {'name': 'Chrome', 'version': '96.0.4664.93', 'os': 'Windows 10', 'driver_version': '96.0.4664.93'}
db.execute_crud('insert', 'browsers', data)

# 插入一条测试用例数据
data = {'name': 'Login Test', 'description': 'Test login functionality', 'status': 'In Progress', 
        'start_time': '2025-02-06 10:00:00', 'end_time': '2025-02-06 10:05:00', 'duration': 300, 'browser_id': 1}
db.execute_crud('insert', 'test_cases', data)

------查询
# 查询所有浏览器信息
result = db.execute_crud('select', 'browsers')
print(result)

# 查询特定条件的数据
where = {'name': 'Chrome'}
result = db.execute_crud('select', 'browsers', where=where)
print(result)

------更新
# 更新浏览器版本
data = {'version': '97.0.4692.71'}
where = {'name': 'Chrome'}
db.execute_crud('update', 'browsers', data, where)

------删除
# 删除指定浏览器
where = {'name': 'Chrome'}
db.execute_crud('delete', 'browsers', where=where)


"""
