# TypeScript Interface

> Object type 으로 객체를 생성해 보자.
>
> ```ts
> let user:object;
> user = {
>  name: 'xx',
>  age: 30
> }
> 
> console.log(user.name); // 오류발생
> ```
>
> object type 에는 name 이라는 property가 존재하지 않기 때문에 오류가 발생한다. 
>
> 이처럼 property 를 정의하여 객체를 표현하고자 할때는 ***<u>Interface</u>*** 를 사용한다. 
>
> ```ts
> interface User {
>  name: string;
>  age: number;
> }
> let user: User = {
>  name: 'xx',
>  age: 30
> }
> 
> user.age = 10;
> user.gender = 'male' // 에러 발생 <= gender 라는 property 를 user 는 가지고 있지 않다. 
> ```
>
> 
>
> property 이름 뒤에 `?` 를 붙이면 property를 ***<u>optional 로 설정</u>***할 수 있다.
>
> property 이름 앞에 ***<u>`readonly`</u>*** 를 작성하는 경우 해당 property를 수정불가능한 property로 설정할 수 있다. 
>
> [`property_name`: `type1`] : `type1` 구조로 작성하는 경우 인덱스 시그니처(Index Signature) 속성을 사용할 수 있다. 
>
> ```ts
> type Score = 'A' | 'B' | 'C' | 'F';
> interface User {
>  name: string;
>  age: number;
>  gender?: string;
>  readonly birthYear: number;
>  [grade: number] : Score; // 1:'A' 구조로 생성이 가능하다. 단 값에는 위에서 정의한 Score type 대로 'A'/'B'/'C'/'F' 만이 가능하다. 
> }
> let user: User = {
>  name: 'xx',
>  age: 30,
>  birthYear: 2000,
>  1: 'A',
>  2: 'B',
>  3: 'C'
> }
> //gender 는 optional property 이기 때문에 따로 값을 주지 않아도 오류가 발생하지 않는다.
> 
> user.age = 10;
> user.gender = 'male' 
> user.birthYear = 2000 // 오류발생 <= birthYear 은 readonly property 으로 설정하였으나 값을 수정하려 하였기에 오류가 발생한다.  
> ```
>
> js 로 컴파일된 결과를 보면 interface 구문을 사용하지 않고 user 객체가 생성되는 것을 확인할 수 있다. 
>
> 
>
> Interface 로는 함수의 정의또한 가능하다.
>
> 인터페이스를 함수 타입에 설정할 경우 별도의 매개변수, 리턴 값 설정을 생략한다. 
>
> ```ts
> interface Add {
>  (num1: number, num2: number): number;
> }
> const add : Add = function (x, y){
>  return x + y;
> }
> 
> console.log(add(10,1))
> ```
>
> 인터페이스 내부에서는 `num1` 과 `num2` 로 정의하였지만
>
> 함수를 정의할 때는 다른 parameter 명을 사용해도 무방하다.  
>
> 마찬가지로 컴파일시
>
> ```js
> const add = function (x, y) {
>  return x + y;
> };
> console.log(add(10, 1));
> 
> ```
>
> interface 구문 없이 정의되는 것을 확인할 수 있다. 
>
> ```ts
> interface IsAdult {
>  (age: number): boolean
> }
> 
> const a: IsAdult = (age) => {
>  return age > 19;
> }
> ```
>
> 
>
> interface 로 class 를 정의할 수도 있다.
>
> ```ts
> interface Car {
> 	color: string;
>  wheels: number;
>  start(): void;
> }
> 
> class Bmw implements Car {
>  color;
>  wheels = 4;
>  constructor(c:string){
>      this.color = c
>  }
>  start(){
>      console.log('go..');
>  }
> }
> 
> const b = new Bmw('green');
> console.log(b);
> b.start();
> ```
>
> 
>
> extend 또한 가능하다. 
>
> ```ts
> interface Car {
> 	color: string;
>  wheels: number;
>  start(): void;
> }
> 
> interface Benz extends Car {
>  door: number;
>  stop(): void;
> }
> 
> // 오류발생 <= Car 의 속성까지 모두 입력해 주어야 한다. 
> // class benz implements Benz {
> //     door: 5;
> //     stop(){
> //         console.log('stop');
> //     }
> // }
> class benz implements Benz {
>  color;
>  wheels = 4;
>  constructor(c:string){
>      this.color = c
>  }
>  start(){
>      console.log('go..');
>  };
>  door: 5;
>  stop(){
>      console.log('stop');
>  }
> }
> 
> ```
>
> 
>
> 여러개의 interface 를 통한 extend 도 가능하다. 
>
> ```ts
> interface Car {
> 	color: string;
>  	wheels: number;
>  	start(): void;
> }
> 
> interface Toy {
> 	 name: string;
> }
> 
> interface ToyCar extends Car, Toy {
> 	 price : number
> }
> ```

















