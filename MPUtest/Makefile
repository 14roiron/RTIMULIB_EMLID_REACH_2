CC = arm-linux-gnueabi-g++
NAVIO = ../../Navio
INCLUDES = -I ../..
FLAGS = -march=armv5

all:
	$(CC) $(INCLUDES) MPUtest.cpp MPU9250.cpp SPIdev.h  $(FLAGS) -o MPUtest

clean:
	rm MPUtest
