test:
	python manage.py test test42cc
	python manage.py test person

run:
	python manage.py runserver

syncdb:
	python manage.py syncdb --noinput

syncall:
	python manage.py loaddata fixtures/initial_data.json
	python manage.py syncdb --migrate --noinput