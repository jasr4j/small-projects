#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

void switch_versions() {
        int javaswitch = system("sudo update-alternatives --config java");
        if (javaswitch != 0) {
                printf("Java not installed; Install with jvmanager\n");
                exit(1); 
        }
        system("sudo update-alternatives --config javac"); 
        printf("Changed Java and JavaC Default\n");
}

void listPkg() {
        printf("POSSIBLE INSTALL VERSIONS: \n");
        printf("Adoptium: temurin-<version>-jdk\n"); 
        printf("OpenJDK: openjdk-<version>-jdk\n");
}

int helpFunction() {
        printf("POSSIBLE COMMANDS: \n"); 
        printf("jvmanager install <jdk_name>\n");
        printf("jvmanager remove <jdk_name>\n"); 
        printf("jvmanager switch\n");
        printf("jvmanager --help\n"); 
        printf("jvmanager list-packages\n");
        printf("jvmanager setup-temurin\n"); 
        exit(0);
}

int installer(char* package) {
        printf("INSTALLING PACKAGE %s\n ", package); 
        char command[100]; 
        sprintf(command, "sudo apt install %s", package);
        system(command); 
        return 0;
}

int remover(char* package) {
        printf("REMOVING PACKAGE %s\n ", package); 
        char command[100]; 
        sprintf(command, "sudo apt remove --purge %s", package);
        system(command); 
        return 0;
}

int parseArgs(char* arg) {
        if (strcmp(arg, "switch") == 0) {
                switch_versions();
                exit(0); 
        } else if (strcmp(arg, "--help") == 0) {
                helpFunction(); 
        } else if (strcmp(arg, "install") == 0) {
                return 1; 
        } else if (strcmp(arg, "remove") == 0) {
                return 2;
        } else if (strcmp(arg, "list-packages") == 0) {
                listPkg(); 
        } else if (strcmp(arg, "setup-temurin") == 0) {
                system("sudo apt install -y wget apt-transport-https gpg"); 
                system("wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null");
                system("echo \"deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main\" | tee /etc/apt/sources.list.d/adoptium.list");
                system("sudo apt update");
        } else {
                printf("Argument %s is not recognized by jvmanager\n", arg);
                helpFunction(); 
        }
        return 0;
}

int main(int argc, char **argv) {
        argc--;
        if (argc < 1) {
                printf("Error: Needs Arguments\n");
                printf("Enter jvmanager --help into the console to see a list of commands\n");
                return 1;
        }
        // printf("You have inputted %d arguments\n", argc); 
        for (int i = 1; i < argc + 1; i++) {
                // printf("%s\n", argv[i]); 
                int n = parseArgs(argv[i]); 
                switch(n) {
                        case 0: 
                                return 0; 
                        case 1: 
                                if (argv[i+1] == NULL) {
                                        perror("NO ARG\n"); 
                                        exit(1); 
                                }
                                installer(argv[i+1]); 
                                return 0;
                        case 2: 
                                if (argv[i+1] == NULL) {
                                        perror("NO ARG\n"); 
                                        exit(1); 
                                }
                                remover(argv[i+1]); 
                                return 0;
                        default:
                                perror("Error parsing arguments\n"); 
                                return 1;
                }
        }
        return 0;
}