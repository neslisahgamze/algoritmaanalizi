#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(int argc, char *argv[])
{
    int i, j,n;

    printf("satir sayisi giriniz: ");
    scanf("%d", &n);
    int dizi[n][10];
    srand(time(NULL));
    for(i=0; i<n; i++){
             for(j=0; j<10; j++){
                      
                      dizi[i][j]=rand()%2;
                      printf("%d\t", dizi[i][j]);
                      }
             printf("\n");
             }
int toplam = 0;
int yeniDizi[10];
for(i = 0; i<10; i++){
      for(j = 0; j<n; j++){
          if(dizi[j][i] == 1){
                        toplam = toplam +1;
          }     
      }
      yeniDizi[i] = toplam;
      toplam = 0;
}            


for(i = 0; i<10 ; i++){
      printf("%d. urun :%d \n" ,i, yeniDizi[i]);      
}
  
    
  
  system("PAUSE");	
  return 0;
  }
