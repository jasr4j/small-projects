File Format for all config files will be JVMF (Java Version Manager Format)

tree.jvmf contains all the JDKs and Versions. 

Use C Preprocessor Directives to Check OS

```c
#ifdef _WIN32
        printf("Running on Windows (32-bit or 64-bit)\n");
#elif __linux__
        printf("Running on Linux\n");
#elif __APPLE__
        printf("Running on macOS or iOS\n");
#else
        printf("Unknown operating system\n");
#endif
```