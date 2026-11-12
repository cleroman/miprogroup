#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# ON AJOUTE CETTE LIGNE POUR IMPORTER TES DONNEES
python manage.py loaddata data.json || echo "Donnees deja importees"
