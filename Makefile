VENV_NAME=env_workout_api
ACTIVATE=$(VENV_NAME)\Scripts\activate
DEACTIVATE=$(VENV_NAME)\Scripts\deactivate
DOCKER_APP=C:\Program Files\Docker\Docker\Docker Desktop.exe

create:
	 @python -m venv $(VENV_NAME)
	 $(ACTIVATE) && pip install -r requirements.txt
	 @echo	$(VENV_NAME) criado e ativado.

delete:
	@cmd /C "rmdir /s /q $(VENV_NAME)"
	@echo	$(VENV_NAME) deletado.


run:
	 @cmd /C $(ACTIVATE) && uvicorn $(VENV_NAME).main:app --reload

dk-down:
	docker-compose down

dk-run:
	docker-compose up -d

# Regra para iniciar o Docker Desktop
dk-start:
	@echo	Iniciando o Docker Desktop...
	$(DOCKER_APP) --quiet


create-migrations:
	@cmd /C "set PYTHONPATH=%cd% && alembic revision --autogenerate -m $(d)"

run-migrations:
	@cmd /C "set PYTHONPATH=%cd% && alembic upgrade head"

