vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp computer.o
	@$(CXX) $^ -o $@

computer.o: computer.cpp computer.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main