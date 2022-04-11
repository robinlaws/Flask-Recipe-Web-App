import sys
sys.path.insert(0, '/var/www/egg2z')

activate_this = '/home/ubuntu/.local/share/virtualenvs/egg2z-GZQYUj1a/bin/activate'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

    from application import app1 as application



