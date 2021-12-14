CC=gcc
CFLAGS=-I. -Wall
DEPS = vectorops.h

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

vectors.exe: vectorops.o main.o
	$(CC) -o vectors.exe vectorops.o main.o
