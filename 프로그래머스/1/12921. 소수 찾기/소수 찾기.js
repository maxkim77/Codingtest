function solution(n) {
    // 에라토스테네스의 체를 사용하여 소수를 찾습니다.
    const primes = new Array(n + 1).fill(true);
    primes[0] = false;
    primes[1] = false;
    for (let i = 2; i * i <= n; i++) {
        if (primes[i]) {
            for (let j = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }
    
    // 소수의 개수를 세어 반환합니다.
    return primes.filter(prime => prime).length;
}
