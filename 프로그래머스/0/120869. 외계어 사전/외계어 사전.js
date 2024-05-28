function solution(spell, dic) {
    var answer = 0;
    const spellSorted = spell.sort().join('');
    const dicSorted = dic.map(word => word.split('').sort().join(''));
    
    return dicSorted.includes(spellSorted) ? 1:2;
}