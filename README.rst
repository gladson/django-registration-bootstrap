=============================
Django Registration Bootstrap
=============================
Simple sample using bootstrap from twitter in forms of Django
-------------------------------------------------------------

Just update to Bootstrap from Twitter version 2.3.1

Just update to Django version 1.6

http://twitter.github.com/bootstrap

To clone, just syncdb and do runserver:

	python manage.py syncdb

	Creating tables ...
	Creating table django_admin_log
	Creating table auth_permission
	Creating table auth_group_permissions
	Creating table auth_group
	Creating table auth_user_groups
	Creating table auth_user_user_permissions
	Creating table auth_user
	Creating table django_content_type
	Creating table django_session

	You just installed Django's auth system, which means you don't have any superusers defined.
	Would you like to create one now? (yes/no): yes
	Username (leave blank to use 'gladson'): admin
	Email address: admin@localhost.com
	Password:
	Password (again):
	Superuser created successfully.
	Installing custom SQL ...
	Installing indexes ...
	Installed 0 object(s) from 0 fixture(s)

    python manage.py runserver 8000

	username: admin
	password: admin