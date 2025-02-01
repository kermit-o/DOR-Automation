#!/bin/bash

touch /workspaces/DOR-Automation/DORProject/app/__init__.py


export PYTHONPATH=/workspaces/DOR-Automation/DORProject

#export FLASK_APP=DORProject.app:create_app
export FLASK_ENV=development  # Para recarga automática
cd DORProject
flask run
