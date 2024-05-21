function solution(num, total) {
    var answer = [];
    // 첫번째값 구하기
    // total값에서 num 값을 나누어 중간값을 구하고 num값에서 반을 나누어 내림을해서 빼면 첫번재 값
    const start = Math.ceil(total / num - Math.floor(num / 2));
    //배열에 값넣기
    for(let i=0; i<num; i++){
        answer.push(start + i)
    }
    return answer;
}