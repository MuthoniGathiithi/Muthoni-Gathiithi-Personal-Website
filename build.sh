#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Make migrations
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

# Create superuser if not exists
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Collect static files
python manage.py collectstatic --no-input
