### Linux性能优化
vmstat
```
  vmstat 2 5 | column -t  
  vmstat -s
```
### Wowza
Developer License (Expires in 180 days)  
EDEV4-Nz89f-77cG4-4xGz6-fDnAN-j4R46-8vEBGPwnGU3c  
License Owner  
hhi96274@iencm.com  
### Django
```
python3 -m venv ll_env
source ll_env/bin/activate
pip install django==1.8.4
django-admin startproject learning_log .
python manage.py migrate
python manage.py runserver 8000
python manage.py startapp learning_logs
python manage.py makemigrations learning_logs
python manage.py createsuperuser
python manage.py shell
    from learning_logs.models import Topic
    Topic.objects.all()
    topics = Topic.objects.all()
    for topic in topics:
        print(topic.id, topic)
    t = Topic.objects.get(id=1)
    t.text
    t.date_added
    t.entry_set.all()

making web pages with Django consists of three stages: defining URLs, writing
views, and writing templates.
URLs-->views-->templates
```
### sublime
```
{
	"color_scheme": "Packages/Color Scheme - Default/Monokai.sublime-color-scheme",
	"font_size": 14,
	"ignored_packages":
	[
	],
	"rulers":
	[
		80,
		100,
		120
	],
	"theme": "Default.sublime-theme",
	"word_wrap": true,
	"wrap_width": 100
}

{"anaconda_linting": false}

set ts=4
syntax on
```
### backup
1. nginx rtmp
	nginx-based media streaming server
	nginx-rtmp-module
2. resource monitor: resmon
3. performance monitor: perfmon
4. task manager: taskmgr/Ctrl+Shift+Esc
5. mstsc /v ip:port

### mount windows os disk to linux
```
sudo mount -t cifs -o username='Administrator',password='a' //192.168.1.102/tmp /home/trent/workspace/tmp/
sudo mount -t cifs -o username='Administrator',password='a' //192.168.1.100/data /home/trent/workspace/data/
```
### Delete file in 180 days
`find /home/boful/enzo/flowjs/ -type f -mtime +180 -exec rm -f {} \;`
### get pdf size
`pdfinfo teachercotrol.pdf | grep 'File size:' | awk '{print int($3/1024)}'`
### find replication
`cat log | cut -d ' ' -f 1 | sort | uniq -d`
### virtualenv
```
python3 -m venv turorial-env
pip search astronomy
pip install novas
pip install requests==2.6.0
pip install --upgrade requests
pip uninstall
pip show requests
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```