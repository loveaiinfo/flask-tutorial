# flask-tutorial
simple blog based on flask

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
flask --app flaskr run --debug

flask --app flaskr init-db

pip install -e .

pytest

coverage run -m pytest
coverage report
coverage html
```

## Deploy to Production

__Build and Install__

```bash
$ pip install build
$ python -m build --wheel
```

__Run with a Production Server__
```bash
pip install waitress
waitress-serve --call 'flaskr:create_app'

gunicorn -w 4 'flaskr:create_app()'
gunicorn --bind 0.0.0.0:8000 -w 4 --worker-class=gevent 'flaskr:create_app()'
```
