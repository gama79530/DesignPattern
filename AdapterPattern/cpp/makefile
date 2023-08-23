vpath %.cpp src src/lib
vpath %.h src/header src/lib/header

CXX = g++

HEADER_PATH = src/header
SOURCE_PATH = src
LIB_PATH = src/lib

all: main clean run
	
main: main.cpp computer.o old_cpu.o
	@$(CXX) $^ -o $@

computer.o: computer.cpp computer.h old_cpu.h
	@$(CXX) $< -c

old_cpu.o: old_cpu.cpp old_cpu.h
	@$(CXX) $< -c

.PHONY: clean run
clean:
	@-rm -rf *.o *.gch

run:
	@./main