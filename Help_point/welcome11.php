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

    <h1 class="h1">General</h1>

    <?php
    $n = $_POST["num"];
    $ter = $_POST["ter"];
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
    $r = $_POST["reg"];


    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
        die("Error: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM kyr.main WHERE Flight_number = '$n';";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {

        while($row = $result->fetch_assoc()) {
           if ($n != ""){echo "Flight_number: " . $row["Flight_number"] . "</br>";}
           if ($dir == "+"){ echo "Direction: " . $row["Direction"] . "</br>";}
           if ($d == "+"){ echo "Date: " . $row["Date"] . "</br>";}
           if ($s == "+"){ echo "Status: " . $row["Status"] . "</br>";}
        }
    }

    $sql = "SELECT * FROM kyr.airpiane WHERE Flight_number = '$n';";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {

        while($row = $result->fetch_assoc()) {
           if ($ar == "+"){ echo "Airline_name: " . $row["Airline_name"] . "</br>";}
           if ($ft == "+"){ echo "Flight_type: " . $row["Flight_type"] . "</br>";}
           if ($art == "+"){ echo "Airplane_type: " . $row["Airplane_type"] . "</br>";}
        }
    }

    $sql = "SELECT * FROM kyr.boarding WHERE Terminal = '$ter';";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {

        while($row = $result->fetch_assoc()) {
           if ($r != ""){echo "Terminal: " . $row["Terminal"] . "</br>";}
           if ($r == "+"){ echo "Start_of_registration: " . $row["Start_of_registration"] . "</br>";}
           if ($dt == "+"){ echo "Down_time: " . $row["Down_time"] . "</br>";}
           if ($dep == "+"){ echo "Departure_time: " . $row["Departure_time"] . "</br>";}
        }
    }

      $sql = "SELECT * FROM kyr.time WHERE Flight_number = '$n';";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {

        while($row = $result->fetch_assoc()) {
           if ($t == "+"){ echo "Travel_time: " . $row["Travel_time"] . "</br>";}
           if ($a == "+"){ echo "Arrival_time: " . $row["Arrival_time"] . "</br>";}
        }
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
