#!/usr/bin/env python3

distros = [
    "alpine-3.5",
    "alpine-3.6",
    "alpine-3.7",
    "alpine-3.8",
    "alpine-edge",
    "archlinux",
    "centos-7",
    "debian-jessie",
    "debian-stretch",
    "debian-buster",
    "debian-sid",
    "fedora-27",
    "fedora-28",
    "fedora-29",
    "fedora-rawhide",
    "opensuse-leap-42",
    "opensuse-leap-15",
    "opensuse-tumbleweed",
    "ubuntu-16.04",
    "ubuntu-18.04",
    "ubuntu-18.10",
]

# these don't even manage to build the default build
broken_distros = [
    # need patches/fixes upstream, boost too old and not backported
    "alpine-3.5",
    "alpine-3.6",
    "alpine-3.7",
    "alpine-3.8",
    # need patches/fixes upstream
    "alpine-edge",
    # pretty much everything too old
    "centos-7",
    # boost too old and not backported, cmake too old
    "debian-jessie",
    # boost too old and not backported
    "debian-stretch",
    "debian-buster",
    "debian-sid",  # boost 1.67 already in testing
    "fedora-27",
    "fedora-28",
    "fedora-29",
    "fedora-rawhide",
    "opensuse-leap-42",
    "opensuse-leap-15",
    "ubuntu-16.04",
    "ubuntu-18.04",
]

travis_test_py_opts = [
    # ("commandline option(s)", "description")
    ("", "default build"),
    ("--generator_option=-Dstatic=OFF", "default build"),
    # TODO: install doxygen everywhere
    # ("--dir docs", "documentation build")
    ("--dir clang.release", "clang release build"),
    ("--dir gcc.release", "gcc release build"),
    ("--dir clang.release --generator_option=-Dstatic=OFF",
     "clang release nonstatic build"),
    ("--dir gcc.release --generator_option=-Dstatic=OFF",
     "gcc release nonstatic build"),
    ("--dir clang.debug --generator_option=-GNinja --generator_option=-Dsan=thread",
     "clang debug ninja build with TSAN enabled"),
    ("--dir clang.debug --generator_option=-GNinja --generator_option=-Dsan=address",
     "clang debug ninja build with ASAN enabled"),
    ("--dir gcc.debug --generator_option=-GNinja --generator_option=-Dsan=thread",
     "gcc debug ninja build with TSAN enabled"),
    ("--dir gcc.debug --generator_option=-GNinja --generator_option=-Dsan=address",
     "gcc debug ninja build with ASAN enabled"),
    ("--dir clang.debug --generator_option=-Dstatic=OFF --generator_option=-GNinja --generator_option=-Dsan=thread",
     "clang debug nonstatic ninja build with TSAN enabled"),
    ("--dir clang.debug --generator_option=-Dstatic=OFF --generator_option=-GNinja --generator_option=-Dsan=address",
     "clang debug nonstatic ninja build with ASAN enabled"),
    ("--dir gcc.debug --generator_option=-Dstatic=OFF --generator_option=-GNinja --generator_option=-Dsan=thread",
     "gcc debug nonstatic ninja build with TSAN enabled"),
    ("--dir gcc.debug --generator_option=-Dstatic=OFF --generator_option=-GNinja --generator_option=-Dsan=address",
     "gcc debug nonstatic ninja build with ASAN enabled"),
    ("--dir clang.release.nounity --generator_option=-GNinja",
     "clang release nounity ninja build"),
    ("--dir gcc.release.nounity --generator_option=-GNinja",
     "gcc release nounity ninja build"),
    ("--dir clang.release.nounity --generator_option=-Dstatic=OFF --generator_option=-GNinja",
     "clang release nonstatic nounity ninja build"),
    ("--dir gcc.release.nounity --generator_option=-Dstatic=OFF --generator_option=-GNinja",
     "gcc release nonstatic nounity ninja build"),
]

