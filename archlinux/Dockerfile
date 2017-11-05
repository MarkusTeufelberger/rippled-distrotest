FROM archimg/base

# Update the OS to current packages, install dependencies, clone repo
RUN  pacman -Syu --noconfirm \
  && pacman -S --noconfirm \
            grep \
            git \
            cmake \
            scons \
            ninja \
            clang \
            pkg-config \
            protobuf \
            boost \
            boost-libs \
            python \
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
