<!DOCTYPE html>

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

    <h1 class="h1">Search</h1>

    <?php 
    $n = $_POST["num"];
    $d = $_POST["date"];

    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
        die("Error: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM kyr.ticket_main WHERE Ticket_number = '$n' and Date = '$d'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<table><tr><th>Ticket_number</th><th>Date</th><th>Place</th><th>Recommended_login</th><th>Name</th></tr>";
        
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["Ticket_number"] . "</td>";
            echo "<td>" . $row["Date"] . "</td>";
            echo "<td>" . $row["Place"] . "</td>";
            echo "<td>" . $row["Recommended_login"] . "</td>";
            echo "<td>" . $row["Name"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "0 results";
    }

    $conn->close();

    ?>

    <a href=".\головна.php"><button class="button">End</button></a>
    <a href=".\пасажир.php"><button class="button">Main</button></a>

    <h2>More information?</h2>
    <form action="welcome5.php" method="post">
     
    Ticket_number: <input type="text" name="num"><br>
    Direction: <input type="text" name="dir"><br>
    <input class="button" type="submit">
  
</body>
</html>
