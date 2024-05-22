# MySQL

## データベースの生成

```mysql
CREATE TABLE [IF NOT EXISTS] web.diary(
	day int,
    title varchar(100),
    main varchar(1000)
);
```

## ログイン
```
mysql -u root -proot
```

# 参考

- [テーブルを作成する(CREATE TABLE文)](https://www.javadrive.jp/mysql/table/index1.html)