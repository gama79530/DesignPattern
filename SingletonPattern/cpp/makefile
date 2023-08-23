vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp car_management.o
	@$(CXX) $^ -o $@

car_management.o: car_management.cpp car_management.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main