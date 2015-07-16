# blood_db
A blood database portal

Getting started

1.Clone this project and setup a virtual environment
2.Install the requirements using pip
	pip install -r requirements.txt
3.Now sync your database 
	pyhton manage.py syncdb
4.Start the server using 
	python manage.py runserver
5.The directory structure is as follows

blood_db
|	
|__	api
│   ├── admin.py
│   ├── admin.pyc
│   ├── forms.py               //contains the DonorForm
│   ├── forms.pyc
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0001_initial.pyc
│   │   ├── __init__.py
│   │   └── __init__.pyc 
│   ├── models.py                    // donor model here
│   ├── models.pyc
│   ├── templates
│   │   └── api
│   │       ├── add.html           //contains the add donor  html file
│   │       ├── base.html          // contains the base template 
│   │       └── search.html         //contains the search page html file
│   ├── tests.py
│   ├── urls.py                   //urls here
│   ├── urls.pyc
│   ├── views.py                 // create views here
│   └── views.pyc
├── blood_db
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── settings.py                 // main settings file
│   ├── settings.pyc
│   ├── urls.py                     // main url file
│   ├── urls.pyc
│   ├── wsgi.py
│   └── wsgi.pyc
├── login
│   ├── admin.py
│   ├── admin.pyc
│   ├── forms.pyc 
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0001_initial.pyc
│   │   ├── 0002_auto_20150615_1306.py
│   │   ├── 0002_auto_20150615_1306.pyc
│   │   ├── 0003_delete_user.py
│   │   ├── 0003_delete_user.pyc
│   │   ├── 0004_donor.py
│   │   ├── 0004_donor.pyc
│   │   ├── __init__.py
│   │   └── __init__.pyc
│   ├── models.py
│   ├── models.pyc
│   ├── static
│   │   └── login
│   │       ├── style2.css
│   │       ├── style2.css~
│   │       ├── style.css                          // main css file 
│   │       └── style.css~
│   ├── templates
│   │   └── login
│   │       ├── base.html                          // login app base template
│   │       ├── home.html                          // main home 
│   │       └── login.html                         // 
│   ├── tests.py
│   ├── urls.py
│   ├── urls.pyc
│   ├── views.py
│   └── views.pyc
├── manage.py
├── README.md                                // You are here ;)
└── requirements.txt




Happy Coding