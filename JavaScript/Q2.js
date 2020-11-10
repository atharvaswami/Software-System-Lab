function check(f1) {
    var pstr = f1.palindrome.value;
    var cstr = pstr.toLowerCase().replace(/[^a-zA-Z0-9]+/g, '');

    if (cstr === "") {
        alert("Please enter a string.");
        return false;
    }
    if ((cstr.length) % 2 === 0) {
        ccount = (cstr.length) / 2;
    }
    else {
        if (cstr.length === 1) {
            alert("Entry is a palindrome.");
            return true;
        }
        else {
            ccount = (cstr.length - 1) / 2;
        }
    }
    for (var x = 0; x < ccount; x++) {
        if (cstr[x] != cstr.slice(-1 - x)[0]) {
            alert("Entry is not a palindrome.");
            return false;
        }
    }
    alert("Entry is a palindrome.");
    return true;
}

function calculate(f2) {
    n1 = f2.num1.value;
    n2 = f2.num2.value;

    if(n1=="" || n2=="")
    {
        alert("Please enter 2 numbers.");
        return;
    }
    x = Math.abs(n1);
    y = Math.abs(n2);
    while (y) {
        var t = y;
        y = x % y;
        x = t;
    }
    alert("GCD of "+n1+" and "+n2+" is "+x);

}

function printseq(f3) {
    var num = f3.fibonacci.value;
    if(num=="")
    {
        alert("Please enter a number.");
        return;
    }
    if(num==1)
    {
        alert(0);
        return;
    }
    else
    {
        var num1=0; 
    var num2=1; 
    var sum; 
    var i=0; 
    var l=[0, 1];
    for (i = 0; i < num-2; i++)  
    { 
        sum=num1+num2; 
        num1=num2; 
        num2=sum; 
        l.push(num2);
    } 
    alert(l); 
    }
}