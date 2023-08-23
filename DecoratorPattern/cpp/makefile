vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp beverage.o
	@$(CXX) $^ -o $@

beverage.o: beverage.cpp beverage.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main