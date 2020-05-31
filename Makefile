run:
	rm -rf manager
	cp -r sample-manager manager
	python3 main.py

build:
	rm -rf submission
	cp -r sample-manager manager
	docker build -t test-manager .
