const [N, M] = require('fs').readFileSync('input.txt', 'utf8').trim().split(' ').map(Number);

day = 0

if (N == 1){
    day = M
}else if (N == 2){
    day = 31+M
}else if (N == 3){
    day = 59+M
}else if (N == 4){
    day = 90+M
}else if (N == 5){
    day = 120+M
}else if (N == 6){
    day = 151+M
}else if (N == 7){
    day = 181+M
}else if (N == 8){
    day = 212+M
}else if (N == 9){
    day = 243+M
}else if (N == 10){
    day = 273+M
}else if (N == 11){
    day = 304+M
}else if (N == 12){
    day = 334+M
}    

week = day % 7

if (week == 0){
    console.log('SUN')
}else if (week == 1){
    console.log('MON')
}else if (week == 2){
    console.log('TUE')
}else if (week == 3){
    console.log('WED')
}else if (week == 4){
    console.log('THU')
}else if (week == 5){
    console.log('FRI')
}else if (week == 6){
    console.log('SAT')
}

