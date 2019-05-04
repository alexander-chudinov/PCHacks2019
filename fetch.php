<?php
    include('connect.php');
    $sql = "SELECT gx,gy,gz FROM raw_data";
    $result = $dbcon->query($sql);
    $response = "";
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            //$row["time"]. "," .
            $response .=  $row["gx"]  . "," . $row["gy"] . "," . $row["gz"] . "|";
        }
    }
    $response = rtrim($response, '|');
    echo $response;
    $dbcon->close();
?>