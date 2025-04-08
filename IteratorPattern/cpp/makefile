vpath %.cpp src
vpath %.h header

CXX = g++

all: main clean run

main: main.cpp vehicle.o garage.h
	@$(CXX) $^ -Iheader -o $@

vehicle.o: vehicle.cpp vehicle.h
	@$(CXX) $< -I./header -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main