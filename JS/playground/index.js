// console.log(getName) 
// console.log(x) // 7

// let x = 7
// a()
// b()
// console.log(x) // 7

// function a(){
//     var x = 42
//     console.log(x) // 42
//     scam()
//     function scam(){
//         console.log(x) // 42
//     }
// }

// function b(){
//     // var x = 67
//     console.log(x) // 67
// }

// function bom(){
//     var x = 67
//     console.log(x) // 67
// }


function a(){
    var b = 42
    console.log(b) // 42
    console.log(x) // 42
}

function b(){
   a()
   x=7
   console.log(x) // 7
}

b();
x=13
console.log(x) // 13