with open(".travis.yml", "w") as travisfile:
    # header
    print(
        """sudo: required

services:
  - docker

# most builds are with ninja because it automatically uses all available cores
# Travis-ci is rather limited in that regards though
env:""",
        file=travisfile)

    # content
    for test_py_opt in travis_test_py_opts:
        # description
        print(f"  # {test_py_opt[1]}", file=travisfile)
        # commandline option(s) and distro
        for distro in distros:
            if test_py_opt[
                    1] == "default build" or distro not in broken_distros:
                print(
                    f'  - TEST_PY_OPTS="{test_py_opt[0]}" DISTRO={distro}',
                    file=travisfile)

    # footer
    print(
        """
before_install:
  - cd $DISTRO
  - docker build --pull --no-cache -t rippled/$DISTRO .
  # --no-cache might not be necessary because it is unlikely that Travis-ci re-uses build VMs
  # - docker build -t rippled/$DISTRO .

script:
  - docker run --rm -t rippled/$DISTRO /bin/bash -c "cd .. && ./Builds/Test.py -v $TEST_PY_OPTS"
  # This takes FAR too long for Travis-ci:
  # - docker run --rm -t rippled/$DISTRO /bin/bash -c "./build_all.sh"
""",
        file=travisfile)

build_types = [
    "gcc.debug.nounity",
    "gcc.debug.unity",
    "gcc.debug.coverage.nounity",
    "gcc.debug.coverage.unity",
    "gcc.release.nounity",
    "gcc.release.unity",
    "gcc.debug.nounity.profile",
    "gcc.debug.unity.profile",
    "gcc.debug.coverage.nounity.profile",
    "gcc.debug.coverage.unity.profile",
    "gcc.release.nounity.profile",
    "gcc.release.unity.profile",
    "clang.debug.nounity",
    "clang.debug.unity",
    "clang.debug.coverage.nounity",
    "clang.debug.coverage.unity",
    "clang.release.nounity",
    "clang.release.unity",
    "clang.debug.nounity.profile",
    "clang.debug.unity.profile",
    "clang.debug.coverage.nounity.profile",
    "clang.debug.coverage.unity.profile",
    "clang.release.nounity.profile",
    "clang.release.unity.profile",
]

sanitizers = [
    "none",
    "address",
    "thread",
    "memory",
    "undefined",
]

