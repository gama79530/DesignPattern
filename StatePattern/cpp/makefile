vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp taxi.o
	@$(CXX) $^ -o $@

taxi.o: taxi.cpp taxi.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main