function fib(n){
  var a = 0;
  var b = 1;
  var temp = 0;
  var sum = 0;
  while (b < n) {
    if ((b % 2) == 0){
      sum += b
    }
    temp = b;
    b = a+b;
    a = temp;
  }
  return sum
}
console.log(fib(4000000));


