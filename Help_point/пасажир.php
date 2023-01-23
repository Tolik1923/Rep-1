<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8" />
    <title>Main</title>
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
            padding: 15px 25px;
            font-size: 24px;
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

    <h1 class="h1">Main</h1>

        <?php
        $conn = new mysqli("localhost", "root", "Asdfg123456-");
        if($conn->connect_error){
            die("Error: " . $conn->connect_error);
        }
        $sql = "SELECT * FROM kyr.main";
        if($result = $conn->query($sql)){
            $rowsCount = $result->num_rows;
            echo "<table><tr><th>Flight_number</th><th>Direction</th><th>Data</th><th>Status</th></tr>";
            foreach($result as $row){
                echo "<tr>";
                echo "<td>" . $row["Flight_number"] . "</td>";
                echo "<td>" . $row["Direction"] . "</td>";
                echo "<td>" . $row["Date"] . "</td>";
                echo "<td>" . $row["Status"] . "</td>";
                echo "</tr>";
            }
            echo "</table>";
            $result->free();
        } else{
            echo "Error: " . $conn->error;
        }
        $conn->close();
        ?>

    <table>
        <tr class="buttons">
            <td class ="q"><a href=".\головна.php"><button class="button">End</button></a></td>
            <td class ="q"><a href=".\пошук.php"><button class="button">Find flight information</button></a></td>
            <td class ="q"><a href=".\пошук_кв.php"><button class="button">Find ticket information</button></a></td>
        </tr>
    </table>

</body>
</html>
