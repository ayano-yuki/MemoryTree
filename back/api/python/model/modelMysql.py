import pymysql.cursors
 

def addElement(day, title, main):
    # データベースに接続
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='web',
                                cursorclass=pymysql.cursors.DictCursor)
    
    with connection:
        with connection.cursor() as cursor:
            # レコードを挿入
            sql = 'INSERT INTO diary VALUES (%s, %s, %s)'
            cursor.execute(sql, (day, title, main))
    
        # コミットしてトランザクション実行
        connection.commit()


def deleteElement(day, title):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='web',
                                cursorclass=pymysql.cursors.DictCursor)
 
    with connection:
        with connection.cursor() as cursor:
            # データ削除
            sql = "DELETE FROM diary WHERE day=%s AND title=%s"
            cursor.execute(sql, (day, title))
            connection.commit()
            print(cursor.rowcount, 'rows deleted')

def getAllElement():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='web',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # データ読み込み
            sql = "SELECT * FROM diary order by day"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)

    for box in result:
        print(box["day"], box["title"])

    

def getDiary(day, title):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='web',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # データ読み込み
            sql = "SELECT * FROM diary WHERE day=%s AND title=%s"
            cursor.execute(sql, (day, title))
            result = cursor.fetchall()

            if len(result) == 0:
                print("None")

            else :
                print(result[0]["day"])
                print(result[0]["title"])
                print(result[0]["main"])

getAllElement()

"""
Reference
- [PythonでMySQLを操作する（PyMySQL）](https://python-work.com/pymysql/)
"""