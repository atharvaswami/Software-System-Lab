function display(){

    var Name=document.getElementById("fname").value;
    var Address=document.getElementById("address").value;
    var Pnum=document.getElementById("pnum").value;
    var Email=document.getElementById("email").value;
    var EQ=document.getElementById("eduquali").value;
    var Age=document.getElementById("age").value;

    var table='';
    for(var r=0;r<6;r++)
    {
        table+='<tr>';
        if(r==0){
            table+='<td>'+"User.Name"+'</td>';
            if(Name!="")
            table+='<td>'+Name+'</td>';
            else
            table+='<td>'+"Enter your Name"+'</td>';
        }
        else if(r==1){
            table+='<td>'+"User.Address"+'</td>';
            if(Address!="")
            table+='<td>'+Address+'</td>';
            else
            table+='<td>'+"Enter your Address"+'</td>';
        }
        else if(r==2){
            table+='<td>'+"User.Phone Number"+'</td>';
            if(Pnum!="")
            table+='<td>'+Pnum+'</td>';
            else
            table+='<td>'+"Enter your Phone Number"+'</td>';
        }
        else if(r==3){
            table+='<td>'+"User.EmailID"+'</td>';
            if(Email!="")
            table+='<td>'+Email+'</td>';
            else
            table+='<td>'+"Enter your EmailID"+'</td>';
        }
        else if(r==4){
            table+='<td>'+"User.Educational Qualifications"+'</td>';
            if(EQ!="")
            table+='<td>'+EQ+'</td>';
            else
            table+='<td>'+"Enter your Educational Qualifications"+'</td>';
        }
        else if(r==5){
            table+='<td>'+"User.Age"+'</td>';
            if(Age!="")
            table+='<td>'+Age+'</td>';
            else
            table+='<td>'+"Enter your Age"+'</td>';
        }
        table+='</tr>';
    }
    /*var div=document.getElementById('User');
    document.write(div.innerHTML+'<br>');*/
    document.write('<br>'+'<table border="2">'+table+'</table>');
}