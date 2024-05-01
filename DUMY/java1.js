// // Print 
// alert('how are you')
// console.log("Azad Chaiwala Institute");
// document.write('Ahmad Butt')

// // Keywords 
// var m = 'Ahmad';
//  id = 10;
//  console.log(id)

//  // Display Message
//  alert('Ahmad')
//  confirm("Do you want exit");
//  prompt("Enter Your Name");

//  // Variables
// let x = 10
// var z = 'Umer';
// console.log(z);
// let _a =2;



// let msg = "This is a message";

// // Multiple Variables
// let q = 1 , w = "hassan";
// console.log(q,w);


let p = 23;
p = 45;
console.log(p);


const _p = 22;
console.log(_p);

let t =4;
v = 3;
r =t-v
console.log(r);

let zz =5;
xy =5
console.log(zz*xy);

let divi =10;
dd =2;
console.log(divi/dd);

let reminder = 10 % 3;
console.log(reminder);


//sum 
let num1 = 25;
let num2 = 5;
rt = num1+num2;
console.log(rt);

//subtract
let zzz = 25;
let xxx = 20;
nt = zzz-xxx;
console.log(nt);

//divide
let yyy = 30;
let aaa = 3;
ut = yyy/aaa;
console.log(ut);

//multiply
let sss = 44;
let fff = 44;
yt = sss*fff;
console.log(yt);

let rem = 20 % 3;
console.log(rem)

// program

let n = 10;
let g = 5;
console.log(n >= g);

let h = 20;
let e = 40;
console.log(h<=e);

let tt = 20;
let rr = 30;
console.log(tt != rr);


// check numbers
function check_number(a,b){
    if  (a>b) {
        console.log("First value is largest" + a)
    }
    else if (a<b) {
        console.log("Second value is largest" + b)
    }
    else {
        console.log("Both are equal"+ a + ',' +b)
    }
}
check_number(50,40);
check_number(44,44);
check_number(30,45);

// Arrow Function

function mul (a,b) {
    console.log(a*b);
}
mul (4,5);

let abc = num => num*num
let result = abc(5)

console.log(result);

const add = (a,b) => a+b;
console.log(add(2,3));

//example

const sub = (a,b) => a-b;
console.log (sub(4,2));

const multi = (a,b) => a*b;
console.log (multi(4,2));

const div = (a,b) => a/b;
console.log (div(4,8));

const per = (a,b) => a % b;
console.log (per(4,2));