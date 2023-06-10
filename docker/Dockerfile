FROM python
RUN apt-get update
RUN apt-get install -y cmake
RUN apt-get install -y libaec-dev
RUN apt install -y gfortran
RUN apt-get install -y cron
RUN git clone https://github.com/vercingetorix47/GRIB-read.git
WORKDIR /GRIB-read
RUN cd /GRIB-read
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir /eccodes ; mkdir /climatedata
RUN mkdir /installfiles ; cd /installfiles
RUN wget https://confluence.ecmwf.int/download/attachments/45757960/eccodes-2.30.0-Source.tar.gz
RUN tar -xzf  eccodes-2.30.0-Source.tar.gz
RUN mkdir /installfiles/build ; cd /installfiles/build
RUN cmake -DCMAKE_INSTALL_PREFIX=/eccodes ./eccodes-2.30.0-Source
RUN make
RUN ctest
RUN make install
RUN cd /installfiles ; rm -r /installfiles/*
RUN cd / ; rmdir installfiles
ENV ECCODES_DIR="/eccodes"
ENV TZ=America/Los_Angeles
RUN cd /GRIB-read
RUN chmod 755 getgrib
RUN crontab gribcron
CMD cron
