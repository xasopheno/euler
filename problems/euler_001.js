function sum3or5(n) {
  var sum = 0;
  for (var i = 0; i < n; i ++) {
    if ((i%3 == 0) || (i%5 == 0)) {
      sum += i
    }
  }

  return sum
}

console.log(sum3or5(1000));
