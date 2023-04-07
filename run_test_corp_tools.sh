git clone https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools.git
cd allianceauth-corp-tools
pwd
export DJANGO_SETTINGS_MODULE="tests.test_settings"
pip install --upgrade pip
pip install coverage
pip install -e .
pip install -r ../requirements.txt
pip freeze
coverage run runtests.py
coverage report -m