FROM phusion/baseimage

# add core and directories
RUN mkdir /MyMDB
WORKDIR /MyMDB
COPY requirements* /MyMDB/
COPY mymdb/ /MyMDB/mymdb
COPY core/ /MyMDB/core
COPY user/ /MyMDB/user
COPY templates/ /MyMDB/templates
COPY manage.py /MyMDB/manage.py
COPY scripts /MyMDB/scripts
RUN mkdir /var/log/mymdb/
RUN touch /var/log/mymdb/mymdb.log

# install packages
RUN apt-get -y update
RUN apt-get install -y \
    nginx \
    postgresql-client \
    python3 \
    python3-pip


# create virtualenv, install dependencies
RUN pip3 install virtualenv
RUN virtualenv /MyMDB/venv
RUN bash /MyMDB/scripts/pip_install.sh /MyMDB
RUN bash /MyMDB/scripts/collect_static.sh /MyMDB

# configure nginx 
COPY nginx/mymdb.conf /etc/nginx/sites-available/mymdb.conf
RUN rm /etc/ngenx/sites-enabled/*
RUN ln -s /etc/nginx/sites-available/mymdb.conf /etc/nginx/sites-enabled/mymdb.conf

COPY runit/nginx /etc/service/nginx
RUN chmod +x /etc/service/nginx/run

# add uwsgi
COPY uwsgi/mymdb.ini /etc/uwsgi/apps-enabled/mymdb.ini
RUN mkdir -p /var/log/uwsgi/
RUN touch /var/log/uwsgi/mymdb.log
RUN chown www-data /var/log/uwsgi/mymdb.log
RUN chown www-data /var/log/mymdb/mymdb.log

COPY runit/uwsgi /etc/service/uwsgi
RUN chmod +x /etc/service/uwsgi/run

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* tmp/* /var/tmp/*
EXPOSE 80


