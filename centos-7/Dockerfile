FROM centos:7

# Update the OS to current packages, install dependencies, clone repo
RUN  yum -y install \
          epel-release \
  && yum -y upgrade \
  && yum -y install \
          git \
          ninja-build \
          cmake \
          gcc \
          gcc-c++ \
          clang \
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
  && git clone https://github.com/ripple/rippled.git /rippled \
  && ln /usr/bin/ninja-build /usr/bin/ninja \
  && git --version \
  && bash --version \
  && cmake --version \
  && lscpu --version \
  && grep --version \
  && ninja --version \
  && pkg-config --version \
  && gcc --version \
  && clang --version \
  && protoc --version

WORKDIR /rippled/Builds

CMD ["/bin/bash", "/rippled/Builds/build_all.sh"]
