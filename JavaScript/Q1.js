function checkAge(f)
{
    var a=f.age.value;
    if(a>=18 && a<=100)
    {
        alert("You are eligible!");
    }
    else if(a=="")
    {
        alert("Please enter your age");
    }
    else
    {
        alert("Sorry,you are not eligible");
    }
}