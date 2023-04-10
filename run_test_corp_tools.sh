set -e
pip install -e .
cd auth_updater
git clone https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools.git corptools
cd corptools
pwd
export DJANGO_SETTINGS_MODULE="auth_updater.tests_ct_mysql"
pip install --upgrade pip
pip install coverage wheel
pip install -e .
pip install -r ../../requirements.txt --no-deps
echo "****************************************"
echo "********** Current Versions! ***********"
echo "****************************************"
pip freeze
echo "****************************************"
echo "*******   Running Core Tests!   ********"
echo "****************************************"
coverage run runtests.py -v 2 --debug-mode
coverage report -m
