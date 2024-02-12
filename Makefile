on:
	.\env_workoutapi\Scripts\activate

run:
	@uvicorn workout_api.main:app --reload

dk-down:
	docker-compose down

dk-run:
	docker-compose up -d

