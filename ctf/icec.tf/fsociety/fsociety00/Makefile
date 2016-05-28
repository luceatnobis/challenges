
CC = gcc

TARGET = ircbot

OBJECTS = main.o irc.o socket.o

all: $(TARGET)

%.o: %.c
	$(CC) -ggdb3 -c -o $@ $<

clean: clean-obj clean-bin

clean-obj:
	rm -rf *.o

clean-bin:
	rm -rf $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) -ggdb3 -o $(TARGET) $(OBJECTS)
