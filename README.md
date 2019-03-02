# Froney Backend (Python 3)

> Django backend for Froney App

# [Docker](https://hub.docker.com/r/ibrahimawad/froney_backend)
```
docker container run -p 80:80 ibrahimawad/froney_backend
```
Open your browser [http://localhost](http://localhost)

## Getting Started (windows)
### Development - [Github](https://github.com/ibrahimawad/froney_backend)

#### `Setup Environment and Activate`

```
git clone https://github.com/ibrahimawadhamid/froney_backend.git
cd froney_backend
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
```

#### `Install Prerequisites`

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json
```

#### `Start Server`

```
python manage.py runserver
```

#### `Login to Admin`

```
User: admin
Pass: admin
```

## License

[MIT](https://github.com/ibrahimawadhamid/froney_backend/blob/master/LICENSE)
