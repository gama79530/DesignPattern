vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp pizza_store.o
	@$(CXX) $^ -o $@

pizza_store.o: pizza_store.cpp pizza_store.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main