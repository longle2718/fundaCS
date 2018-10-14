# Use <CTRL-V><Tab> in insert mode to insert tabs
HEADER = $(wildcard *.hpp) $(wildcard *.h)
SRC = $(wildcard *.cpp)
OBJ = $(patsubst %.cpp, %.o, $(SRC))
TARGET = main.out
CFLAGS = -std=c++11

$(TARGET): $(OBJ) $(HEADER)
	g++ $(CFLAGS) $(OBJ) -lfftw3 -o $@
%.o: %.cpp 
	g++ $(CFLAGS) -c $< -o $@
clean:
	rm -f $(TARGET) $(OBJ)
