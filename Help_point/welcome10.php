<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8" />
    <title>Update</title>
</head>

<body>

    <style>
        body {
            background-color: #c9ffe5;
        }

        .h1 {
            font-family: Lucida Console, Papyrus, fantasy;
            padding-top: 50px;
            padding-right: 30px;
            padding-left: 665px;
        }

        table {
            padding-left: 410px;
        }

        td{
            padding-right: 120px;
        }


        .button {
            display: inline-block;
            padding: 7px 10px;
            font-size: 18px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #000000;
            background-color: #f4bbff;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
        }
        .button:hover {
            background-color: #87CEFA
        }

        .button:active {
            background-color: #B0C4DE;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }

        .line {
            width: 95%;
            background-color: #E0FFFF;
        }
    </style>

    <h1 class="h1">Congratulations</h1>

    <?php
    $w = $_POST["where"];
    $o = $_POST["old"];
    $n = $_POST["new"];

    if (($w == "Flight_number") || ($w =='Airline_name')|| ($w =='Flight_type')|| ($w =='Airplane_type')){
        $conn = new mysqli("localhost", "root", "Asdfg123456-");
        if($conn->connect_error){
            die("Error: " . $conn->connect_error);
        }
        $sql = "UPDATE kyr.airpiane
                    SET $w ='$n'
                    WHERE $w ='$o'";

        if ($conn->query($sql) === TRUE) {
            echo "Record updated successfully";
        } else {
            echo "Error updating record: " . $conn->error;
        }
        $conn->close();
    }

    if (($w == "Terminal") or ($w == "Start_of_registration") or ($w == "Down_time") or ($w == "Departure_time")){
        $conn = new mysqli("localhost", "root", "Asdfg123456-");
        if($conn->connect_error){
            die("Error: " . $conn->connect_error);
        }
        $sql = "UPDATE kyr.boarding
                    SET $w ='$n'
                    WHERE $w ='$o'";

        if ($conn->query($sql) === TRUE) {
            echo "Record updated successfully";
        } else {
            echo "Error updating record: " . $conn->error;
        }
        $conn->close();
    }

    if (($w == "Flight_number") || ($w =='Direction')|| ($w =='Date')|| ($w =='Status')){
        $conn = new mysqli("localhost", "root", "Asdfg123456-");
        if($conn->connect_error){
            die("Error: " . $conn->connect_error);
        }
         $sql = "UPDATE kyr.main
                    SET $w ='$n'
                    WHERE $w ='$o'";

         if ($conn->query($sql) === TRUE) {
             echo "Record updated successfully";
         } else {
             echo "Error updating record: " . $conn->error;
         }
         $conn->close();
    }

    if (($w == "Ticket_number") || ($w =='Date')|| ($w =='Departure_time')|| ($w =='Travel_time')|| ($w =='Arrival_time')){
        $conn = new mysqli("localhost", "root", "Asdfg123456-");
        if($conn->connect_error){
            die("Error: " . $conn->connect_error);
        }
         $sql = "UPDATE kyr.time
                    SET $w ='$n'
                    WHERE $w ='$o'";

         if ($conn->query($sql) === TRUE) {
             echo "Record updated successfully";
         } else {
             echo "Error updating record: " . $conn->error;
         }
         $conn->close();
    }

    if (($w == "Ticket_number") || ($w =='Direction')|| ($w =='Baggage')|| ($w =='Passport_control')|| ($w =='Type_of_planting')){
        $conn = new mysqli("localhost", "root", "Asdfg123456-");
        if($conn->connect_error){
            die("Error: " . $conn->connect_error);
        }
         $sql = "UPDATE kyr.ticket_details
                    SET $w ='$n'
                    WHERE $w ='$o'";

         if ($conn->query($sql) === TRUE) {
             echo "Record updated successfully";
         } else {
             echo "Error updating record: " . $conn->error;
         }
         $conn->close();
    }

    if (($w == "Ticket_number") || ($w =='Date')|| ($w =='Place')|| ($w =='Recommended_login')|| ($w =='Name')){
        $conn = new mysqli("localhost", "root", "Asdfg123456-");
        if($conn->connect_error){
            die("Error: " . $conn->connect_error);
        }
         $sql = "UPDATE kyr.ticket_main
                    SET $w ='$n'
                    WHERE $w ='$o'";

         if ($conn->query($sql) === TRUE) {
             echo "Record updated successfully";
         } else {
             echo "Error updating record: " . $conn->error;
         }
         $conn->close();
    }

    ?>

    <a href=".\головна.php">
        <button class="button">End</button>
    </a>
    <a href=".\меню_а.php">
        <button class="button">Menu</button>
    </a>

</body>
</html>