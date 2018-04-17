#!/usr/bin/env python3

distros = [
"alpine-3.5",
"alpine-3.6",
"alpine-3.7",
"alpine-edge",
"archlinux",
"centos-7",
"debian-jessie",
"debian-stretch",
"debian-buster",
"debian-sid",
"fedora-26",
"fedora-27",
"fedora-28",
"fedora-rawhide",
"opensuse-42.3",
"opensuse-tumbleweed",
"ubuntu-16.04",
"ubuntu-17.10",
"ubuntu-18.04",
]

# these don't even manage to build the default build
broken_distros = [
# need patches/fixes upstream
"alpine-3.5",
"alpine-3.6",
"alpine-3.7",
"alpine-edge",
# boost too old and not backported
"debian-jessie",
]

test_py_opts = [
# ("commandline option(s)", "description")
("", "default build"),
("--dir clang.release", "clang release build"),
("--dir gcc.release", "gcc release build"),
("--dir clang.debug --generator_option=-GNinja --generator_option=-Dsan=thread", "clang debug ninja build with TSAN enabled"),
("--dir clang.debug --generator_option=-GNinja --generator_option=-Dsan=address", "clang debug ninja build with ASAN enabled"),
("--dir gcc.debug --generator_option=-GNinja --generator_option=-Dsan=thread", "gcc debug ninja build with TSAN enabled"),
("--dir gcc.debug --generator_option=-GNinja --generator_option=-Dsan=address", "gcc debug ninja build with ASAN enabled"),
("--dir clang.release.nounity  --generator_option=-GNinja", "clang release nounity ninja build"),
("--dir gcc.release.nounity  --generator_option=-GNinja", "gcc release nounity ninja build"),
("--dir clang.coverage --static --assert --generator_option=-GNinja", "clang coverage ninja build statically linked and with assertions enabled"),
("--dir gcc.coverage --static --assert --generator_option=-GNinja", "gcc coverage ninja build statically linked and with assertions enabled"),
]

with open(".travis.yml", "w") as travisfile:
    # header
    print("""sudo: required

services:
  - docker

# most builds are with ninja because it automatically uses all available cores
# Travis-ci is rather limited in that regards though
env:""", file=travisfile)

    # content
    for test_py_opt in test_py_opts:
        print(f"  # {test_py_opt[1]}", file=travisfile)
        for distro in distros:
            if test_py_opt[1] == "default build" or distro not in broken_distros:
                print(f'  - TEST_PY_OPTS="{test_py_opt[0]}" DISTRO={distro}', file=travisfile)

    # footer
    print("""
before_install:
  - cd $DISTRO
  - docker build --pull --no-cache -t rippled/$DISTRO .
  # --no-cache might not be necessary because it is unlikely that Travis-ci re-uses build VMs
  # - docker build -t rippled/$DISTRO .

script:
  - docker run --rm -t rippled/$DISTRO /bin/bash -c "cd .. && ./Builds/Test.py -v $TEST_PY_OPTS"
  # This takes FAR too long for Travis-ci:
  # - docker run --rm -t rippled/$DISTRO /bin/bash -c "./build_all.sh"
""", file=travisfile)
