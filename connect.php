<?php
    error_reporting(E_ALL);
    ini_set('display_errors', '1');

    define('DB_USER','visitor');
    define('DB_PSWD','');
    define('DB_HOST','158.69.210.95:3306');
    define('DB_NAME','javelindata');

    $dbcon = mysqli_connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
    OR die("Error: " . mysqli_connect_error());
?>