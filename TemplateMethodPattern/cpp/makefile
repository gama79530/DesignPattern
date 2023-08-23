vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp solution.o
	@$(CXX) $^ -o $@

solution.o: solution.cpp solution.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main