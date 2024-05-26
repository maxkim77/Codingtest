function solution(array) {
    //배열을 오름차순으로 정렬
    array.sort((a,b) => a - b);
    
    //배열에서 중앙인덱스 설정
    const middle = Math.floor(array.length / 2);
    // 중앙인덱스값 반환
    
    return array[middle];
}