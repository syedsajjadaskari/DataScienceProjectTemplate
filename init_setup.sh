echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8"
pip install virtualenv
python -m virtualenv venv
echo [$(date)]: "activate env"
venv/bin/activate
echo [$(date)]: "intalling dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"