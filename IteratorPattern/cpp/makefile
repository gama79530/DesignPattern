vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp vehicle.o garage.o
	@$(CXX) $^ -o $@

vehicle.o: vehicle.cpp vehicle.h
	@$(CXX) $< -c

garage.o: garage.cpp garage.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main