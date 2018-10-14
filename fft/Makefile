# Use <CTRL-V><Tab> in insert mode to insert tabs
HEADER = $(wildcard *.h)
SRC = $(wildcard *.cpp)
OBJ = $(patsubst %.cpp, %.o, $(SRC))
TARGET = main.out
CFLAGS = -std=c++11

$(TARGET): $(OBJ)
	g++ $(CFLAGS) $(OBJ) -lfftw3 -o $@
$(OBJ): $(SRC) $(HEADER)
	g++ $(CFLAGS) -c $< -o $@
clean:
	rm $(TARGET) $(OBJ)
