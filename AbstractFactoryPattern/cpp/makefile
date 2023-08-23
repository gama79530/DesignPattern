vpath %.cpp src
vpath %.h src/header

CXX = g++

all: main clean run

main: main.cpp ingredient_factory.o ingredient.o pizza_store.o pizza.o
	@$(CXX) $^ -o $@ 

ingredient_factory.o: ingredient_factory.cpp ingredient_factory.h ingredient.h
	@$(CXX) $< -c

ingredient.o: ingredient.cpp ingredient.h
	@$(CXX) $< -c

pizza_store.o: pizza_store.cpp pizza_store.h ingredient.h
	@$(CXX) $< -c

pizza.o: pizza.cpp pizza.h ingredient.h
	@$(CXX) $< -c

.PHONY: clean run
clean:
	@-rm -rf *.o *.gch

run:
	@./main
