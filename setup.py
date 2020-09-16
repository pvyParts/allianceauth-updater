import os
from setuptools import find_packages, setup
from auth_updater import VERSION

install_requires = [
    'allianceauth>=2.7.5',
    'celery>=4.4.2,<5.0.0',
    'django>=2.2.16,<3.0.0',

]

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
