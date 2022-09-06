#include <iostream>
#include "node.hpp"
using namespace std;

class LIST {
    public:
        int64_t size = 0;
        Node *tail;
        Node *head;
        void append(int n);
        void pop();
        void walk();
        void insert(int n, int ind);
};
