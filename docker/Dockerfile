FROM python
RUN apt-get update
RUN apt-get install -y cmake
RUN apt-get install -y libaec-dev
RUN apt install -y gfortran
RUN git clone https://github.com/vercingetorix47/GRIB-read.git
WORKDIR /GRIB-read
RUN cd /GRIB-read
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN wget https://confluence.ecmwf.int/download/attachments/45757960/eccodes-2.30.0-Source.tar.gz
RUN tar -xzf  eccodes-2.30.0-Source.tar.gz
RUN mkdir build ; cd build
RUN cmake -DCMAKE_INSTALL_PREFIX=/GRIB-read/eccodes ./eccodes-2.30.0-Source
RUN make
RUN ctest
RUN make install
ENV ECCODES_DIR="/GRIB-read/eccodes"
RUN cd /GRIB-read
CMD ["python3", "'Grib read main.py'"]
