run:
	python3 run.py

install:
	pip3 install --no-cache-dir -r requirements.txt

run-docker:
	docker compose up -d --build

remove-docker:
	docker compose down