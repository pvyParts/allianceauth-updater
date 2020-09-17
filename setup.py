import os
from setuptools import find_packages, setup
from auth_updater import VERSION

install_requires = [
    'allianceauth>=2.7.5',
    'celery>=4.4.2,<5.0.0',
    'django>=2.2.16,<3.0.0',  #3.0.0 not working with auth
    'mysqlclient',
    'dnspython',
    'passlib',
    'requests>=2.9.1,<3.0.0',
    'bcrypt',
    'python-slugify>=1.2',
    'requests-oauthlib',
    'semantic_version',
    'packaging>=20.1,<21',

    'redis>=3.3.1,<4.0.0',
    'celery>=4.3.0,<5.0.0,!=4.4.4',  # 4.4.4 is missing a dependency
    'celery_once',

    'django-bootstrap-form',
    'django-registration==2.4',
    'django-sortedm2m',
    'django-redis-cache>=2.1.0,<3.0.0',
    'django-celery-beat>=1.1.1,<3.0.0',

    'openfire-restapi',
    'sleekxmpp',
    'pydiscourse',

    'django-esi>=2.0.0,<3.0']

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='allianceauth-wiki-js',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license='MIT',
    description='Alliance Auth Dependency update helper',
    long_description=long_description,
    url="https://github.com/pvyParts/allianceauth-wiki-js",
    long_description_content_type='text/markdown',
    author='AaronKable',
    author_email='aaronkable@gmail.com',
)

https://discordapp.com/api/webhooks/566902300728360960/mjrhz4Rmj4PScQek_rcX2TWA5NJCQotNomkhRzeIfPcWuq1rej-HYMi54CqS91UNR1ve
