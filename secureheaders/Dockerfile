FROM alpine:latest

LABEL org.owasp.url="https://www.owasp.org/index.php/OWASP_Secure_Headers_Project" \
  org.owasp.name="Owasp SecureHeaders Project" \
  org.owasp.description="Front-end from SecureHeaders Project" \
  org.owasp.version="v3.1.0"

ENV APPLICATION_DIRECTORY /opt/headers
ENV FLASK_APP ${APPLICATION_DIRECTORY}/web/webui.py

WORKDIR ${APPLICATION_DIRECTORY}

COPY . .

RUN apk add --no-cache py2-pip py-setuptools gcc make build-base python2-dev \
  && pip2 install --upgrade pip \
  && pip2 install -r requirements.txt

EXPOSE 5000

COPY docker/docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
