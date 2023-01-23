<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8" />
    <title>Ticket information</title>
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
    $d = $_POST["date"];
    $p = $_POST["pl"];
    $r = $_POST["rec"];
    $na = $_POST["name"];
    $dir = $_POST["dir"];
    $b = $_POST["bag"];
    $c = $_POST["cont"];
    $t = $_POST["type"];


    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
        die("Error: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM kyr.ticket_main WHERE Ticket_number = '$n';";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {

        while($row = $result->fetch_assoc()) {
           if ($n != ""){echo "Ticket_number: " . $row["Ticket_number"] . "</br>";}
           if ($p == "+"){ echo "Place: " . $row["Place"] . "</br>";}
           if ($d == "+"){ echo "Date: " . $row["Date"] . "</br>";}
           if ($r == "+"){ echo "Recommended_login: " . $row["Recommended_login"] . "</br>";}
           if ($na == "+"){ echo "Name: " . $row["Name"] . "</br>";}
        }
    }

    $sql = "SELECT * FROM kyr.ticket_details WHERE Ticket_number = '$n';";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {

        while($row = $result->fetch_assoc()) {
           if ($dir == "+"){ echo "Direction: " . $row["Direction"] . "</br>";}
           if ($b == "+"){ echo "Baggage: " . $row["Baggage"] . "</br>";}
           if ($c == "+"){ echo "Passport_control: " . $row["Passport_control"] . "</br>";}
           if ($t == "+"){ echo "Type_of_planting: " . $row["Type_of_planting"] . "</br>";}
        }
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
