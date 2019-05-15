FROM opensuse/leap:42.3

# Update the OS to current packages, install dependencies, clone repo
RUN  zypper --non-interactive update \
  && zypper --non-interactive install \
  git \
  cmake \
  gcc5 \
  gcc5-c++ \
  llvm-clang \
  ninja \
  pkg-config \
  protobuf-devel \
  protobuf-c \
  boost_1_61-devel \
  libopenssl-devel \
  doxygen \
  && git clone https://github.com/ripple/rippled.git /rippled \
  && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 99 \
  && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 99 \
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
