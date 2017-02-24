
Item 1: Know Which JavaScript You Are Using

Things to Remember
✦ Decide which versions of JavaScript your application supports.
✦ Be sure that any JavaScript features you use are supported by all
environments where your application runs.
✦ Always test strict code in environments that perform the strict-
mode checks.
✦ Beware  of  concatenating  scripts  that  differ  in  their  expectations
about strict mode.

Item 2: Understand JavaScript’s Floating-Point Numbers


Most programming languages have several types of numeric data, but 
JavaScript gets away with just one. You can see this reflected in the 
behavior  of  the typeof operator,  which  classifies  integers  and  float-
ing-point numbers alike simply as numbers:

typeof 17; // "number"
typeof 98.6; // "number"
typeof -2.1; // "number"

In  fact,  all  numbers  in  JavaScript  are  
double-precision  floating-point
numbers,  that  is,  the  64-bit  encoding  of  numbers  specified  by  the  
IEEE  754  standard—commonly  known  as  “doubles.”



Things to Remember
✦ JavaScript numbers are double-precision floating-point numbers.
✦ Integers in JavaScript are just a subset of doubles rather than a
separate datatype.
✦ Bitwise operators treat numbers as if they were 32-bit signed integers.
✦ Be aware of limitations of precisions in floating-point arithmetic.


Item 3:  Beware of Implicit Coercions 

These coercions can be seductively convenient—for example, for auto-
matically converting strings that come from user input, a text file, or 
a network stream:

"17" * 3; // 51
"8" | "1"; // 9

But  coercions  can  also  hide  errors.  A  variable  that  turns  out  to  be  
null will  not  fail  in  an  arithmetic  calculation,  but  silently  convert  
to  0;  an  undefined variable  will  convert  to  the  special  floating-point  value 
NaN (the  paradoxically  named  “not  a  number”  number—blame  
the IEEE floating-point standard!). Rather than immediately throw-
ing  an  exception,  these  coercions  cause  the  calculation  to  continue  
with  often  confusing  and  unpredictable  results.  Frustratingly,  it’s  
particularly  difficult  even  to  test  for  the  NaN
  value,  for  two  reasons.  

First,  JavaScript  follows  the  IEEE  floating-point  standard’s  head-  
scratching  requirement  that  
NaN be  treated  as  unequal  to  itself.  So  testing whether a value is equal to 
NaN doesn’t work at all:
var x = NaN;
x === NaN;
// false Moreover,  the  standard  isNaN library  function  is  not  very  reliable  
because it comes with its own implicit coercion, converting its argu-
ment to a number before testing the value. (A more accurate name for 
isNaN probably would have been coercesToNaN .)  If  you  already  know  
that a value is a number, you can test it for NaN with isNaN :

isNaN(NaN); // true
But  other  values  that  are  definitely  not  NaN ,  yet  are  nevertheless  
coercible to NaN , are indistinguishable to isNaN :
isNaN("foo"); // true
isNaN(undefined); // true
isNaN({}); // true
isNaN({ valueOf: "foo" }); // true

Luckily  there’s  an  idiom  that  is  both  reliable  and  concise—if  some-
what unintuitive—for testing for NaN . Since NaN is the only JavaScript 
value  that  is  treated  as  unequal  to  itself,  you  can  always  test  if  a  
value is NaN by checking it for equality to itself:
var a = NaN;
a !== a; // true
var b = "foo";
b !== b; // false
JavaScript  follows  the  IEEE  floating-point  standard’s  head-  
scratching  requirement  that  NaN be  treated  as  unequal  to  itself.  So  
testing whether a value is equal to NaN doesn’t work at all:

var x = NaN;
x === NaN; // false
Moreover,  the  standard  isNaN library  function  is  not  very  reliable  
because it comes with its own implicit coercion, converting its argu-
ment to a number before testing the value. (A more accurate name for 
isNaN probably would have been coercesToNaN .)  If  you  already  know  
that a value is a number, you can test it for NaN with isNaN :
isNaN(NaN); // true

But  other  values  that  are  definitely  not  NaN ,  yet  are  nevertheless  
coercible to NaN , are indistinguishable to isNaN :

isNaN("foo"); // true
isNaN(undefined); // true
isNaN({}); // true
isNaN({ valueOf: "foo" }); // true

Luckily  there’s  an  idiom  that  is  both  reliable  and  concise—if  some-
what unintuitive—for testing for NaN . Since NaN is the only JavaScript 
value  that  is  treated  as  unequal  to  itself,  you  can  always  test  if  a  
value is NaN by checking it for equality to itself:

var a = NaN;
a !== a; // true
var b = "foo";
b !== b; // false
var c = undefined;
c !== c; // false
var d = {};
d !== d; // false
var e = { valueOf: "foo" };
e !== e; // false

You  can  also  abstract  this  pattern  into  a  clearly  named  utility  
function:
function
isReallyNaN(x) {
return
 x !== x;
}



Similarly,  objects  can  be  converted  to  numbers  via  their  
valueOf
method.  You  can  control  the  type  conversion  of  objects  by  defining  
these methods:
"J" + { toString: 
function
() { 
return
"S"; } }; 
// "JS"
2 * { valueOf: 
function
() { 
return
3; } };
// 6



The  last  kind  of  coercion  is  sometimes  known  as  
truthiness.




There  are  exactly  
seven 
falsy
 values: 
false
,
0
,
-0
,
""
,
NaN
,
null
, and 
undefined
.



The more precise way to check for 
undefined
 is to use 
typeof
:
function
point(x, y) {
if
 (
typeof
 x === "undefined") {
        x = 320;
    }
if
 (
typeof
 y === "undefined") {
        y = 240;
    }
return
 { x: x, y: y };
}



.
Things to Remember
✦ 
Type errors can be silently hidden by implicit coercions.
✦ 
The 
+
 operator is overloaded to do addition or string concatenation 
depending on its argument types.
✦ 
Objects  are  coerced  to  numbers  via  
valueOf
  and  to  strings  via  
toString
.
✦ 
Objects with 
valueOf
 methods should implement a 
toString
 method 
that provides a string representation of the number produced by 
valueOf
.
✦ 
Use 
typeof
  or  comparison  to  
undefined
  rather  than  truthiness  to  
test for undefined values.

Item 4:   
Prefer Primitives to Object Wrappers

Things to Remember
✦ Object wrappers for primitive types do not have the same behavior 
as their primitive values when compared for equality.
✦ Getting and setting properties on primitives implicitly creates object 
wrappers.
.
Item 5:   Avoid using == with Mixed Types

.Things to Remember
✦ The ==  operator  applies  a  confusing  set  of  implicit  coercions  when  
its arguments are of different types.
✦ Use === to make it clear to your readers that your comparison does 
not involve any implicit coercions.
✦ Use your own explicit coercions when comparing values of different 
types to make your program’s behavior clearer
