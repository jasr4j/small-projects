## Java Version Manager

### How to compile from source: 

```bash
$ cd previous/java-version-manager
$ gcc main.c -std=c17 -o jvmanager
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
