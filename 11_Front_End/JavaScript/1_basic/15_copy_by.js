/**
 * copy by value 값에 의한 전달
 * copy by reference 참조에 의한 전달
 * 
 * 1) 기본적으로 모든 primitive 값은 copy by value이다
 * 2) 객체는 copy by reference이다
 */
let original = '안녕하세요';
let clone = original;
console.log(original); // 안녕하세요
console.log(clone); // 안녕하세요

clone += ' 안유진 입니다';
console.log(original); // 안녕하세요
console.log(clone); // 안녕하세요 안유진 입니다

let originalObj = {
  name: '안유진',
  group: '아이브',
};
let cloneObj = originalObj;
console.log(originalObj); // { name: '안유진', group: '아이브' }
console.log(cloneObj); // { name: '안유진', group: '아이브' }

originalObj['group'] = '코드팩토리';
console.log(originalObj); // { name: '안유진', group: '코드팩토리' }
console.log(cloneObj); // { name: '안유진', group: '코드팩토리' }

console.log(original === clone); // false
console.log(originalObj === cloneObj); // true

originalObj = {
  name: '최지호',
  group: '코드팩토리',
};
console.log(originalObj === cloneObj); // false

/**
 * [ Copy by Value ]
 * 
 * original 0X000001 -> 안녕하세요
 * clone    0X000003 -> 안녕하세요 + 안유진 입니다
 */

/**
 * [ Copy by Reference ]
 * 
 * originalObj 0X000001 -> 0X000003
 * cloneObj    0X000002 -> 0X000003
 * 
 * 0X000003 ->
 * let originalObj = {
    name: '안유진',  -> 값을 변경 시
    group: '아이브', -> originalObj과 cloneObj 모두 변경
  };
 */

  // 3:56