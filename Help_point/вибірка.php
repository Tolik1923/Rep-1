<!DOCTYPE html> 

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

    <h1 class="h1">General</h1>

    <form action="welcome11.php" method="post">
       
    Where flight_number: <input type="text" name="num"><br>
    And terminal: <input type="text" name="ter"><br>
    Date: <input type="text" name="date"><br>
    Direction: <input type="text" name="dir"><br>
    Status: <input type="text" name="stat"><br>
    Departure_time: <input type="text" name="dep"><br>
    Travel_time: <input type="text" name="trav"><br>
    Arrival_time: <input type="text" name="arr"><br>
    Start_of_registration: <input type="text" name="reg"><br>
    Down_time: <input type="text" name="down"><br>
    Airline_name: <input type="text" name="air"><br>
    Flight_type: <input type="text" name="type"><br>
    Airplane_type: <input type="text" name="art"><br>
    <input class="button" type="submit">
        </form>

</body>
</html>


