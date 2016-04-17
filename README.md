# django CMS: d120

This is an instance of django CMS used to build d120.de.

## Development Setup

A quick development setup is much simpler than the whole installation for production. Just do the following steps to get a local instance running:

```
git clone THIS_REPO
cd djangocms
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

## Important Notes on Settings

By default, the `settings.py` file is used which is suitable for a development setup. To have a proper deployment on production, one should use the `settings_production.py` file (which imports the default, overrides certain preferences, and reads secrets from `settings_secrets.py`). This means:
* pass the `--settings d120.settings_production` option to certain `manage.py` commands
* or do `export DJANGO_SETTINGS_MODULE=d120.settings_production` to set the environment variable before running multiple `manage.py` commands
* let the application server (e.g. uwsgi) set the environment variable (see example uwsgi file)

## Installation

* install dependencies (which you may find out later)
* create a user, e.g. named *django*
* clone the repository, e.g. `cd /srv`, `git clone THIS_REPO`
* create virtualenv, i.e. `cd djangocms`, `virtualenv -p python3 venv` (and maybe update pip)
* setup the database, e.g.:
    * `mysql -u root`
    * `create database djangocms;`
    * `grant all on djangocms.* to djangocms@localhost identified by DB_PASSWORD;`
    * `quit`
* create the file `d120/settings_secrets.py` (better restrict read access from others) and fill it with the secrets needed in `d120/settings_production.py`
* follow the necessary steps from the *Deploying Updates* section
* properly setup a wsgi application server like uwsgi and a webserver like Apache which should serve the static files
    * the file `uwsgi-djangocms.ini` contains an exemplary uwsgi configuration

## Deploying Updates

* go to project folder, e.g. `cd /srv/djangocms`
* maybe stop the application server, e.g. `systemctl stop uwsgi`
* update the project, i.e. `git pull`
* activate virtualenv, i.e. `source venv/bin/activate`
* `pip install --upgrade -r requirements.txt`
* `export DJANGO_SETTINGS_MODULE=d120.settings_production` for the following `manage.py` commands
* `./manage.py migrate`
* `./manage.py collectstatic --noinput`
* `chown -R django:django .`
* maybe start the application server, e.g. `systemctl start uwsgi`

## Updating the CMS

To install security or bugfix updates, it should be enough to follow the instructions from the *Deploying Updates* section.

When a new major version of django-cms becomes available, one might want to test this locally before adapting the `requirements.txt` (version is restricted there) and deploying the update on production.

The same holds true for the Django framework itself. Maybe it is a good idea to stick with LTS releases.
