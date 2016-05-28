#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include <string.h>

#include <openssl/md5.h>
#include <openssl/sha.h>

void custom_hexlify(unsigned char*, char*);

int main(int argc, char *argv[]){

    char *target = {"ff378b84e6d42e5078bdc02711477cc6"};

    if(argc == 2){  // we need a file
        if(access(argv[1], R_OK)){
            fprintf(stderr, "Could not access file %s\n", argv[1]);
            return EXIT_FAILURE;
        }
    } else {
        fprintf(stderr, "Usage: %s <wordlist>\n", argv[0]);
        return EXIT_FAILURE;
    }

    FILE *f;
    char buf[32] = {0};
    char *pbuf = calloc(sizeof(char), 6);
    unsigned char sha1_md[SHA_DIGEST_LENGTH] = {0};
    unsigned char md5_md[MD5_DIGEST_LENGTH] = {0};

    /* log:
     * sha1 - md5 - sha1 - md5 : f
     * sha1 - sha1 - md5 - md5 : f
     * md5 - md5 - sha1 - sha1 : f
     * md5 - sha1 - sha1 - md5 : f
     * sha1 - md5 - md5 - sha1 : r
    */

    f = fopen(argv[1], "r");
    while(fscanf(f, "%s", pbuf) != EOF){
        strcpy(buf, pbuf);

        SHA1((unsigned char*)buf, strlen(buf), sha1_md);
        custom_hexlify(sha1_md, buf);

        MD5((unsigned char*)buf, strlen(buf), md5_md);
        custom_hexlify(md5_md, buf);

        MD5((unsigned char*)buf, strlen(buf), md5_md);
        custom_hexlify(md5_md, buf);

        SHA1((unsigned char*)buf, strlen(buf), sha1_md);
        custom_hexlify(sha1_md, buf);

        if(strcmp(buf, target) == 0){
            printf("smms%s\n", pbuf);
            break;
        }
    }
    fclose(f);
    free(pbuf);
    return EXIT_SUCCESS;
}

inline void custom_hexlify(unsigned char *md, char *buf){
    uint8_t i;
    for(i = 0; i < 16; i++)
        sprintf(&buf[i*2], "%02x", md[i]);
}
