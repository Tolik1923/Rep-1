<!DOCTYPE html>

<head>
    <meta charset="utf-8" />
    <title>Menu</title>
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
            padding-left: 480px;
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

    <h1 class="h1">Menu</h1>

    <table>
        <tr class="buttons">
            <td>Flight</td>
            <td><a href=".\додати.php"><button class="button">Add</button></a></td>
            <td><a href=".\видалення.php"><button class="button">Delete</button></a></td>
            <td><a href=".\оновити.php"><button class="button">Update</button></a></td>
            <td><a href=".\вибірка.php"><button class="button">General</button></a></td>
        </tr>
        <tr>
            <td>Ticket</td>
            <td><a href=".\додати_кв.php"><button class="button">Add</button></a></td>
            <td><a href=".\видалення_кв.php"><button class="button">Delete</button></a></td>
            <td><a href=".\оновити.php"><button class="button">Update</button></a></td>  
            <td><a href=".\вибірка_кв.php"><button class="button">General</button></a></td>
        </tr>
        <tr><td><a href=".\головна.php"><button class="button">End</button></a></td></tr>
    </table>



    <?php
    echo "";
    ?>
</body>
</html>

