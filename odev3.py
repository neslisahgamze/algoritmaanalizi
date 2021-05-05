#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int sayi;
    int i,j;
    srand(time(NULL));
    printf ("sayiyi gir : "); scanf("%d",&sayi);
    int dizi[sayi][100];
    for(i=0;i<sayi;i++){
        for(j=0;j<100;j++){
            dizi[i][j]=rand()%2;
        }
    }

   
    int sayac=0,toplam=0;
    i=0;
    int satir,sutun;
    for(j=0;j<100;j++){
        for(i=0;i<sayi;i++){
            if(dizi[i][j]==1)
                 toplam+=1;
        }
        if(sayac<toplam){
            sayac=toplam;
            sutun=j;
        }

    }

   printf("\nEncok 1 olan sutun %d ve toplam urun  %d: ",sutun,sayac);
    return 0;
}
