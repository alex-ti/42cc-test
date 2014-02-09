MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) test test42cc

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) syncdb --noinput
