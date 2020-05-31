# -*- coding:utf-8 -*-

import sys
import flask

app = flask.Flask(__name__, template_folder='./templates', static_folder='./static')


@app.route('/')
def index():
    return "域名出售，联系mengpanfei@qq.com"


# 启动1   $PYTHON3 flask_app.py 80 debug
if __name__ == "__main__":
    port = sys.argv[1]
    _debug= len(sys.argv)>=3 and sys.argv[2]=="debug"
    app.run(host="0.0.0.0", port=port, debug=_debug)
    
