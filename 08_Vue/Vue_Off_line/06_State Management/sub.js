const name = 'Alice'
const age = 23
const obj = {
    name,
    age,
    introduce() {
        console.log(`My name is ${this.name}`)
        console.log(`and I am ${this.age} year old`);
    }
}

export const some = '정의'
export { name, age, obj }