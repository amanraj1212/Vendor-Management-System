# Vendor-Management-System
Steps:

1) Ensure that Django version==4.1.5 and django_rest_framework version==3.14.0 is installed in your system
        if not installed then run command in your terminal: 
                 --> pip install django==4.1.5
                 --> pip install djangorestframework==3.14.0

2) clone the repo in your system by following command in your git bash:
  --> git clone https://github.com/amanraj1212/Vendor-Management-System.git

3) Ensure that INSTALLED_APPS = [] section contains 'vendor','rest_framework' 

4) Also makesure that ALLOWED_HOSTS = ['*']

5) Type the following command to reach backend folder:
       --> cd backend

6) Type the following command in your terminal
   --> python manage.py runserver

7) The APIs url are in backend/backend/urls.py which you can verify by typing the url in your localhost browser. The valid urls are given below:

A) admin/
B) api/vendors/ [name='vendor-list-create']
C) api/vendors/<int:pk>/ [name='vendor-detail']
D) api/purchase_orders/ [name='purchase-order-list-create']
E) api/purchase_orders/<int:pk>/ [name='purchase-order-detail']
F) api/vendors/<int:pk>/performance/ [name='vendor-performance']
G) api/purchase_orders/<int:pk>/acknowledge/ [name='acknowledge-purchase-order']





     


