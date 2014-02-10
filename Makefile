MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) test test42cc
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) test person

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) loaddata fixtures/initial_data.json