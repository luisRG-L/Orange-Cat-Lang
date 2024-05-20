#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NATURAL_ROUTE getenv("USERPROFILE")
#define ABSOLUTE_PATH "\\Orange-Cat-Lang\\pro\\"

void print_help() {
    printf("Use: ocat [options]\n");
    printf("Options:\n");
    printf("  version           Shows the ocat version\n");
    printf("    --version           Shows the ocat version with other details\n");
    printf("  help              Shows the help text\n");
    printf("  run               Executes an ocat file\n");
    printf("    dev               Executes an orange cat project\n");
    printf("  open              Opens the ocat directory\n");
    printf("  clear             Clear the 'projects' folder\n");
    printf("  create            Creates a new orange cat file\n");
    printf("    dev               Creates a new orange cat project\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("This command don't exists\n");
        return 1;
    }

    if (strcmp(argv[1], "version") == 0) {
        printf("1.0.0\n");
    } else if (strcmp(argv[1], "--version") == 0) {
        printf("1.0.0: 19/5/24");
    } else if (strcmp(argv[1], "help") == 0) {
        print_help();
    } else if (strcmp(argv[1], "run") == 0) {
        if (argc > 2 && strcmp(argv[2], "dev") == 0) {
            char command[512];
            const char *python_script = "devRunner.py";
            snprintf(command, sizeof(command), "python \"%s%s%s\"", NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                printf("Error executing this script\n");
            } else {
                printf("Exit code: %d\n", status);
            }
        } else if (argc > 2 && strcmp(argv[2], "") == 0){
            char command[512];
            const char *python_script = "runner.py";
            snprintf(command, sizeof(command), "python \"%s%s%s\"", NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                printf("Error executing this script\n");
            } else {
                printf("Exit code: %d\n", status);
            }
        }
    } else if (strcmp(argv[1], "open") == 0) {
        char command[512];
        snprintf(command, sizeof(command), "explorer %s%s", NATURAL_ROUTE, ABSOLUTE_PATH);
        int status = system(command);
        if (status == -1) {
            printf("Error opening the explorer\n");
        } else {
            printf("Exit status: %d\n", status);
        }
    } else if (strcmp(argv[1], "clear") == 0) {
        char command[512];
        const char *python_script = "clear.py";
        snprintf(command, sizeof(command), "python \"%s%s%s\"", NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
        int status = system(command);
        if (status == -1) {
            printf("Error executing this script\n");
        } else {
            printf("Exit status: %d\n", status);
        }
    } else if (argc > 2 && strcmp(argv[1], "create") == 0) {
        if (strcmp(argv[2], "dev") == 0) {
            char command[512];
            const char *python_script = "dev.py";
            snprintf(command, sizeof(command), "python \"%s%s%s\"", NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                printf("Error executing this script\n");
            } else {
                printf("Exit status: %d\n", status);
            }
        } else if(argc > 2 && strcmp(argv[2], "file") == 0){
            char command[512];
            const char *python_script = "creater.py";
            snprintf(command, sizeof(command), "python \"%s%s%s\"", NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                printf("Error executing this script\n");
            } else {
                printf("Exit status: %d\n", status);
            }
        }
    }else {
        printf("This ocat variant doesn't exists, put 'ocat help' for get the ocat variations\n");
    }

    return 0;
}