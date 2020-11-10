<?php

    
    $username = "eval";
    $password = "eva";

    if(isset($_SESSION['loggedin']) && $_SESSION['loggedin'] == true){
        header("Location: album.php");
    }
    # If you do not want the user to directly access the login page through the url bar then use the below code
#    else if(isset($_SESSION['loggedin']) || $_SESSION['loggedin'] == false){
#        header("Location: index.php");
#    }

    if(isset($_POST['username']) && isset($_POST['password'])){
        if($_POST['username'] == $username && $_POST['password'] == $password){
            $_SESSION['loggedin'] = true;
            header("Location: album.php");
        }
        else{
            echo "<h2>Wrong Login Credentials! Try Again...</h2>";
        }
    }

?>