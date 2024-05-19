function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    // 분모 분자 구하기
    let denominator = denom1 * denom2;
    let molecule = numer1 * denom2 + denom1 * numer2;
    // 분모와 분자의 최대공약수 구하기
    function gcd(a, b) {
        return b === 0 ? a : gcd(b , a % b);
    }
    let divisor = gcd(molecule, denominator);
    // 분모 분자를 최대공약수로 나누기 
    molecule /= divisor;
    denominator /= divisor;
    // 반환 값 넣어서 return
    answer = [molecule, denominator];
    return answer;
}