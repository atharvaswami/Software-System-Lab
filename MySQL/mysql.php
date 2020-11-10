<?php

error_reporting(0);

$connect = new mysqli("localhost","root","","publications");

if (!$connect) {
  die("Connection failed: " . mysqli_connect_error());
}

//echo "Connected! <br>";

// connect include
//require("connect.php");

@$display_authors = $_POST["display_authors"];
@$display_titles = $_POST["display_titles"];
@$add_authors = $_POST["add_authors"];
@$add_titles = $_POST["add_titles"];
@$delete_author = $_POST["delete_author"];
@$delete_title = $_POST["delete_title"];
@$update_title = $_POST["update_title"];
@$display_book = $_POST["display_book"];
@$display_details = $_POST["display_details"];

// display table authors
if($display_authors){
  $sql = "SELECT * FROM authors";
  $extract_authors = mysqli_query($connect,$sql);

  echo"<table border='1'>";
  echo"<tr><td>Author</td><td>Publisher</td></tr>";
  while($row = mysqli_fetch_assoc($extract_authors))
  {
    $author = $row["author"];
    $publisher = $row["publisher"];
    echo "<tr><td>$author</td><td>$publisher</td></tr>";
  }
  echo"</table>";

  mysqli_free_result($extract_authors);
}

// display table titles
if($display_titles){
  $sql = "SELECT * FROM titles";
  $extract_titles = mysqli_query($connect,$sql);

  echo"<table border='1'>";
  echo"<tr><td>Title</td><td>Author</td><td>Year</td></tr>";
  while($row = mysqli_fetch_assoc($extract_titles))
  {
    $title = $row["title"];
    $author = $row["author"];
    $year = $row["year"];
    echo "<tr><td>$title</td><td>$author</td><td>$year</td></tr>";
  }
  echo"</table>";

  mysqli_free_result($extract_titles);
}

// add a new record in table authors
if($add_authors){
  $author = $_POST['author_tb1'];
  $publisher = $_POST['publisher_tb'];
  if($author)
  {
    $sql = "INSERT INTO authors (author,publisher) VALUES('$author','$publisher')";
    if(mysqli_query($connect,$sql))
      echo"New record created successfully!";
    else
      echo"Error: $sql";
  }
  else
    echo"The Author should not be blank!";
}

// add a new record in table titles
if($add_titles){
  $title = $_POST['title_tb'];
  $author = $_POST['author_tb2'];
  $year = $_POST['year_tb'];
  if(!(int)$year)
  {
    echo "Enter only integer values in year!";
    return;
  }
  if($title)
  {
    $sql = "INSERT INTO titles (title,author,year) VALUES('$title','$author','$year')";
    if(mysqli_query($connect,$sql))
      echo"New record created successfully!";
    else
      echo"Error: $sql";
  }
  else
    echo"The Title should not be blank!";
}

// delete a record from table authors
if($delete_author){
  $author = $_POST['author_delete_tb'];
  $sql = "DELETE FROM authors WHERE author='$author'";
  if($author)
  {
    if (mysqli_query($connect, $sql))
      echo "Record deleted successfully";
    else 
      echo "Error deleting record: " . mysqli_error($connect);
  }
  else
    echo"The Author should not be blank!";
}

// delete a record from table titles
if($delete_title){
  $title = $_POST['title_delete_tb'];
  if($title)
  {
    $sql = "DELETE FROM titles WHERE title='$title'";
    if (mysqli_query($connect, $sql))
      echo "Record deleted successfully !";
    else 
      echo "Error deleting record: " . mysqli_error($connect);
  }
  else
    echo"The Title should not be blank!";
}

// update the year of a book
if($update_title){
  $title = $_POST['title_update_tb'];
  $new_year = $_POST['new_year_tb'];
  if(!(int)$new_year)
  {
    echo "Enter only integer values in year!";
    return;
  }
  if($title && $new_year)
  {
    $sql = "UPDATE titles SET year='$new_year' WHERE title LIKE '%$title%'";
    if (mysqli_query($connect, $sql))
      echo "Record updated successfully !";
    else 
      echo "Error updating record: " . mysqli_error($connect);
  }
  else
    echo"The Title or Year should not be blank!";
}

// display author and year of publication of a book
if($display_book){
  $title = $_POST['book_tb'];
  if($title)
  {
    $sql = "SELECT author,year FROM titles WHERE title LIKE '%$title%'";
    $display = mysqli_query($connect,$sql);
    echo"<table border='1'>";
    echo"<tr><td>Author</td><td>Year</td></tr>";
    while($row = mysqli_fetch_assoc($display))
    {
      $author = $row["author"];
      $year = $row["year"]; 
      echo "<tr><td>$author</td><td>$year</td></tr>";
    }
    echo"</table>";
  }
  else
    echo"The Book Title should not be blank!";
}

// display details of the book of the given publisher
if($display_details){
  $publisher = $_POST['publisher_details_tb'];
  if($publisher)
  {
    $sql = "SELECT * FROM authors a,titles b WHERE a.author=b.author AND a.publisher LIKE '%$publisher%'";
    $display = mysqli_query($connect,$sql);

    echo"<table border='1'>";
    echo"<tr><td>Title</td><td>Author</td><td>Year</td></tr>";
    while($row = mysqli_fetch_assoc($display))
    {
      $title = $row["title"];
      $author = $row["author"];
      $year = $row["year"];
      echo "<tr><td>$title</td><td>$author</td><td>$year</td></tr>";
    }
    echo"</table>";
  }
  else
    echo"The Publisher should not be blank!";
}

mysqli_close($connect);

?>
