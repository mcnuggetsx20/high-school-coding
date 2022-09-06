//#include <bits/stdc++.h>
#include <iostream>
#include "list.hpp"

using namespace std;

void LIST::append(int n){
    //cout << "Called 'APPEND' with: " << n << '\n';
    Node *current;
    current = new Node;
    current -> val = n;
    current -> next = nullptr;

    this -> tail -> next = current;
    this -> tail = current;

    if(not (this -> size)){
        //cout << "Size: " << this -> size << '\n';
        this -> head = current;
    }
    ++this -> size;
}

void LIST::pop(){
    if(not (this -> size)){return;}

    delete this -> tail;
    --this -> size;

    if(not (this -> size)){return;}

    Node *now;
    now = this -> head;

    while(1){
        if(now -> next == this -> tail){
            this -> tail = now;
            this -> tail -> next = nullptr;
            now = NULL;
            break;
        }
        now = now -> next;
    }
}

void LIST::insert(int n, int ind){
    if(ind >= this -> size){return;}

    Node *current;
    current = new Node;
    current -> val = n;
    
    Node *now;
    now = this -> head;
    int c = 0;

    while(1){
        if(c == ind-1){
            current -> next = now -> next;
            now -> next = current;
            break;
        }
        now = now -> next;
        c++;
    }
    ++this ->size;
}

void LIST::walk(){
    if( not (this -> size)){
        return;
    }
    Node *now;
    now = this -> head;
    while(1){
        cout << now -> val << '\n';
        if(now == this -> tail){
            return;
        }
        now = now -> next;
    }
}




