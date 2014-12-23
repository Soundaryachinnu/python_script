import hello
# hello.print_func("test");

arg1 = raw_input('Enter the first number :');
arg2 = raw_input('Enter the second number :');

# v1 = hello.mathfunc(arg1);
# v2 = hello.mathfunc(arg2);
# v1.funcadd(float(arg2));
# v1.funcsub(float(arg2));
# v1.funcmultiply(float(arg2));
# v1.funcdivide(float(arg2));
v1 = hello.mathfunc(arg1,arg2);
v1.funcadd();
v1.funcsub();
v1.funcmultiply();
v1.funcdivide();
# print v1 + v2;
# print v1 - v2;
# print v1 * v2;
# print v1 / v2;




