// Currying is the process of transforming a function that takes multiple arguments into a sequence of functions, each taking one argument.

// a closure is a function that "closes over" its surrounding state—it retains access to the variables in its scope even after the outer function has returned.

function main() {
  outer = 23;
  console.log("outer function");

  return (a, b) => {
    console.log("Inner function", a, b);
    console.log("outer scoped variable", ++outer);
    return outer * a * b;
  };
}
inner = main();
console.log(inner(2, 3));
