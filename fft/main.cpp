#include <fftw3.h>
#include <stdint.h>

using namespace std;

int main(int argc, char* argv[]){
    double in[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    double out[16];
    fftw_plan plan = fftw_plan_r2r_2d(8,2,in,out,FFTW_RODFT00,FFTW_RODFT00,FFTW_ESTIMATE);
    
    fftw_execute(plan);

    fftw_destroy_plan(plan);

    printf("out = ");
    for (uint32_t k=0; k<15; k++){
        printf("%.3f,",out[k]/4);
    }
    printf("%.3f\n",out[15]/4);

    return 0;
}
