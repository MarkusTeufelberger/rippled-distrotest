FROM opensuse:tumbleweed

# Update the OS to current packages, install dependencies, clone repo
RUN  zypper --non-interactive update \
  && zypper --non-interactive install \
            git \
            scons \
            cmake \
            gcc \
            clang \
            ninja \
            libasan4 \
            libtsan0 \
            pkg-config \
            protobuf-devel \
            protobuf-c \
            boost_1_65-devel \
            libopenssl-devel \
  && git clone https://github.com/ripple/rippled.git /rippled \
  && git --version \
  && bash --version \
  && cmake --version \
  && lscpu --version \
  && grep --version \
  && scons --version \
  && ninja --version \
  && pkg-config --version \
  && gcc --version \
  && clang --version \
  && protoc --version

WORKDIR /rippled/Builds

CMD ["/bin/bash", "/rippled/Builds/build_all.sh"]