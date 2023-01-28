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

    $sql = "INSERT INTO kyr.ticket_main (Ticket_number, Date, Place, Recommended_login, Name)
VALUES ('$n', '$d', '$p', '$r', '$na')";

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

    $sql = "INSERT INTO kyr.ticket_details (Ticket_number, Direction, Baggage, Passport_control, Type_of_planting)
VALUES ('$n', '$dir', '$b', '$c', '$t')";

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
