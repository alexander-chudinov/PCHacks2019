<?php
    include('connect.php');
    $sql = "SELECT ax,ay,az,gx,gy,gz FROM raw_data";
    $result = $dbcon->query($sql);
    $response = "";
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            //$row["time"]. "," .
            $response .=  $row["ax"]. "," . $row["ay"]. "," . $row["az"] . "," . $row["gx"]  . "," . $row["gy"] . "," . $row["gz"] . "|";
        }
    }
    $response = rtrim($response, '|');
    echo $response;
    $dbcon->close();
?>