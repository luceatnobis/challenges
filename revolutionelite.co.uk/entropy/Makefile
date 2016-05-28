WARN = -Wall
DEBUG = -ggdb3
EXENAME = entropy

LINKING = -lcrypto

all:
	$(CC)  *.c $(LINKING) -o $(EXENAME)
debug:
	$(CC) $(DEBUG) $(WARN)  *.c $(LINKING) -o $(EXENAME)
