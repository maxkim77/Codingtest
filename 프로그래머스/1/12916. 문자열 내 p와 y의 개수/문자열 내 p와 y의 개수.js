function solution(s){
    // 대소문자 구분 없이 'p'와 'y'의 개수를 비교
    var pCount = s.match(/p/gi); // 'p'의 개수를 찾고
    var yCount = s.match(/y/gi); // 'y'의 개수를 찾습니다.
    // match가 null을 반환할 수 있으므로, null이면 0으로 처리합니다.
    pCount = pCount ? pCount.length : 0;
    yCount = yCount ? yCount.length : 0;
    
    return pCount === yCount; // 두 개수를 비교하여 결과를 반환합니다.
}
