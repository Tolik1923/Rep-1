<!DOCTYPE html>

<html lang="en" xmlns="http://www.lab.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title>z2-t3</title>
</head>
<body>

    <style>
        body {
            background-color: #e6e6fa;
        }

        h1 {
            font-family: Copperplate, Papyrus, Trebuchet MS;
            padding-top: 30px;
            padding-right: 30px;
            padding-left: 620px;
        }

        td {
            padding-left: 50px;
            padding-top: 20px;
        }

        .с1 {
            padding-left: 50px;
        }

        .с2 {
            padding-left: 400px;
            padding-top: 30px;
            padding-bottom: 30px;
        }

        .с3 {
            padding-left: 40px;
            padding-top: 30px;
            padding-bottom: 30px;
        }

        .button {
            display: inline-block;
            padding: 10px 15px;
            font-size: 15px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #000000;
            background-color: #c4c3d0;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
        }

            .button:hover {
                background-color: #e0b0ff
            }

            .button:active {
                background-color: #ff66cc;
                box-shadow: 0 5px #666;
                transform: translateY(4px);
            }
    </style>

    <h1>Конфіденційність</h1>

    <table>
        <tr><th>Назва активу</th><th>Власник активу</th><th>Місце розташування</th><th class="с1">Категорія</th></tr>
        <th class="с1">База даних наявних експонатів</th>
        <th class="с1">Очільник науково-методичного відділу</th>
        <th class="с1">Хмарне середовище, доступ - Робоча станція 1, кабінет 1</th>
        <th class="с1">ЕД</th>
    </table>

    <table>
        <th class="с2">Загроза:</th>
        <th class="с3">Несанкціоноване використання програмного забезпечення (хмарне середовище  OneDrive )</th>
    </table>

    <?php
    $conn = new mysqli("localhost", "root", "Asdfg123456-");
    if($conn->connect_error){
    die("Error: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM r3.z2_t3";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
    echo "
    <table>
        <tr><th>Джерело загрози</th><th>Механізм реалізації нападу</th></tr>";
        while($row = $result->fetch_assoc()) {
        echo "
        <tr>
            ";
            echo "
            <td>" . $row["drl"] . "</td>";
            echo "
            <td>" . $row["meh"] . "</td>";
            echo "
        </tr>";
        }
        echo "
    </table>";
    } else {
    echo "0 results";
    }



    $conn->close();

    ?>

    <a href=".\aktuv.html">
        <button class="button">Перейти до актиків</button>
    </a>

</body>
</html>