vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp menu.o
	@$(CXX) $^ -o $@

menu.o: menu.cpp menu.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main