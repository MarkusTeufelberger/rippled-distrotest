FROM archlinux/base

# Update the OS to current packages, install dependencies, clone repo
RUN  pacman -Syu --noconfirm \
  && pacman -S --noconfirm \
  grep \
  git \
  cmake \
  make \
  ninja \
  clang \
  pkg-config \
  protobuf \
  boost \
  boost-libs \
  python \
  doxygen \
  && git clone https://github.com/ripple/rippled.git /rippled \
  && git --version \
  && bash --version \
  && make --version \
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
