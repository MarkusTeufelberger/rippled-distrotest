FROM fedora:rawhide

# Update the OS to current packages, install dependencies, clone repo
RUN  dnf -y upgrade --refresh \
  && dnf -y install \
  git \
  cmake \
  make \
  ninja-build \
  clang \
  libstdc++-devel \
  libstdc++-static \
  libasan \
  libasan-static \
  libtsan \
  libtsan-static \
  pkgconfig \
  protobuf-compiler \
  protobuf-devel \
  protobuf-static \
  openssl-devel \
  openssl-libs \
  openssl-static \
  boost-devel \
  boost-static \
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
  && doxygen --version \
  && ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /rippled/Builds

CMD ["/bin/bash", "/rippled/Builds/build_all.sh"]
