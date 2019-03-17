FROM opensuse/tumbleweed

# Update the OS to current packages, install dependencies, clone repo
RUN  zypper --non-interactive update \
  && zypper --non-interactive install \
  git \
  python \
  cmake \
  gcc \
  clang \
  ninja \
  libasan4 \
  libtsan0 \
  pkg-config \
  protobuf-devel \
  protobuf-c \
  libboost_atomic1_69_0-devel \
  libboost_headers1_69_0-devel \
  libboost_container1_69_0-devel \
  libboost_coroutine1_69_0-devel \
  libboost_filesystem1_69_0-devel \
  libboost_program_options1_69_0-devel \
  libboost_regex1_69_0-devel \
  libboost_serialization1_69_0-devel \
  libboost_thread1_69_0-devel \
  libopenssl-devel \
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
