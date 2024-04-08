# create a django project

    - `django-admin startproject watchmate`

# create a new app inside the project

    - `python3 manage.py startapp watchlist`

    - `pip install djangorestframework` without underscore !important

### add `rest_framework` to INSTALLED_APPS inside settings.py

### create api folder inside the app and inside:

    - create a views.py, serializers.py and urls.py folder.

### create the following:

    - model called `Movies`
    - a serializer -> user `rest_framework.serializers.Serialzer` as parent class.
    - view function called `movie_list`
    - set up routes in the urls.py file.

### run

    - `python manage.py makemigrations/migrate`

### run the server!

### Inside Serializer

    - define create and update functions to make POST and PUT work.

### POST create

    - `return Movie.objects.create(**validated_data)`
