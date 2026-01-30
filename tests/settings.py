SECRET_KEY = "test"
DEBUG = True

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
    "djangotenberg",
]

ROOT_URLCONF = "tests.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

GOTENBERG_CONFIG = {
    "GOTENBERG_URL": "http://localhost:3001",
}