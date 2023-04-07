git clone https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools.git
cd allianceauth-corp-tools
pwd
export DJANGO_SETTINGS_MODULE="tests.test_settings"
	pip install --upgrade pip
	pip install coverage
pip install -e .
pip install -r ../requirements.txt --no-deps
echo "****************************************"
echo "********** Current Versions! ***********"
echo "****************************************"
pip freeze
echo "****************************************"
echo "**********   Running Tests!   **********"
echo "****************************************"
coverage run runtests.py -v 2 --debug-mode
coverage report -m
