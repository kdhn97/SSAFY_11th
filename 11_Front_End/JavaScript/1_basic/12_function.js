/**
 * function 함수
 * 
 * 만약 2라는 숫자에 * 10 / 2 % 3 스트링으로 변환해서
 * 반환받고 싶다면 어떻게 해야할까?
 */
console.log((2 * 10 / 2 % 3).toString()); // 1
console.log((3 * 10 / 2 % 3).toString()); // 0

/**
 * DRY
 * D - Don't
 * R - Repeat
 * Y - Yourself
 * 동일한 형식을 중복해서 적지마라
 */
function claculate(n){
  console.log((n * 10 / 2 % 3).toString());
}
claculate(2); // 1
claculate(3); // 0

/**
 * 함수에서 입력받는 값에 대한 정의를 Parameter : n
 * 실제 입력하는 값은 argument : 2
 */