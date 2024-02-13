on:
	.\env_workoutapi\Scripts\activate
off:
	.\env_workoutapi\Scripts\deactivate

run:
	@uvicorn workout_api.main:app --reload

dk-down:
	docker-compose down

dk-run:
	docker-compose up -d

create-migrations:
	@set	PYTHONPATH=%PYTHONPATH%;%cd% && alembic revision --autogenerate -m $(d)

run-migrations:
	@set	PYTHONPATH=%PYTHONPATH%;%cd% && alembic upgrade head