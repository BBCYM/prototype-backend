# Prototype_backend
###### tags: `django`
1. <font color="red">**切記勿將機密資料提交到git repo紀錄裡
可在.gitignore新增機密資料的檔名，以避免在commit時提交credential**</font>
2. <font color="red">**不要在這個hackmd文件寫任何機密**</font>
## branch分配

|   Name   | Branch name |
|:--------:|:-----------:|
|   Bob    |    schua    |
|  yojin   |    yojin    |
|  caicai  |     cai     |
| michelle |  michelle   |
|  bobolu  |    bobo     |
## clone下來後
在資料夾內用pipenv產生虛擬環境並下載套件
```bash=
pipenv install
```
進入pipenv shell
```bash=
pipenv shell
```
開server
```bash=
python manage.py runserver
```