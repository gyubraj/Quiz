# Quiz APP

## Follow these steps

1. Create Virtual Enviroment and Activate it

2. `pip install -r requirements.txt`
3. `python manage.py makemigrations && manage.py migrate`
4. `python manage.py loaddata testdata.json`
5. `python manage.py runserver`

### To obtain English Quiz
_127.0.0.1:8000/api/quiz_

### To obtain Nepali Quiz
_127.0.0.1:8000/api/quiz?language=NEP_

### Make sure to insert data before accessing it otherwise Error will be thrown
#### Insert at least one  Data for each level 

### To Add New Data goto
`127.0.0.1:8000/quiz/`
