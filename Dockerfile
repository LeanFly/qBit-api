FROM python


WORKDIR /code

ENTRYPOINT [ "python" ]

EXPOSE 8000

RUN pip install uvicorn
RUN pip install fastapi
RUN pip install python-qbittorrent

RUN curl -O https://raw.githubusercontent.com/LeanFly/qBit-api/main/qbit.py

CMD [ "./qbit.py" ]

