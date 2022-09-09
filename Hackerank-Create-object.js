/*Objective

In this challenge, we practice creating objects. Check out the attached tutorial for more details.

Task

Complete the function in the editor. It has two parameters:  and . It must return an object modeling a rectangle that has the following properties:

length: This value is equal to .a
width: This value is equal to .b
perimeter: This value is equal to 2*(a+b
area: This value is equal to a.b
Note: The names of the object's properties must be spelled correctly to pass this challenge.

Input Format

The first line contains an integer denoting .
The second line contains an integer denoting .

Constraints

Output Format

Return a object that has the properties specified above. Locked code in the editor prints the returned object's length,width ,perimeter , and area to STDOUT.

Sample Input 0

4
5
Sample Output 0

4
5
18
20*/

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    let r = 
    {
         length : a,
         width : b,
         perimeter : 2*(a+b),
         area : a*b,
    };
    return r;
}


function main() {
    const a = +(readLine());
    const b = +(readLine());
    
    const rec = new Rectangle(a, b);
    
    console.log(rec.length);
    console.log(rec.width);
    console.log(rec.perimeter);
    console.log(rec.area);
}
