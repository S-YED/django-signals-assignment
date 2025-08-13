# Django Signals & Python Rectangle Class - Assignment

This repository contains runnable code for the Django Signals and Python Custom Class questions.



## **How to Run**

1. **Clone the repo**
```bash
git clone https://github.com/s-yed/django-signals-assignment.git
cd django-signals-assignment
```
2. **Create virtual environment & install dependencies**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. **Run migrations (Django needs DB setup)**
```bash
python manage.py migrate
```
4. **Run each question in Django shell**
```bash
python manage.py shell < signals_demo/sync_signal.py
python manage.py shell < signals_demo/same_thread.py
python manage.py shell < signals_demo/same_transaction.py

```
5. **Run Rectangle class**
```bash
python rectangle_demo/rectangle.py
```

## **FILES** 

* Q1 - Synchronous execution proof → signals_demo/q1_sync_signal.py

* Q2 - Same thread proof → signals_demo/q2_same_thread.py

* Q3 - Same DB transaction proof → signals_demo/q3_same_transaction.py

* Rectangle- Iterable class → rectangle_demo/rectangle.py

**Requirements**
```txt
Django==3.2
``` 

## **AUTHOR**
**Syed khaja Moinuddin**
