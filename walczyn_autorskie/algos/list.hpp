#include <iostream>
#include "node.hpp"
using namespace std;

class MyList {
    public:
        int64_t size = 0;
        Node *tail;
        Node *head;
        void append(int n);
        void pop();
};
