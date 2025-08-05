from setuptools import setup, find_packages

setup(
    name="personal-website",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Django==4.2.7',
        'psycopg2-binary==2.9.9',
        'dj-database-url==2.1.0',
        'whitenoise==6.6.0',
        'Pillow>=10.0.0,<11.0.0',  # Compatible with Python 3.13
        'gunicorn==21.2.0',
        'python-dotenv==1.0.0',
    ],
)
