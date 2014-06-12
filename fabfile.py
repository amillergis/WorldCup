from fabric.api import local,lcd

def prepare_deployment(branch_name):
	local('python manage.py test worldcuppool')
	local('git add -p && git commit')
	local('git checkout master && git merge ' + branch_name)

def deploy():
	with lcd('path/to/my/prod/area/'):
		local('git pull /my/path/to/dev/area/')
		local('python manage.py migrate worldcuppool')
		local('python manage.py test worldcuppool')
		local('/my/command/to/restart/webserver')