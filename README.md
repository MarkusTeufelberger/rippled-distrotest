Travis builds of a small subset of possible builds:

[![Build Status](https://travis-ci.org/MarkusTeufelberger/rippled-distrotest.svg?branch=master)](https://travis-ci.org/MarkusTeufelberger/rippled-distrotest)

This project aims to regularly build and test all possible build variants of
https://github.com/ripple/rippled/ on different Linux distributions using their
upstream packages.

Ideally the `build_all.sh` script from the /Builds folder in the rippled repo should run with 0 errors on every distro out there.

Status at the moment:

## Alpine Linux

### 3.5

Boost: 1.62.0 (https://pkgs.alpinelinux.org/packages?name=boost&branch=v3.5)

Requires musl compatibility patches.

### 3.6

Boost: 1.62.0 (https://pkgs.alpinelinux.org/packages?name=boost&branch=v3.6)

Requires musl compatibility patches.

### 3.7

Boost: 1.62.0 (https://pkgs.alpinelinux.org/packages?name=boost&branch=v3.7)

Requires musl compatibility patches.

### Edge (Rolling Release)

Boost: 1.66.0 (https://pkgs.alpinelinux.org/packages?name=boost&branch=edge)

Upstream: https://pkgs.alpinelinux.org/package/edge/testing/x86_64/rippled

One of the few distros that at least have an actual rippled package upstream (in edge/testing).
It requires a few patches that still weren't accepted in rippled so far (https://github.com/alpinelinux/aports/tree/master/testing/rippled).

## Arch Linux

### (Rolling Release)

Boost: 1.67.0 (https://www.archlinux.org/packages/extra/x86_64/boost/)

Upstream: https://aur.archlinux.org/packages/rippled/

Not 100% "upstream" (the AUR is more of a collection of build scripts and open for anyone to contribute), but at least some build script is available and maintained.

## CentOS/RHEL

The only distro Ripple currently ships pre-built binaries for (https://mirrors.ripple.com/rpm/) and one of 2 supported platforms (https://ripple.com/build/rippled-setup/#installing-rippled)

### 7

Boost: 1.53.0 (https://pkgs.org/download/boost)

Ships with gcc 4.8 (https://pkgs.org/download/gcc) which is too old to build rippled.

The devtoolset collection from the SCLo repository could be a solution, but is not exactly "upstream".

OTOH, ninja-build also already must be pulled in from EPEL, but that's because it is only available there.

Another issue is the CMake version (rippled requires at least CMake version 3.1.0).


## Debian

### Jessie

Boost: 1.55.0 (https://packages.debian.org/jessie/libboost-all-dev)

Boost too old to build.

No backports are available, but rippled builds on newer Debian versions.

Another issue is the CMake version (rippled requires at least CMake version 3.1.0).

### Stretch

Boost: 1.62.0 (https://packages.debian.org/stretch/libboost-all-dev)

### Buster

Boost: 1.62.0 (https://packages.debian.org/buster/libboost-all-dev)

### Sid (Rolling Release)

Boost: 1.62.0 (https://packages.debian.org/sid/libboost-all-dev)

## Fedora

### 27

Boost: 1.64.0 (https://apps.fedoraproject.org/packages/boost)

### 28

Boost: 1.66.0 (https://apps.fedoraproject.org/packages/boost)

### Rawhide (Rolling Release)

Boost: 1.66.0 (https://apps.fedoraproject.org/packages/boost)

Currently ships without `/usr/bin/python`, but has `/usr/bin/python3` installed.

Not a hard build dependency for `rippled`.

## OpenSUSE

### Leap (42.3)

Boost: 1.61.0 (https://software.opensuse.org/package/boost)

### Leap (15.0)

Boost: 1.66.0 (https://software.opensuse.org/package/boost)

Boost is split into tons of individual sub-packages (https://lists.opensuse.org/opensuse-factory/2017-02/msg00024.html).

### Tumbleweed (Rolling Release)

Boost: 1.67.0 (https://software.opensuse.org/package/boost)

Boost is split into tons of individual sub-packages (https://lists.opensuse.org/opensuse-factory/2017-02/msg00024.html).

## Ubuntu

Officially supported by Ripple (https://ripple.com/build/rippled-setup/#installing-rippled) "Ubuntu 15.04 or later".
No deb packages offered, only rpm.

### 16.04 (LTS)

Boost: 1.58.0 (https://packages.ubuntu.com/xenial/libboost-all-dev)

Boost too old to build.

No backports for libboost are available, but rippled builds on newer Ubuntu versions.

### 17.10

Boost: 1.62.0 (https://packages.ubuntu.com/artful/libboost-all-dev)

### 18.04 (LTS)

Boost: 1.65.1 (https://packages.ubuntu.com/bionic/libboost-all-dev)

### 18.10

Boost: 1.65.1 (https://packages.ubuntu.com/cosmic/libboost-all-dev)

