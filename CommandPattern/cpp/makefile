vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp remote_control.o
	@$(CXX) $^ -o $@

remote_control.o: remote_control.cpp remote_control.h
	@$(CXX) $^ -c

.PHONY: clean run
clean:
	@-rm -rf *.o *.gch

run:
	@./main