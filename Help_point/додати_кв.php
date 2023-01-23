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

    <h1 class="h1">Add</h1>

    <form action="welcome7.php" method="post">
       
    Ticket_number: <input type="text" name="num"><br>
    Date: <input type="text" name="date"><br>
    Place: <input type="text" name="pl"><br>
    Recommended_login: <input type="text" name="rec"><br>
    Name: <input type="text" name="name"><br>
    Direction: <input type="text" name="dir"><br>
    Baggage: <input type="text" name="bag"><br>
    Passport_control: <input type="text" name="cont"><br>
    Type_of_planting: <input type="text" name="type"><br>
    <input class="button" type="submit">

</body>
</html>
