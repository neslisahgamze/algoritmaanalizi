//
//  main.cpp
//  algoritmaanalizi
//
//  Created by neslisah on 10.05.2016.
//  Copyright © 2016 neslisah. All rights reserved.
//
#include <iostream>

using namespace std;

class myClass{
public:
    char a[7];
    char b[7];
    char c[7];

    void sayiKontrol(int);
    int sayiArttir(int);
};
void myClass::sayiKontrol(int sayi){
    
    if (sayi < 256){
        int i;
        int gecici;
        
            for (i=0; i < 8; i++) {
                if(sayi != 0) {
                    gecici= sayi % 2;
                    c[i] = gecici;
                    std::cout<<"c["<<i<<"]"<<"="<<gecici;
                    sayi= sayi /2;
        
            }
        }

    }
   if (sayi >255 && sayi < 65536 ){
       int i;
       int gecici;
       
       for (i=0; i <16; i++) {
           if (i<8  && sayi!=0){
           
            gecici= sayi % 2;
            c[i] = gecici;
            std::cout<<"c["<<i<<"]"<<"="<<gecici;
            sayi= sayi /2;
           }
           else {
                gecici=sayi%2;
                b[i] = gecici;
                sayi= sayi / 2;
                std::cout<<"b["<<i<<"]"<<"="<<gecici;
           }
           
    }
    if (sayi > 65535 && sayi <  16777216) {
        int i;
        int gecici;
        for (i=0; i <24; i++) {
            if (i<8  && sayi!=0){
                
                gecici= sayi % 2;
                c[i] = gecici;
                std::cout<<"c["<<i<<"]"<<"="<<gecici;
                sayi= sayi /2;
            }
            else if(i>7 && i<16 && sayi!=0){
                gecici=sayi%2;
                b[i] = gecici;
                sayi= sayi / 2;
                std::cout<<"b["<<i<<"]"<<"="<<gecici;
            }
            else;
                 gecici=sayi%2;
                 a[i] = gecici;
                 sayi= sayi / 2;
                 std::cout<<"a["<<i<<"]"<<"="<<gecici;
                 }
            
        }
   }

   if (sayi > 16777215 || sayi < 0) {
        std::cout<<"Sayı boyutu hesaplanamaz"<<std::endl;
    }
}
int myClass::sayiArttir(int sayi){
    if (sayi < 0 || sayi > 16777215) {
        std::cout<<"Sayı boyutu arttırılamaz"<<std::endl;
    }
    sayi=sayi+1;
    return sayi;
}

    int main(int argc, const char * argv[]) {
        
        myClass sayi;
        int n;
        std::cout<< "Bir sayi giriniz:"<<std::endl;
        std::cin >> n;
        std::cout<< "Sayı arttır :"<<sayi.sayiArttir(n)<<std::endl;
        sayi.sayiKontrol(n);

    

        return 0;
    
}
