// 파일로부터 입력 받기
const input = require('fs').readFileSync('input.txt').toString().trim();

for (let N = input; N > 1; N--) {
    console.log(' '.repeat(input-N) + '*'.repeat(N * 2 - 1))
}

for (let N = 1; N <= input; N++) {
    console.log(' '.repeat(input-N) + '*'.repeat(N * 2 - 1))
}