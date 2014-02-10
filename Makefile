test:
	python manage.py test test42cc
	python manage.py test person

syncdb:
	python manage.py syncdb --noinput
	python manage.py migrate person
	python manage.py loaddata fixtures/initial_data.json

run:
	python manage.py runserver