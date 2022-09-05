//#include <bits/stdc++.h>
#include <iostream>
#include "list.hpp"

using namespace std;

void MyList::append(int n){
    Node *current;
    head -> val = n;
    if(this -> size != 0){
        this -> tail = current;
        return;
    }
    current -> next = nullptr

}




