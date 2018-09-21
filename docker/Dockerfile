FROM python:2.7.15-alpine3.8
MAINTAINER Abhay Bhargav
RUN pip install bandit
RUN mkdir -p /results/ && mkdir -p /src/ && mkdir -p /runexec/
ADD run_bandit.sh /runexec/
RUN chmod +x /runexec/run_bandit.sh
CMD ["/runexec/run_bandit.sh"]