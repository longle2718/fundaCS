SRCS=$(shell find $(SRC_DIRS) -name *.cpp)
OBJS=$(subst .cpp,.o,$(SRCS))
TARGET=main.out
CPPFLAGS=-std=c++11

$(TARGET): $(OBJS)
	g++ $(CPPFLAGS) -o $(TARGET) $(OBJS) -lfftw3
%.o: %.cpp
	g++ $(CPPFLAGS) -c $< -o $@
clean:
	rm $(TARGET) $(OBJS)
