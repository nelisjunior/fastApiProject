activate:
	.\env_workoutapi\Scripts\activate

run:
	@uvicorn workout_api.main:app --reload

dk-down:
	docker-compose down

run-docker:
	docker-compose up -d

