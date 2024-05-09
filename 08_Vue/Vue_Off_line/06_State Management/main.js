import { name, age, obj, some } from './sub.js'
import bob, { newName } from './other.js'

console.log(name)
console.log(age)
console.log(some)
obj.introduce()

console.log(bob)
console.log(newName)

// 터미널에서 node main.js 입력하면 출력됨