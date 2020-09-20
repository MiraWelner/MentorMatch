You have submitted your data!
<?php
$path = 'data.txt';
if (isset($_POST['field1']) && isset($_POST['field2']) && isset($_POST['field3'])) {
    $fh = fopen($path,"a+");
    $string = $_POST['field1'].' - '.$_POST['field2'].' - '.$_POST['field3'];
    fwrite($fh,$string); // Write information to the file
    fclose($fh); // Close the file
}
?>