with open("azure-pipelines.yml", "w") as azurefile:
    # header
    print(
        """# To prevent excessive use of resources, start with a simple static and nonstatic build.
# Then make every other build a matrix build depending on the initial one succeeding.

# Job dependencies: https://docs.microsoft.com/en-us/azure/devops/pipelines/process/conditions?view=vsts&tabs=yaml#job-status-functions
# Matrix build strategy: https://docs.microsoft.com/en-us/azure/devops/pipelines/process/phases?view=vsts&tabs=yaml#multi-configuration
jobs:""",
        file=azurefile)
    # initial smoketest builds
    for distro in distros:
        # static
        print(
            f"- job: {distro.replace('-', '_').replace('.', '_')}_static_smoketest",
            file=azurefile)
        print("  pool:", file=azurefile)
        print("    vmImage: 'Ubuntu 16.04'", file=azurefile)
        print("  steps:", file=azurefile)
        print("  - script: |", file=azurefile)
        print(f"      cd {distro}", file=azurefile)
        print(
            f"      docker build --pull --no-cache -t rippled/{distro} .",
            file=azurefile)
        print(
            f'      docker run --rm -t rippled/{distro} /bin/bash -c "cd .. && ./Builds/Test.py -v --generator_option=-Dstatic=ON"',
            file=azurefile)
        # nonstatic
        print(
            f"- job: {distro.replace('-', '_').replace('.', '_')}_nonstatic_smoketest",
            file=azurefile)
        print("  pool:", file=azurefile)
        print("    vmImage: 'Ubuntu 16.04'", file=azurefile)
        print("  steps:", file=azurefile)
        print("  - script: |", file=azurefile)
        print(f"      cd {distro}", file=azurefile)
        print(
            f"      docker build --pull --no-cache -t rippled/{distro} .",
            file=azurefile)
        print(
            f'      docker run --rm -t rippled/{distro} /bin/bash -c "cd .. && ./Builds/Test.py -v --generator_option=-Dstatic=OFF"',
            file=azurefile)
    # all possible builds, depend on the smoketest being successful
    print("# actual matrix builds start here", file=azurefile)
    for distro in distros:
        # static
        print(
            f"- job: {distro.replace('-', '_').replace('.', '_')}_static_matrix",
            file=azurefile)
        print("  pool:", file=azurefile)
        print("    vmImage: 'Ubuntu 16.04'", file=azurefile)
        print(
            f"  dependsOn: {distro.replace('-', '_').replace('.', '_')}_static_smoketest",
            file=azurefile)
        print("  condition: succeeded()", file=azurefile)
        print("  strategy:", file=azurefile)
        print("    matrix:", file=azurefile)
        for build_type in build_types:
            for sanitizer in sanitizers:
                if sanitizer == "none":
                    print(
                        f"      {distro.replace('-', '_').replace('.', '_')}_static_{build_type.replace('.', '_')}:",
                        file=azurefile)
                    print(
                        f"        TEST_PY_OPTS: --dir {build_type}",
                        file=azurefile)
                else:
                    print(
                        f"      {distro.replace('-', '_').replace('.', '_')}_static_{build_type.replace('.', '_')}_{sanitizer}:",
                        file=azurefile)
                    print(
                        f"        TEST_PY_OPTS: --dir {build_type} --generator_option=-Dsan={sanitizer}",
                        file=azurefile)
        print("  steps:", file=azurefile)
        print("  - script: |", file=azurefile)
        print(f"      cd {distro}", file=azurefile)
        print(
            f"      docker build --pull --no-cache -t rippled/{distro} .",
            file=azurefile)
        print(
            f'      docker run --rm -t rippled/{distro} /bin/bash -c "cd .. && ./Builds/Test.py -v --generator_option=-GNinja --generator_option=-Dstatic=ON $TEST_PY_OPTS"',
            file=azurefile)
        # nonstatic
        print(
            f"- job: {distro.replace('-', '_').replace('.', '_')}_nonstatic_matrix",
            file=azurefile)
        print("  pool:", file=azurefile)
        print("    vmImage: 'Ubuntu 16.04'", file=azurefile)
        print(
            f"  dependsOn: {distro.replace('-', '_').replace('.', '_')}_nonstatic_smoketest",
            file=azurefile)
        print("  condition: succeeded()", file=azurefile)
        print("  strategy:", file=azurefile)
        print("    matrix:", file=azurefile)
        for build_type in build_types:
            for sanitizer in sanitizers:
                if sanitizer == "none":
                    print(
                        f"      {distro.replace('-', '_').replace('.', '_')}_nonstatic_{build_type.replace('.', '_')}:",
                        file=azurefile)
                    print(
                        f"        TEST_PY_OPTS: --dir {build_type}",
                        file=azurefile)
                else:
                    print(
                        f"      {distro.replace('-', '_').replace('.', '_')}_nonstatic_{build_type.replace('.', '_')}_{sanitizer}:",
                        file=azurefile)
                    print(
                        f"        TEST_PY_OPTS: --dir {build_type} --generator_option=-Dsan={sanitizer}",
                        file=azurefile)
        print("  steps:", file=azurefile)
        print("  - script: |", file=azurefile)
        print(f"      cd {distro}", file=azurefile)
        print(
            f"      docker build --pull --no-cache -t rippled/{distro} .",
            file=azurefile)
        print(
            f'      docker run --rm -t rippled/{distro} /bin/bash -c "cd .. && ./Builds/Test.py -v --generator_option=-GNinja --generator_option=-Dstatic=OFF $TEST_PY_OPTS"',
            file=azurefile)
