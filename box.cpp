#include <iostream>
#include "bits\stdc++.h"

using namespace std;


class Box {
    int l;    
    int b;    
    int h;

    public:
    Box() : l(0), b(0), h(0) {};
    Box(int Length, int Breadth, int Height) : l(Length), b(Breadth), h(Height){};
    Box(const Box& oldBox) : l(oldBox.l), b(oldBox.b), h(oldBox.b){};
    
    // Box(int l, int b, int h) {l=l; b=b; h=h;};
    // Box(Box) {l=0; b=0; h=0};

    int getLength() {return l;} // Return box's length
    int getBreadth () {return b;} // Return box's breadth
    int getHeight () {return h;}  //Return box's height
    long long CalculateVolume() {return l*b*h;} // Return the volume of the box
    
    bool operator < (Box& right_box) {
        if (l < right_box.l){
            return true;
        } else if (l == right_box.l && b < right_box.b){
            return true;
        } else if (h < right_box.h && l == right_box.l && b == right_box.b){
            return true;
        }
        else {
            return false;
        }  
    }

    ostream& operator<<(ostream& out, const Box& box){

    } 
};

int main(){
    Box b1; 
    Box b2(2, 3, 4); 

    b2.getLength();	
    b2.getBreadth(); 
    b2.getHeight();	

    b2.CalculateVolume(); 
    bool x = (b1 < b2);	

    cout << x;




    return 0;
}