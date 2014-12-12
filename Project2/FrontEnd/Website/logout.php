<?php

session_start();
$url = $_SESSION['FBLOGOUTURL'];
session_unset();
	$_SESSION['FBID'] = NULL;           
	$_SESSION['FBUSERNAME'] = NULL;
	$_SESSION['name'] = NULL;
	$_SESSION['FBEMAIL'] =  NULL;
	$_SESSION['FBTOKEN'] =  NULL;
session_destroy();
header('Location: index.php'); 

?>