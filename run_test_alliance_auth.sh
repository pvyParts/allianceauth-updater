set -e
git clone https://gitlab.com/allianceauth/allianceauth.git
cd allianceauth
pwd
export DJANGO_SETTINGS_MODULE="../tests.aa.mysql"
pip install --upgrade pip
pip install coverage wheel
pip install -e ".[test]"
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
