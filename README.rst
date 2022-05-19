python3 -m venv flask
pip3 install <packages>

source bin/activate

coverage run -m pytest > output

coverage html #generage htmlcov/index.html
