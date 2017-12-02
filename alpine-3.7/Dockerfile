FROM alpine:3.7

# Update the OS to current packages, install dependencies, clone repo
RUN  apk add --no-cache \
              git \
              bash \
              cmake \
              util-linux \
              scons \
              ninja \
              pkgconf \
              clang \
              gcc \
              g++ \
              protobuf \
              protobuf-dev \
              protobuf-c \
              protobuf-c-dev \
              openssl-dev \
              boost-dev \
  && git clone https://github.com/ripple/rippled.git /rippled \
  && git --version \
  && bash --version \
  && cmake --version \
  && lscpu --version \
  # && grep --version \
  && busybox \
  && scons --version \
  && ninja --version \
  && pkg-config --version \
  && gcc --version \
  && clang --version \
  && protoc --version

WORKDIR /rippled/Builds

CMD ["/bin/bash", "/rippled/Builds/build_all.sh"]
