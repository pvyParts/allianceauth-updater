set -e
pip install -e .
cd auth_updater
git clone //gitlab.com/allianceauth/allianceauth.git
cd allianceauth
pwd
export DJANGO_SETTINGS_MODULE="auth_updater.tests_aa_mysql"
pip install --upgrade pip
pip install coverage wheel
pip install -e ".[test]"
pip install -r ../../requirements.txt --no-deps
echo "****************************************"
echo "********** Current Versions! ***********"
echo "****************************************"
pip freeze
echo "****************************************"
echo "**********   Running Tests!   **********"
echo "****************************************"
coverage run runtests.py -v 2 --debug-mode
coverage report -m
