<?php
    $input = file_get_contents("php://input");
    include('connect.php');
    $obj = json_decode($input);
    if($input!=null){
        echo "got : \n".var_dump($obj);
        $sql = "INSERT INTO raw_data (ax,ay,az,gx,gy,gz) 
        VALUES (".$obj->{'ax'}.", ".$obj->{'ay'}.", ".$obj->{'az'}.", ".$obj->{'gx'}.", ".$obj->{'gy'}.", ".$obj->{'gz'}.")";
        echo $sql;
        if ($dbcon->query($sql) === TRUE) {
            echo "\n\nNew record created successfully";
        } else {
            echo "Error: \n\n";
                echo $sql;
                echo "\n\n".$dbcon->error;
        }
        $dbcon->close();
    }else{
        echo "connected, no post detected";
    }
?>