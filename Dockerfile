FROM python


WORKDIR /code

VOLUME /code

ENTRYPOINT [ "python" ]

EXPOSE 8000

RUN pip install uvicorn
RUN pip install fastapi
RUN pip install python-qbittorrent

CMD [ "./qbit.py" ]