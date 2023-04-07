git clone https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools.git
cd allianceauth-corp-tools
pip install --upgrade pip
pip install coverage
pip install ../requirements.txt
pip freeze
coverage run runtests.py
coverage report -m