import pymysql.cursors
import base64
from starlette.middleware.cors import CORSMiddleware # 追加
from fastapi import FastAPI
from pydantic import BaseModel
import model.modelWordCloud as mwc

app = FastAPI()

# CORSを回避するために追加（今回の肝）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

class data1(BaseModel):
    day: int
    title: str
    main: str

class data2(BaseModel):
    day: int
    title: str

 
@app.post("/add")
def addElement(data: data1):
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
            cursor.execute(sql, (data.day, data.title, data.main))
    
        # コミットしてトランザクション実行
        connection.commit()
    
    return {"msg": "--ADD--",}

@app.post("/delete")
def deleteElement(data: data2):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='web',
                                cursorclass=pymysql.cursors.DictCursor)
 
    with connection:
        with connection.cursor() as cursor:
            # データ削除
            sql = "DELETE FROM diary WHERE day=%s AND title=%s"
            cursor.execute(sql, (data.day, data.title))
            connection.commit()
    return {"msg": "--DELETE--",}

@app.get("/get")
def getAllElement():
    boxDay = []
    boxTitle = []
    boxMain = []
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

    for box in result:
        boxDay.append(box["day"])
        boxTitle.append(box["title"])
        boxMain.append(box["main"])

    return {
            "msg"  : "--DO--",
            "day"  : boxDay,
            "title": boxTitle,
            "main" : boxMain,
        }

@app.get("/get/{day}/{title}")
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
        return {
            "msg"  : "--DO--",
            "day"  : 0,
            "title": "None",
            "main" : "None",
        }

    else :
        return {
            "msg"  : "--DO--",
            "day"  : result[0]["day"],
            "title": result[0]["title"],
            "main" : result[0]["main"],
        }

@app.get("/tree")
def createImage():
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
    
    boxMain = []
    for box in result:
        boxMain.append(box["main"])

    src = ""
    for box in boxMain:
        src = src + box

    mwc.create_wordcrowd(src)

    with open("WC.png", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        b64_string = str(b64_string)
        ret = "data:image/png;base64,{}".format(b64_string[2:-1])

    return{
        "msg" : "--DO--",
        "img" : ret
    }


"""
Reference
- [PythonでMySQLを操作する（PyMySQL）](https://python-work.com/pymysql/)
- [FastAPIでCORSを回避](https://qiita.com/satto_sann/items/0e1f5dbbe62efc612a78)
- [FastAPI - Swagger UI](http://localhost:8000/docs)
"""