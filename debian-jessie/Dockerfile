FROM debian:jessie

# Update the OS to current packages, install dependencies, clone repo
RUN  apt-get update \
  && apt-get -y upgrade \
  && apt-get -y install \
  git \
  cmake \
  ninja-build \
  gcc \
  g++ \
  clang \
  pkg-config \
  protobuf-compiler \
  libprotobuf-dev \
  libssl-dev \
  libboost-all-dev \
  doxygen \
  && git clone https://github.com/ripple/rippled.git /rippled \
  && git --version \
  && bash --version \
  && cmake --version \
  && lscpu --version \
  && grep --version \
  && ninja --version \
  && pkg-config --version \
  && gcc --version \
  && clang --version \
  && protoc --version \
  && doxygen --version

WORKDIR /rippled/Builds

CMD ["/bin/bash", "/rippled/Builds/build_all.sh"]
