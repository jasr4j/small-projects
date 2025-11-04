## Java Version Manager

### How to compile from source: 

```bash
$ cd previous/java-version-manager
$ make
$ ./jvmanager <arg>
```

GOAL: 

* Automatically detects OS
* Installs binaries in the native package manager (e.g. apt, dnf, scoop, brew)

Current OS Support in Progress: 

* Debian and Ubuntu

Support Goals: 

* RHEL/CentOS/Fedora & Derivatives (dnf)
* MacOS X (brew)
* Windows (likely the hardest because of exes)

Resource on JDKs: [Blog on Medium](https://medium.com/@Fredtaylor1/openjdk-temurin-graalvm-which-java-should-you-actually-install-9eb88c1eb8dd)