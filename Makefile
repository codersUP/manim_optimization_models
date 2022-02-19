.DEFAULT_GOAL := run
.PHONY: run

install:
	sudo apt update
	sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
	sudo apt install python3-pip
	pip3 install manim
	python -m pip install -r requirements.txt

run:
	streamlit run ui/main.py
