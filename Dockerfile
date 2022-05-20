FROM python:3.7-buster

RUN python3 -m pip install --upgrade pip

COPY ./ /home/appuser/cald/

WORKDIR /home/appuser/cald

RUN pip3 install -U .
RUN pip3 install -r requirements-dev.txt

CMD cald