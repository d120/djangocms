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
cd d120 && ../manage.py compilemessages && cd ..
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

Note that some of the required Python packages have other dependencies, e.g. to C libraries which one can install using the distribution's package manager. Which exactly can differ but starting a web search when pip install shows an error typically gives good results.

## Important Notes on Settings

By default, the `settings.py` file is used which is suitable for a development setup. To have a proper deployment on production, one should use the `settings_production.py` file (which imports the default, overrides certain preferences, and reads secrets from `settings_secrets.py`). This means:
* pass the `--settings d120.settings_production` option to certain `manage.py` commands
* or do `export DJANGO_SETTINGS_MODULE=d120.settings_production` to set the environment variable before running multiple `manage.py` commands
* let the application server (e.g. uwsgi) set the environment variable (see example uwsgi file)

## Installation

* install dependencies (which you may find out later)
* create a user, e.g. named *djangocms*
* clone the repository, e.g. `cd /srv`, `git clone THIS_REPO`
* create virtualenv, i.e. `cd djangocms`, `virtualenv -p python3 venv` (and maybe update pip and setuptools)
* setup the database, e.g.:
    * `mysql -u root`
    * `create database djangocms;`
    * `grant all on djangocms.* to djangocms@localhost identified by DB_PASSWORD;`
    * `quit`
* create the file `d120/settings_secrets.py` (copy from `d120/settings_secrets.py.sample`) and fill it with the necessary secrets (it is a good advice to restrict read permissions from others)
* make all the files belong to the proper user, e.g. `chown -R djangocms:djangocms .`
* run the update script once: `sudo -u djangocms script/update --prod`
* properly setup a wsgi application server like uwsgi and a webserver like Apache which should serve the static files
    * the file `uwsgi-djangocms.ini` contains an exemplary uwsgi configuration

## Updating from this Repository

All necessary steps to update from this repository can be found in `script/update`. Just go into the project folder and run the script.

* for a local installation, this would be `script/update`
* for a production installation owned by user *djangocms*, this would be `sudo -u djangocms script/update --prod`

Since our `requirements.txt` does not pin versions of additional packages, it might happen that a third party package receives an update which breaks compatibility. In this case, have a look on the output of the script, roll back the affected package and/or investigate what is going on.

## Updating django CMS, Django, and additional packages

To install security or bugfix updates, it should be enough to follow the instructions from above, due to the loose version pinning in `requirements.txt`. This is done to avoid keeping track of releases of all the installed packages. Pinning them would lead to a poorly updated installation.

However, major updates from additional packages can break compatibility, see notes above for this. If it seems necessary to pin the version of an additional package, make this a temporary solution and add a comment in `requirements.txt` explaining the reason.

The version of the django-cms package itself is restricted to a major release, so only compatible updates are installed without touching the `requirements.txt`. When a new major version becomes available, one might want to test this locally before changing the restriction and deploying the update on production. The official django CMS documentation should include important information in the release notes section!

The same holds true for the Django framework. Maybe it is a good idea to stick with LTS releases.
