<?php
    error_reporting(E_ALL);
    ini_set('display_errors', '1');
    $input = file_get_contents("php://input");
    $obj = json_decode($input);
    if($input!=null){
        echo "got : \n".var_dump($obj);
        
    }else{
        echo "connected, no post detected";
    }
?>