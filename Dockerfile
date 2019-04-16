FROM python:3.6
ADD uuidSender.py /
ENV SOURCEVALUE X
ENV DESTINATION X
ENV WAITTIME X
RUN pip install --upgrade pip
RUN pip install requests
CMD python uuidSender.py $SOURCEVALUE $DESTINATION $WAITTIME
