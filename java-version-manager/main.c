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

int helpFunction() {
        printf("POSSIBLE COMMANDS: \n"); 
        printf("jvmanager install <jdk_name>\n");
        printf("jvmanager remove <jdk_name>\n"); 
        printf("jvmanager switch\n");
        printf("jvmanager help\n"); 
        exit(0);
}

int installer() {
        /*
         * Fetch from web and use distro specific commands to install jdk
         */
        return 0;
}

int remover() {
        /*
         * Remove from system with native package manager
         */
        return 0;
}

int parseArgs(char* arg) {
        if (strcmp(arg, "switch") == 0) {
                switch_versions();
                exit(0); 
        } else if (strcmp(arg, "help") == 0) {
                helpFunction(); 
        } else if (strcmp(arg, "install") == 0) {
                installer(); 
        } else if (strcmp(arg, "remove") == 0) {
                remover(); 
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
                parseArgs(argv[i]); 
        }
        return 0;
}