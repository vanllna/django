# myweb_uwsgi.ini file
[uwsgi]

# Django-related settings

socket = 127.0.0.1:8000

# the base directory (full path)
chdir           = /home/wanghao/workspace/TestNud

# Django s wsgi file
module          = TestNud.wsgi

# process-related settings
# master
master          = true

# maximum number of worker processes
processes       = 10

# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true
virtualenv = /www/wwwroot/webtest/pro

logto = /tmp/mylog.log

