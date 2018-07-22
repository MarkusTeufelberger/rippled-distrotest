FROM opensuse/leap:15

# Update the OS to current packages, install dependencies, clone repo
RUN  zypper --non-interactive update \
  && zypper --non-interactive install \
  git \
  python \
  cmake \
  gcc \
  gcc-c++ \
  clang \
  ninja \
  pkg-config \
  protobuf-devel \
  protobuf-c \
  libboost_headers1_66_0-devel \
  libboost_container1_66_0-devel \
  libboost_coroutine1_66_0-devel \
  libboost_filesystem1_66_0-devel \
  libboost_program_options1_66_0-devel \
  libboost_regex1_66_0-devel \
  libboost_serialization1_66_0-devel \
  libboost_thread1_66_0-devel \
  libopenssl-devel \
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
  && protoc --version

WORKDIR /rippled/Builds

CMD ["/bin/bash", "/rippled/Builds/build_all.sh"]
