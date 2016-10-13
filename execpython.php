<?php
$path = $_GET["path"];
$arg = $_GET["arg"];
    $fullPath = 'python '.$path.' '.$arg;
    exec($fullPath, $outpara);
    var_dump($outpara);
?>