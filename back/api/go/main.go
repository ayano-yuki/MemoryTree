package main

import(
	"database/sql"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	_ "github.com/go-sql-driver/mysql"
	"github.com/labstack/echo"
    "github.com/labstack/echo/middleware"
)

func main(){
	e := echo.New()

	e.Use(middleware.CORS())
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	e.POST("/add", addElement)
	e.POST("/delete", deleteElement)
	e.GET("/get", getAllElement)
	e.GET("/get/:day/:title", getDiary)

	e.Logger.Fatal(e.Start(":8000"))
}

/* MySQLの操作 */
func addElement(c echo.Context) error{
	// 受信データの取得
	var form map[string]interface{}
	c.Bind(&form)
	log.Println(form)

	// データベースのハンドルを取得する
	db, err := sql.Open("mysql", "root:root@tcp(localhost:3306)/web")
	if err != nil {
		// ここではエラーを返さない
		log.Fatal(err)
	}
	defer db.Close()

	// SQLの準備
	ins, err := db.Prepare("INSERT INTO diary VALUES(?, ?, ?)")
	if err != nil {
		log.Fatal(err)
	}
	defer ins.Close()

	// SQLの実行
	res, err := ins.Exec(form["day"], form["title"], form["main"])
	if err != nil {
		log.Fatal(err)
	}

	// 結果の取得
	lastInsertID, err := res.LastInsertId()
	if err != nil {
		log.Fatal(err)
	}
	
	return c.JSON(http.StatusOK, gin.H{
        "msg": "--ADD--",
		"result": lastInsertID,
    })
}

func deleteElement(c echo.Context) error {
	// 受信データの取得
	var form map[string]interface{}
	c.Bind(&form)
	log.Println(form["day"], form["title"])

	// データベースのハンドルを取得する
	db, err := sql.Open("mysql", "root:root@tcp(localhost:3306)/web")
	if err != nil {
		// ここではエラーを返さない
		log.Fatal(err)
	}
	defer db.Close()

	// SQLの準備
	del, err := db.Prepare("DELETE FROM diary WHERE day=? AND title=?")
	if err != nil {
		log.Fatal(err)
	}
	defer del.Close()

	// SQLの実行
	res, err := del.Exec(form["day"], form["title"])
	if err != nil {
		log.Fatal(err)
	}

	// 結果の取得(影響を受ける行の数を取得)
	affected, err := res.RowsAffected()
	if err != nil {
		log.Fatal(err)
	}

	return c.JSON(http.StatusOK, gin.H{
        "msg": "--DELETE--",
		"result": affected,
    })
}

func getAllElement(c echo.Context) error {
	type getInform struct {
		day int
		title string
		main string
	}

	var days []int
	var titles []string
	var mains []string
	
	// データベースのハンドルを取得する
	db, err := sql.Open("mysql", "root:root@tcp(localhost:3306)/web")
	if err != nil {
		// ここではエラーを返さない
		log.Fatal(err)
	}
	defer db.Close()

	// SQLの実行
	rows, err := db.Query("SELECT * FROM diary order by day")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	// 結果の処理
	for rows.Next() {
		var inform getInform
		err := rows.Scan(&inform.day, &inform.title, &inform.main)

		if err != nil {
			panic(err.Error())
		}

		// log.Println(inform.day, inform.title, inform.main)
		days = append(days, inform.day)
		titles = append(titles, inform.title)
		mains = append(mains, inform.main)
	}

	return c.JSON(http.StatusOK, gin.H{
        "msg": "--DO--",
		"day": days,
		"title": titles,
		"main": mains,
    })

}

func getDiary(c echo.Context) error {
	var day int
	var title string
	var main string
	
	// データベースのハンドルを取得する
	db, err := sql.Open("mysql", "root:root@tcp(localhost:3306)/web")
	if err != nil {
		// ここではエラーを返さない
		log.Fatal(err)
	}
	defer db.Close()

	// SQLの準備
	stmt, err := db.Prepare("SELECT * FROM diary WHERE day=? AND title=?")
	if err != nil {
		log.Fatal(err)
	}
	
	err = stmt.QueryRow(c.Param("day"), c.Param("title")).Scan(&day, &title, &main)
	if err != nil {
		panic(err.Error())
	}

	// log.Println(day, title, main)

	return c.JSON(http.StatusOK, gin.H{
        "msg": "--DO--",
		"day": day,
		"title": title,
		"main": main,
    })

}

/* 
参考
# MySQL
- [【Golang】MySQLの基本的な操作を行う](https://www.chuken-engineer.com/entry/2021/09/24/162120)
- [Go言語を真剣に勉強してみた〜データベース接続(MySQL)編〜](https://qiita.com/watataku8911/items/8c94f8f380f91aa3f3e5)

# API
- [GoのJSON操作【プログラミング初心者向け教材】](https://tokitsubaki.com/go-json-manipulation/411/)
- [golang gin でのJson　受け取り](https://teratail.com/questions/322074)
- [【Golang/gin】いつも使ってるgin.Contextの中身、覗いていきませんか？](https://qiita.com/SDTakeuchi/items/7f6314d166580a06d36c)
- [Go Gin爆速入門 (REST API)](https://qiita.com/ozora/items/0597e52b3f9c1759e292)
- [Go言語のechoフレームワークを使用してAPIサーバーを立てる方法](https://ichi-station.com/how-to-use-golang-echo/)
- [Go + Vue.js でGETとPOSTをやってみる](https://qiita.com/ymshun/items/e57446ffa4269376e699)
*/
