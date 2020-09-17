import os
from setuptools import find_packages, setup
from auth_updater import VERSION

install_requires = [
    'allianceauth==2.8.0a1',
    'celery==4.4.7',
    'django==2.2.16',  #3.0.0 not working with auth
    'mysqlclient==2.0.1',
    'dnspython==2.0.0',
    'passlib==1.7.2',
    'requests==2.24.0',
    'bcrypt==3.2.0',
    'python-slugify==4.0.0',
    'requests-oauthlib==1.3.0',
    'semantic_version==2.8,5',
    'packaging==20.4',

    'redis==3.5.3',
    'celery_once==3.0.1',

    'django-bootstrap-form==3.4',
    'django-registration==2.5.2', # incompat 3.0
    'django-sortedm2m==3.0.2',
    'django-redis-cache==2.1.1',
    'django-celery-beat==1.6.0', # incompat 2.0

    'django-esi==2.0.0',
    'bravado==10.6.2']

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
