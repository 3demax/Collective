# This is a script for glitch.me

# First, setup $SUPERUSERNAME, $SUPERUSER_EMAIL, $SUPERUSER_PASSWORD environment variables
# For glitch, this can be done in .env (see .env.example)

# Uncomment to run
# cat <<EOF | python manage.py shell
# from django.contrib.auth import get_user_model
# User = get_user_model()  # get the currently active user model,
# User.objects.filter(username='admin').exists() or \
#     User.objects.create_superuser($SUPERUSERNAME, $SUPERUSER_EMAIL, $SUPERUSER_PASSWORD)
# EOF

# Main part, that updates the database and runs the server
python2 manage.py migrate
python2 manage.py runserver $PORT