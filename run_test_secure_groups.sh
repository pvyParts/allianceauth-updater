set -e
cd auth_updater
git clone https://github.com/Solar-Helix-Independent-Transport/allianceauth-secure-groups.git secgroups
cd secgroups
pwd
export DJANGO_SETTINGS_MODULE="auth_updater.tests_sg_mysql"
pip install --upgrade pip
pip install coverage wheel 
pip install -e .
pip install -r ../../requirements.txt --no-deps
echo "****************************************"
echo "********** Current Versions! ***********"
echo "****************************************"
pip freeze
echo "****************************************"
echo "*****   Running SecGroup Tests!   ******"
echo "****************************************"
coverage run runtests.py -v 2 --debug-mode
coverage report -m
