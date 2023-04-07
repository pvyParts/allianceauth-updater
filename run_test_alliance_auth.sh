git clone https://gitlab.com/allianceauth/allianceauth.git
cd allianceauth
pwd
export DJANGO_SETTINGS_MODULE="tests.settings_all"
make setup
pip install -e ".[test]"
make test
