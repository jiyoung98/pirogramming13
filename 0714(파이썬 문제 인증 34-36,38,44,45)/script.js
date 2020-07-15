
// // 1. 변수 선언
// var j;
// const x = 123;
// let y = 3;

// // 2. 조건문
// // a===0 // 같음. ==은 값을 비교, ===는 자료형까지 비교
// // a!==0 // 다름
// // a > 0


// a=0

// if (a>0) {
//   console.log("a is more than b.")
// }
// if (a===0) {
//   console.log("a is b")
// }

// function sayHello() {
//   console.log("hi")
// }

// sayHello();


// //함수 선언의 다른 방식
// const adder = (a,b) => {
//   return a+b;
// }

// console.log(adder(3,4))

// //4. array - 파이썬과 동일

// //5. 반복문

// for(let k=0; k<5; k++) {
//   console.log(k);
// }

// r=0
// while (r<5) {
//   console.log(r)
//   r++; //=r=r+1
// }


// //array.forEach(function)
// const arr = [10,20,30,40,50]

// arr.forEach((value) => {
//   console.log(value);
// })

// //3항 연산자

// const z= 2;
// for (let x=1; x<= 5; x++) {
//   console.log((x===2)? "correct" : "incorect")
// }




// // 1. Code runs as you type: edit message
// let msg = 'hello world'

// // 2. Files import automatically: uncomment this
// // msg = capitalize(msg)

// $('#header')
//   .html(msg)
//   // 3. Smart autocomplete: type .fadeIn('slow')
//   // after .fadeOut('slow')
//   .fadeOut(1000)

// console.log({ myMessage: msg })


//===========================================실습========================================

// querySelector(css 선택태그)하면 해당 객체가 선택됨.
const lastCity = document.querySelector('#four');
lastCity.className = "green";

// querySelectorAll로 해당 태그를 가진 모든 객체의 array가 선택됨.
const elems = document.querySelectorAll('li.red');
elems.forEach(elem => console.log(elem));
elems.forEach(elem => elem.className = 'blue');

const one = document.querySelector('#one');

const textNode = one.firstChild;
textNode.nodeValue = 'Busan';

const input = document.querySelector('#passwordInput');
if (!input.hasAttribute('value')) {
  // value 어트리뷰트를 추가하고 값으로 'hello!'를 설정
  input.setAttribute('value', 'hello!');
}

const makeClickHandler1 = () => {
  return function () {
    const passwordInput = document.querySelector('#passwordInput'); //edit
    const password = passwordInput.value; //edit
    const cityInput = document.querySelector('#cityInput');
    const cityName = cityInput.value;
    console.log(cityName);
    const realPassword = "1234" //edit
    if (password === realPassword) { //edit
      const newElem = document.createElement('li');
      const newText = document.createTextNode(cityName);
      newElem.appendChild(newText);
      const container = document.querySelector('ul');
      container.appendChild(newElem);
    }
  };
}

$cityInput = document.querySelector('.add');
$cityInput.onclick = makeClickHandler1();



const $password = document.querySelector('.password');
const $show = document.querySelector('.show');

const makeClickHandler2 = () => {
  let isShow = true;
  return function () {
    isShow = !isShow;
    $password.setAttribute('type', isShow ? 'text' : 'password');
    $show.innerHTML = isShow ? 'hide' : 'show';
  };
}

$show.onclick = makeClickHandler2();
