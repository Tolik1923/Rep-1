<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8" />
    <title>Flight information</title>
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

        .q{
            padding-right: 0;
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
    $n = $_POST["num"];
    $d = $_POST["date"];
    $dir = $_POST["dir"];
    $s = $_POST["stat"];
    $dep = $_POST["dep"];
    $t = $_POST["trav"];
    $a = $_POST["arr"];
    $dt = $_POST["dow"];
    $ar = $_POST["air"];
    $ft = $_POST["type"];
    $art = $_POST["art"];
    $ter = $_POST["ter"];
    $r = $_POST["reg"];


    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
        die("Error: " . $conn->connect_error);
    }

    $sql = "INSERT INTO kyr.main (Flight_number, Direction, Date, Status)
VALUES ('$n', '$dir', '$d', '$s')";

    if ($conn->query($sql) === TRUE) {
        echo "";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
    $conn->close();

    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
        die("Error: " . $conn->connect_error);
    }

    $sql = "INSERT INTO kyr.boarding (Terminal, Start_of_registration, Down_time, Departure_time)
VALUES ('$ter', '$reg', '$dt', '$dep')";

    if ($conn->query($sql) === TRUE) {
        echo "";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
    $conn->close();

    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
        die("Error: " . $conn->connect_error);
    }

    $sql = "INSERT INTO kyr.time (Flight_number, Date, Departure_time, Travel_time, Arrival_time)
VALUES ('$n', '$d', '$dep', '$t', '$a')";

    if ($conn->query($sql) === TRUE) {
        echo "";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
    $conn->close();

    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
        die("Error: " . $conn->connect_error);
    }

    $sql = "INSERT INTO kyr.airpiane (Flight_number, Airline_name, Flight_type, Airplane_type)
VALUES ('$n', '$ar', '$ft', '$art')";
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    ?>

    <a href=".\головна.php">
        <button class="button">End</button>
    </a>
    <a href=".\меню_а.php">
        <button class="button">Menu</button>
    </a>



</body>
</html>
