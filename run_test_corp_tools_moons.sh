set -e
cd auth_updater
git clone https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools-moons.git moons
cd moons
pwd
export DJANGO_SETTINGS_MODULE="auth_updater.tests_ct_moons_mysql"
pip install -e .
pip install -r ../../requirements.txt --no-deps
echo "****************************************"
echo "********** Current Versions! ***********"
echo "****************************************"
pip freeze
echo "****************************************"
echo "******   Running Moons Tests!   ********"
echo "****************************************"
coverage run runtests.py -v 2 --debug-mode
coverage report -m
