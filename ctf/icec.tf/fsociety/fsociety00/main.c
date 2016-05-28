#include "socket.h"
#include "irc.h"
#include "unistd.h"

int main(int argc, char **argv)
{
    irc_t irc;

    if ( irc_connect(&irc, "glitch.is", "6667") < 0 )
    {
        fprintf(stderr, "Connection failed.\n");
        goto exit_err;
    }

    irc_set_output(&irc, "/dev/stdout");

    if ( irc_login(&irc, "luceatvobis") < 0 )
    {
        fprintf(stderr, "Couldn't log in.\n");
        goto exit_err;
    }

    if ( irc_join_channel(&irc, "#IceCTF") < 0 )
    {
        fprintf(stderr, "Couldn't join channel.\n");
        goto exit_err;
    }

    while ( irc_handle_data(&irc) >= 0 );

    irc_close(&irc);
    return 0;

exit_err:
    irc_close(&irc);
    exit(1);
}

