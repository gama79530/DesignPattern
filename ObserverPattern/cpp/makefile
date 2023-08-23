CXX = g++

HEADER_PATH = src/header
SOURCE_PATH = src

all: main clean run

main: main.cpp streamer.o audience.o
	@$(CXX) $^ -o $@

streamer.o: $(SOURCE_PATH)/streamer.cpp $(HEADER_PATH)/streamer.h $(HEADER_PATH)/audience.h
	@$(CXX) $< -c

audience.o: $(SOURCE_PATH)/audience.cpp $(HEADER_PATH)/audience.h
	@$(CXX) $< -c

.PHONY: clean run

clean:
	@-rm -rf *.o *.gch

run:
	@./main