vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp office_device.o
	@$(CXX) $^ -o $@

office_device.o: office_device.cpp office_device.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main