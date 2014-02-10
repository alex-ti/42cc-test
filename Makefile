MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) person

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) syncdb --noinput

syncall:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) syncdb --migrate --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test42cc.settings $(MANAGE) loaddata fixtures/initial_data.json

clean:
	find -type f -name "*.pyc" -delete