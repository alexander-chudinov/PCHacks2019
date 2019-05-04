<?php
    include('connect.php');
    $sql = "SELECT time FROM raw_data";
    $result = $dbcon->query($sql);
    $response = "";
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            //$row["time"]. "," .
            $response .=  $row["time"]."|";
        }
    }
    $response = rtrim($response, '|');
    echo $response;
    $dbcon->close();
?>