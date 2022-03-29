if [[ !  -f "venv/" ]]
then
   virtualenv venv
   pip install -r requirements.txt
  
fi

source venv/bin/activate
python main.py
