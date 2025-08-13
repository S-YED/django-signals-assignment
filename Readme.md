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
python manage.py shell < signalsdemo/sync_signal.py
python manage.py shell < signalsdemo/same_thread.py
python manage.py shell < signalsdemo/same_transaction.py

```
5. **Run Rectangle class**
```bash
python rectangledemo/rectangle.py
```

## **FILES** 

* Q1 - Synchronous execution proof → signalsdemo/sync_signal.py

Answer - By default, Django signals are synchronous. When a signal is sent (for example post_save), Django immediately calls each connected receiver in order, and the original code does not continue until all receivers finish. If a receiver is slow, the request or command that triggered it will also be slow.

* Q2 - Same thread proof → signalsdemo/same_thread.py

Answer - Yes, by default a signal receiver runs in the same thread that sent the signal. This matters because any heavy work in the receiver will block that same thread.

* Q3 - Same DB transaction proof → signalsdemo/same_transaction.py

Answer -

Signal receivers execute in the same database connection and transactional context as the caller.

If the caller is inside transaction.atomic(), then the receiver’s database writes are part of that same transaction. A rollback will undo both.

If you are not inside an atomic block (default autocommit), each query commits on its own. There is no larger transaction to “share,” but the receiver still runs inline on the same connection.

If you need the receiver to act only after the outer transaction successfully commits, use transaction.on_commit(...).

* Rectangle- Iterable class → rectangledemo/rectangle.py

**Requirements**
```txt
Django==3.2
``` 

## **AUTHOR**
**Syed khaja Moinuddin**
