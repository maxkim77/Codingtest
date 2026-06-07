function solution(clothes) {
    let answer = 1;
    const map = new Map();
    
    for (const cloth of clothes) {
        const type = cloth[1];
        map.set(type, (map.get(type) || 0) + 1);
    }
    
    for (const cnt of map.values()) {
        answer *= (cnt + 1);
    }
    
    return answer - 1;
}