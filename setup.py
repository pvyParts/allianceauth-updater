import os
from setuptools import find_packages, setup
from auth_updater import __VERSION__

install_requires = [
    #locked 
    'django<3.0.0',  #3.0.0 not working with auth
    'django-celery-beat<2.0.0', # incompat 2.0
    'django-registration<3.0.0', # incompat 3.0

    #unlocked
    'celery',
    'gunicorn',
    'mysqlclient',
    'dnspython',
    'passlib',
    'requests',
    'bcrypt',
    'python-slugify',
    'requests-oauthlib',
    'semantic_version',
    'packaging',
    'redis',
    'celery_once',
    'django-bootstrap-form',
    'django-sortedm2m',
    'django-redis-cache',
    'django-esi',
    'bravado']

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='allianceauth-updater',
    version=__VERSION__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license='MIT',
    description='Alliance Auth Dependency update helper',
    long_description=long_description,
    url="https://github.com/pvyParts/allianceauth-updater",
    long_description_content_type='text/markdown',
    author='AaronKable',
    author_email='aaronkable@gmail.com',
)
