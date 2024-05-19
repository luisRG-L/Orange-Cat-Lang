#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NATURAL_ROUTE getenv("USERPROFILE")

void print_help() {
    printf("Use: ocat [options]\n");
    printf("Options:\n");
    printf("  version           Shows the ocat version\n");
    printf("    --version           Shows the ocat version with other details");
    printf("  help              Shows the help text\n");
    printf("  run               Executes an ocat file\n");
    printf("  open              Opens the ocat directory\n");
    printf("  dev               Creates a new orange cat project");
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
        char command[512];
        const char *python_script_path = "\\Documents\\Orange Cat\\versions\\pro\\OrangeCat.py";
        snprintf(command, sizeof(command), "python \"%s%s\"", NATURAL_ROUTE, python_script_path);
        int status = system(command);
        if (status == -1) {
            printf("Error executing this script n\n");
        } else {
            printf("Exit code: %d\n", status);
        }
    } else if (strcmp(argv[1], "open") == 0) {
        char command[512];
        const char *file_path = "\\Documents\\Orange Cat\\versions\\pro";
        snprintf(command, sizeof(command), "explorer %s%s", file_path);
        int status = system(command);
        if (status == -1) {
            printf("Error executing this script\n");
        } else {
            printf("Exit status: %d\n", status);
        }
    } else if (strcmp(argv[1], "dev") == 0) {
        char command[512];
        const char *file_path = "C:\\Users\\peque\\Documents\\Orange Cat\\versions\\pro\\dev.py";
        snprintf(command, sizeof(command), "python \"%s%s\"", NATURAL_ROUTE, file_path);
        int status = system(command);
        if (status == -1) {
            printf("Error executing this script\n");
        } else {
            printf("Exit status: %d\n", status);
        }
    } else {
        printf("This ocat variant doesn't exists, put 'ocat help' for get the ocat variations\n");
    }

    return 0;
}
