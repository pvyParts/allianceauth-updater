git clone https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools.git
cd allianceauth-corp-tools
pwd
export DJANGO_SETTINGS_MODULE="tests.test_settings"
make setup
pip install -e .
make runtest
