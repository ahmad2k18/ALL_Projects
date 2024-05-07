// object defination 
let std_obj = {
    firstname : 'ahmad',
    lastname : 'hassan',
    age : 23,
    address : 'karachi',
    phone : +923117497715,
    email : 'ahmad@gmail.com',

}
console.log(std_obj)

// acess way 1
console.log(std_obj['firstname']);

// acess way 2

console.log(std_obj.firstname);

// add new record

std_obj['email'] = 'ahmadbutt@gmail.com';
console.log(std_obj);

// for loop

for (let i = 0; i < 10; i++) {
    console.log("Ahmad");
}

// while loop

let i = 0;
while (i < 10) {
     i++;
console.log("Ahmad");
    
}


// do while loop

let j = 1;
do {
    j++;
    console.log("Ahmad");
}

while (j <= 10);

// for in loop

for (let key in std_obj) {
    console.log(key);
    console.log(std_obj[key]);
}

// for of loop


// for (let key of std_obj) {
//     console.log(key);
//     console.log(std_obj[key]);
// }

// task 1 assume  a array list anf they all elements sum using a loop

let arr = [1,2,3,4,5,6,7,8,9,10];
let sum = 0;
for (let i = 0; i < arr.length; i++){
    sum = sum + arr[i];
    console.log(sum);   
}

// reverse itreations

for (let i = arr.length - 1; i >= 0; i--) {
    console.log(arr[i]);
}



