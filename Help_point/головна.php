<!DOCTYPE html>

<html lang="en" xmlns="http://www.lab3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title>Hallo!</title>
</head>
<body>

    <style>
        body {
            background-color: #F9F9D4;
        }

        .h1 {
            font-family: Copperplate, Papyrus, fantasy;
            padding-top: 140px;
            padding-right: 30px;
            padding-left: 705px;
        }

        table {
            padding-left: 300px;
        }

        td {
            padding-left: 100px;
        }

        .button {
            display: inline-block;
            padding: 70px 100px;
            font-size: 24px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #000000;
            background-color: #B0E0E6;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
        }
        .button:hover {
            background-image: url("https://t4.ftcdn.net/jpg/01/90/43/89/240_F_190438981_GQzfQA2CRJtBnOfcAbd92IQqpL1QRA5X.jpg")
        }

        .button:active {
            background-color: #F0F030;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }

    </style>

    <h1 class="h1">Виберіть</h1>

    <table>
        <tr class="buttons">
            <td><a href=".\реєстр.php"><button class="button">Administrator</button></a></td>
            <td><a href=".\пасажир.php"><button class="button">Passenger</button></a></td>

        </tr>
    </table>

</body>
</html>

