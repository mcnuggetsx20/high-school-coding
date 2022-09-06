#include <iostream>
#include "list.cpp"
using namespace std;


int main(){
    LIST tab;
    tab.append(9);
    tab.append(100);
    tab.append(214);
    tab.append(483945);
    tab.pop();
    tab.insert(420, 2);
    tab.walk();
}

