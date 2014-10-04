# Project Anchovy

## 개발환경
* python 3.4
* django 1.7
* mysql 5.x

## 팁 혹은 트러블 슈팅
## 3.4 virtualenv 설치
http://novafactory.net/archives/tag/python3-4

```sh
claztec:~ claztec$ pip3.4 install virtualenv
Downloading/unpacking virtualenv
  Downloading virtualenv-1.11.6-py2.py3-none-any.whl (1.6MB): 1.6MB downloaded
Installing collected packages: virtualenv
Successfully installed virtualenv
Cleaning up...
claztec:~ claztec$
claztec:Documents claztec$ mkdir hurry
claztec:Documents claztec$ cd hurry/
claztec:hurry claztec$ virtualenv-3.4
-bash: virtualenv-3.4: command not found
claztec:hurry claztec$ virtualenv venv
Using base prefix '/Library/Frameworks/Python.framework/Versions/3.4'
New python executable in venv/bin/python3.4
Also creating executable in venv/bin/python
Installing setuptools, pip...done.
claztec:hurry claztec$
```

## python3와 mysql 연동

http://stackoverflow.com/questions/2952187/getting-error-loading-mysqldb-module-no-module-named-mysqldb-have-tried-pre
```
pip install MySQL-python
```
```
mysql_config must be on the path. On Mac, do

export PATH=$PATH:/usr/local/mysql/bin/
sudo pip install MySQL-python
```


python manage.py syncdb 에러 발생시.
http://www.curlybrace.com/words/2011/01/25/mac-os-mysql-python-1-2-3-importerror-library-not-loaded-libmysqlclient-16-dylib/

http://stackoverflow.com/questions/6389920/pydev-where-do-i-have-to-add-the-path-for-an-external-lib-usr-local-mysql-lib