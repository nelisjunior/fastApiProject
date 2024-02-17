# Create virtual environment and install requirements

python -m venv env_workout_api
env_workout_api\Scripts\activate
pip install -r requirements.txt

# Activate virtual environment
env_workout_api\Scripts\activate

# Run the application
uvicorn "workout_api.main:app" --reload

# Docker commands
docker-compose down
docker-compose up -d
"C:\Program Files\Docker\Docker\Docker Desktop.exe" --quiet

# Alembic commands for migrations
$env:PYTHONPATH += ";$PWD"; alembic revision --autogenerate -m $args[0]
$env:PYTHONPATH += ";$PWD"; alembic upgrade head
