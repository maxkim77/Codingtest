function solution(money) {
    var answer = [];
    coffeeMoney = 5500;
    cups = Math.floor(money / coffeeMoney);
    remain = money % coffeeMoney;
    answer = [cups, remain];
    return answer;
}