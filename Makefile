activate:
	.\env_workoutapi\Scripts\activate

run:
	@uvicorn workout_api.main:app --reload