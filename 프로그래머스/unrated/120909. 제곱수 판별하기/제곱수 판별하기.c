#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>  // 이 헤더 파일은 sqrt 함수를 사용하기 위해 필요합니다.

int solution(int n) {
    // 제곱근을 구합니다.
    int sqrt_n = (int) sqrt(n);
    
    // 제곱근을 다시 제곱하여 원래의 수와 비교합니다.
    // 같다면 n은 제곱수이므로 1을 반환하고, 아니라면 2를 반환합니다.
    return (sqrt_n * sqrt_n == n) ? 1 : 2;
}
