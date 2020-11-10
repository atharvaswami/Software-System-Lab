function mostfreq(f)
{
    var istr=f.freq.value;
    if(istr=="")
    {
        alert("Please enter a string.");
        return;
    }
    var str = istr.toLowerCase().replace(/[^a-zA-Z0-9]+/g, '');
    var expCounts = {};
    var maxKey = '';
    for(var i = 0; i < str.length; i++)
    {
        var key = str[i];
        if(!expCounts[key])
        {
        expCounts[key] = 0;
        }
        expCounts[key]++;
        if(maxKey == '' || expCounts[key] > expCounts[maxKey])
        {
            maxKey = key;
        }
    }
    alert("Most Frequent character: "+maxKey+"\nNumber of occurrences: "+expCounts[maxKey]);
}