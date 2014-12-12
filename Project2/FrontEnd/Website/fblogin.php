<?php
require 'src/facebook.php';  // Include facebook SDK file
//require 'functions.php';  // Include functions
$facebook = new Facebook(array(
  'appId'  => '1510866255838153',   // Facebook App ID 
  'secret' => '358d7809324e77adce72de0ea7d82789',  // Facebook App Secret
  'cookie' => true,	
));
$user = $facebook->getUser();

function get_raw_facebook_avatar_url($uid)
{
    $array = get_headers('https://graph.facebook.com/'.$uid.'/picture?width=100&height=100', 1);
    return (isset($array['Location']) ? $array['Location'] : FALSE);
}

if ($user) {
  try {
		$user_profile = $facebook->api('/me');
  	    $fbid = $user_profile['id'];                 // To Get Facebook ID
 	    $fbuname = $user_profile['username'];  // To Get Facebook Username
 	    $fbfullname = $user_profile['name']; // To Get Facebook full name
	    $fbemail = $user_profile['email'];    // To Get Facebook email ID
		$fbtoken = $facebook->getAccessToken();
	/* ---- Session Variables -----*/
	    $_SESSION['FBID'] = $fbid;           
	    $_SESSION['FBUSERNAME'] = $fbuname;
        $_SESSION['name'] = $fbfullname;
	    $_SESSION['FBEMAIL'] =  $fbemail;
	    $_SESSION['FBTOKEN'] =  $fbtoken;
		$_SESSION['image']=	get_raw_facebook_avatar_url($fbid);
    //       checkuser($fbid,$fbuname,$fbfullname,$femail);    // To update local DB
  } catch (FacebookApiException $e) {
		error_log($e);
		$user = null;
  }
}
if ($user) {
	echo $_SESSION['FBID'];
	echo $_SESSION['FBUSERNAME'];
	echo $_SESSION['FBFULLNAME'];
	echo $_SESSION['FBEMAIL'];
	echo $_SESSION['FBTOKEN'];
	$logout_params = array('next'=>'http://ec2-54-69-234-8.us-west-2.compute.amazonaws.com/599a/599/index.php');
    $logoutUrl = $facebook->getLogoutUrl($logout_params);
	$_SESSION['FBLOGOUTURL'] = $logoutUrl;
	echo $_SESSION['FBLOGOUTURL'];
	header("Location: main.php");
} else {
 $loginUrl = $facebook->getLoginUrl(array(
		'scope'		=> 'email, public_profile, user_friends', // Permissions to request from the user
		'redirect_uri'	=> 'http://ec2-54-69-234-8.us-west-2.compute.amazonaws.com/599a/599/fblogin.php',
		));
 header("Location: ".$loginUrl);
}
?>
