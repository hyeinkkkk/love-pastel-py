from app import app


session_opts = {
    'session.type': 'ext:memcached',
    'session.url': '127.0.0.1:11211',
    'session.data_dir': './cache',
}



if __name__ == '__main__':

    app.debug = True
    app.run(host='0.0.0.0')
