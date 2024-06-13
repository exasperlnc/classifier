## Setup Instructions

* $ python3 -m venv .env (setup virtual python environment)
* activate virtual environment with source .env/bin/activate (deactivate with $ deactivate OR $ source .env/bin/deactivate if $ deactivate doesn't work)
* $ which python => checks if the virtual environment is on (correct return looks like: /home/<user>/YOUR-DIRECTORY-NAME/.env/bin/python)
* $ pip install "transformers[sentencepiece]"
* $ pip3 install torch torchvision
* $ python3 main.py (run the files)