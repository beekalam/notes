### count elements of an array

    // count elements of an array
    function array_count(arr, value){
        let ret = 0;
        for(let i = 0; i < arr.length; ++i){
            if (arr[i] === value){
                ret++;
            }
        }
        return ret;
    }

### sort array numerically

By default the sort method sorts elements alphabetically.

    [2,3,0,1].sort(function(a, b) { return a - b; });

### convert set to array

    Array.from(new Set([1,2,3]))

## iterates through the elements of the array using a for... in

    var theArray = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
    var total1 = 0, total2 = 0;
    
    // statement to add each element's value to total2
    for ( var element in theArray )
        total2 += theArray[ element ];
    console.log( "Total using subscripts: " + total1 );

### Count the number of occurences of a character in a string in Javascript

    console.log(("str1,str2,str3,str4".match(/,/g) || []).length); //logs 3
    console.log(("str1,str2,str3,str4".match(new RegExp("str", "g")) || []).length); //logs 4

    function str_count(str, char){
        return (str.match(new RegExp(char, "g")) || []).length;
    }

### name of current function?

You should be able to get it by using arguments.callee.

You may have to parse out the name though, as it will probably include some extra junk. 
Though, in some implementations you can simply get the name using arguments.callee.name.

Parsing:

    function DisplayMyName() 
    {
       var myName = arguments.callee.toString();
       myName = myName.substr('function '.length);
       myName = myName.substr(0, myName.indexOf('('));

       alert(myName);
    }


    var fn = arguments.callee.toString().match(/function\s+([^\s\(]+)/);
    alert(fn[1]);
    For the caller, just use caller.toString().

### generate random numbers between 1 and 6

    Math.floor( 1 + Math.random() * 6)

### Checking for an Existing, Nonempty String

    if (((typeof unknownVariable != 'undefined' && unknownVariable) &&
    unknownVariable.length() > 0) &&
    typeof unknownVariable.valueOf() == 'string') ...

### Finding and Highlighting All Instances of a Pattern

    var searchString = "Now is the time and this is the time and that is the time";
    var pattern = /t\w*e/g;
    var matchArray;

    var str = "";

    // check for pattern with regexp exec, if not null, process
    while((matchArray = pattern.exec(searchString)) != null) {
      str+="at " + matchArray.index + " we found " + matchArray[0] + "\n";
    }
    console.log(str);

The results are:

    at 7 we found the
    at 11 we found time
    at 28 we found the
    at 32 we found time
    at 49 we found the
    at 53 we found time


### Searching Through an Array


Use the Array methods indexOf() and lastIndexOf():

var animals = new Array("dog","cat","seal","elephant","walrus","lion");
console.log(animals.indexOf("elephant")); // prints 3

Flattening a Two-Dimensional Array with concat() and apply()

Use the Array object concat() method to merge the multidimensional array into a single-dimensional array:

var fruitarray = [];
fruitarray[0] = ['strawberry','orange'];
fruitarray[1] = ['lime','peach','banana'];
fruitarray[2] = ['tangerine','apricot'];
fruitarray[3] = ['raspberry','kiwi'];

// flatten array
var newArray = fruitarray.concat.apply([],fruitarray);
console.log(newArray[5]); // tangerine

Removing or Replacing Array Elements

You want to find occurrences of a given value in an array, and either remove the element or replace with another value.

Use the Array indexOf() and splice() to find and remove/replace array elements:

var animals = new Array("dog","cat","seal","walrus","lion", "cat");

// remove the element from array
animals.splice(animals.indexOf("walrus"),1); // dog,cat,seal,lion,cat

// splice in new element
animals.splice(animals.lastIndexOf("cat"),1,"monkey");

// dog,cat,seal,lion,monkey
console.log(animals.toString());


### Extracting a Portion of an Array


The Array slice() method extracts a shallow copy of a portion of an existing array:

var animals = ['elephant','tiger','lion','zebra','cat','dog','rabbit','goose'];

var domestic = animals.slice(4,7);

console.log(domestic); // ['cat','dog','rabbit'];

Applying a Function Against Each Array Element

Use the Array method forEach() to apply a callback function to each array element:

var charSets = ["ab","bb","cd","ab","cc","ab","dd","ab"];

function replaceElement(element,index,array) {
  if (element == "ab") array[index] = "**";
}

// apply function to each array element
charSets.forEach(replaceElement);
console.log(charSets); // ["**", "bb", "cd", "**", "cc", "**", "dd", "**"]



### Traversing the Results from querySelectorAll() with forEach() and call()

You want to use forEach() on the nodeList returned from a call to querySelectorAll().

ou can coerce forEach() into working with a NodeList (the collection returned by querySelectorAll()) 
using the following:

// use querySelector to find all second table cells
var cells = document.querySelectorAll("td + td");

[].forEach.call(cells,function(cell) {
      sum+=parseFloat(cell.firstChild.data);
   });

### Applying a Function to Every Element in an Array and Returning a New Array

you want to convert an array of decimal numbers into a new array with their hexadecimal equivalents.

Use the Array map() method to create a new array consisting of elements from the old array that have been 
modified via a callback function passed to the method:

    var decArray = [23, 255, 122, 5, 16, 99];

    var hexArray = decArray.map(function(element) {
      return element.toString(16);
    });
        
    console.log(hexArray); // ["17", "ff", "7a", "5", "10", "63"]

### Creating a Filtered Array

You want to filter element values in an array and assign the results to a new array.

Use the Array filter() method:

    var charSet = ["**","bb","cd","**","cc","**","dd","**"];

    var newArray = charSet.filter(function(element) {
      return (element !== "**");
    });

    console.log(newArray); // ["bb", "cd", "cc", "dd"]


### Validating Array Contents

Problem

You want to ensure that array contents meet certain criteria.


Use the Array every() method to check that every element passes a given criterion. For instance, the following code checks to ensure that every element in the array consists of alphabetical characters:

    // testing function
    function testValue (element,index,array) {
      var textExp = /^[a-zA-Z]+$/;
      return textExp.test(element);
    }

    var elemSet = ["**",123,"aaa","abc","-",46,"AAA"];


    // run test
    var result = elemSet.every(testValue);

    console.log(result); // false

    var elemSet2 = ["elephant","lion","cat","dog"];

    result = elemSet2.every(testValue);

    console.log(result); // true

Or use the Array some() method to ensure that one or more of the elements pass the criteria. As an example, the following code checks to ensure that at least some of the array elements are alphabetical strings:

    var elemSet = new Array("**",123,"aaa","abc","-",46,"AAA");

    // testing function
    function testValue (element) {
       var textExp = /^[a-zA-Z]+$/;
       return textExp.test(element);
    }

    // run test
    var result = elemSet.some(testValue);

    console.log(result); // true

### Using a Destructuring Assignment to Simplify Code

You want to assign array element values to several variables, but you really don’t want to have assign each, individually.

Use ECMAScript 6’s destructuring assignment to simplify array assignment:

var stateValues = [459, 144, 96, 34, 0, 14];

var [Arizona, Missouri, Idaho, Nebraska, Texas, Minnesota] = stateValues;

console.log(Missouri); // 144

Converting Function Arguments into an Array

Use Array.prototype.slice() and then the function call() method to convert the arguments collection into an array:

function someFunc() {
   var args = Array.prototype.slice.call(arguments);
   ...
}

Or, here’s a simpler approach:

function someFunc() {
   var args = [].slice.call(arguments);
}

function sumRounds() {
  var args = [].slice.call(arguments);

  return args.reduce(function(val1,val2) {
    return parseInt(val1,10) + parseInt(val2,10);
  });
}

var sum = sumRounds("2.3", 4, 5, "16", 18.1);

console.log(sum); // 45

