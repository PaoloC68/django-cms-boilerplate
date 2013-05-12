django-cms-boiler-plate
=======================

Yet another django boiler plate, specialized for django cms [1] projects.

Initial setup
-------------

1. Clone this repository

        git clone https://github.com/ygneo/django-cms-boilerplate.git <your-project-name>

1. Install requirements

        pip install -r pip-requirements.txt

1. Edit settings.py
   - Set the languages you want to have avaliable, and the default one, in LANGUAGES and DEFAULT_LANUAGE settings.
   - By default, sqlite3 db backend is used. You can change DATABASES setting to fit your needs.
   - Set your TIME_ZONE and your LANGUAGE_CODE.
   - If you're not going to use i18n and/or l10n, you can set USE_I8N and/ot USER_L10N to false.
   - Set your media root absolute path, where the user-uploaded files will be saved.
   - By default, STATIC_ROOT is set to 'static/' directory, relative to settings.py path. Change it if you need it.
   - Change SECRET_KEY to something unique, like you. ;-)
   - Django CMS's templates will be loaded by default from 'templates/' directory, relative to settings.py path. Change TEMPLATES if you want something different.
   - Only one sample CMS template is set in CMS_TEMPLATES setting. Add yours.
   - Three sample django cms placeholders are configured. Feel free to change them.
   - A default configuration for logging is made and ready to be modified in LOGGING setting.

1. Create yout configured database, and run manage commands to create tables and apply migrations

        ./manage.py syncdb
        ./manage.py migrate

1. Now you should be able to run the development server.

        ./manage.py runserver

Batteries included
------------------

 - Django CMS 2.4.1 and its default cms plugins and requirements.
 - Python Image Library.
 -

Fabric taks
-----------


[1] https://www.django-cms.org/en/
