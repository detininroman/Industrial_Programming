                                                                                                                                #include <stdio.h>
                                                                                                                                #include <stdlib.h>
                                                                                                                                    #include <time.h>
                                                                                                                                        #define HELLO
        HELLO

                                                                                                                                        #define shamsi 																		int
                                                                                                                                #define KPM 																		void
                                                                                                                                    #define NOTHING

 
                                                                                                                                void shamilv05(shamsi *acronis, int kek, int lol){if (kek < lol){
                                                                                                                                shamsi azaza = kek, FRTK = lol, middle = acronis[(azaza + FRTK) / 2];
        do NOTHING
                                                                                                                                    {while (acronis[azaza] < middle) azaza++;while (acronis[FRTK] > middle) FRTK--;if (azaza <= FRTK){shamsi tmp = acronis[azaza];acronis[azaza] = acronis[FRTK]; acronis[FRTK] = tmp;azaza++;FRTK--;}} while (azaza <= FRTK);shamilv05(acronis, kek, FRTK);shamilv05(acronis, azaza, lol);}}

                                                                                                                                    shamsi main(){
                                                                                                                                shamsi n = 10;shamsi* crew_332 = (int*)calloc(n, sizeof(int));srand(time(NULL));for(shamsi i = 0; i < n; i++) crew_332[i] = rand() % 100;for(shamsi i = 0; i < n; i++) printf("%d ", crew_332[i]);printf("\n");shamilv05(crew_332, 0, n - 1);for(shamsi i = 0; i < n; i++)printf("%d ", crew_332[i]);free(crew_332);
                                                                                                                                                return 0;}