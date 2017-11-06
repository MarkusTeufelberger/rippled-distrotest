Travis builds of a small subset of possible builds:

[![Build Status](https://travis-ci.org/MarkusTeufelberger/rippled-distrotest.svg?branch=master)](https://travis-ci.org/MarkusTeufelberger/rippled-distrotest)

This project aims to regularly build and test all possible build variants of
https://github.com/ripple/rippled/ on different Linux distributions using their
upstream packages.

Ideally the `build_all.sh` script from the /Builds folder in the rippled repo should run with 0 errors on every distro out there.

Status at the moment:

## Alpine Linux

### Edge (Rolling Release)

Upstream: https://pkgs.alpinelinux.org/package/edge/testing/x86_64/rippled

One of the few distros that at least have an actual rippled package upstream (in edge/testing).
It requires a few patches that still weren't accepted in rippled so far.

### 3.5

Requires musl compatibility patches in RocksDB and rippled (beast).

### 3.6

Requires musl compatibility patches in RocksDB and rippled (beast).

## Arch Linux

### (Rolling Release)

Upstream: https://aur.archlinux.org/packages/rippled/

Not 100% "upstream" (the AUR is more of a collection of build scripts and open for anyone to contribute), but at least seom build script is available and maintained.

## CentOS/RHEL

### 7

Ships with gcc 4.8 (https://pkgs.org/download/gcc) which is too old to build rippled.

The devtoolset collection from the SCLo repository could be a solution, but is not exactly "upstream".

OTOH, ninja-build also already must be pulled in from EPEL, but that's because it is only available there.

The only distro Ripple currently ships pre-built binaries for (https://mirrors.ripple.com/rpm/) and one of 2 supported platforms (https://ripple.com/build/rippled-setup/#installing-rippled)

## Debian

### Jessie

Ships with libboost 1.55 (https://packages.debian.org/search?keywords=libboost, https://pkgs.org/download/libboost) which is too old to build rippled.

No backports are available, but rippled builds on newer Debian versions.

### Stretch

...

### Buster

...

### Sid (Rolling Release)

...

## Fedora

### 25

...

### 26

...

### Rawhide (Rolling Release)

...

## OpenSUSE

### Leap (42.3)

...

### Tumbleweed (Rolling Release)

...

## Ubuntu

Officially supported by Ripple (https://ripple.com/build/rippled-setup/#installing-rippled) "Ubuntu 15.04 or later".
No deb packages offered though, only rpm.

### 16.04 (LTS)

...

### 17.04

...

### 17.10

...
