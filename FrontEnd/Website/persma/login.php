<?php
session_start();
require_once('twitteroauth/twitteroauth.php');
include('config.php');


if(isset($_SESSION['name']) && isset($_SESSION['twitter_id'])) //check whether user already logged in with twitter
{

	//echo "Name is :".$_SESSION['name']."<br>";
	//echo "Twitter ID :".$_SESSION['twitter_id']."<br>";
	//echo "Image :<img src='".$_SESSION['image']."'/><br>";
	//echo "Access Token ".$_SESSION['oauth_token']."Token Secret ".$_SESSION['oauth_token_secret'];
	//echo "<br/><a href='logout.php'>Logout</a>";
	//redirect to main page.
		header('Location: main.php');

}
else // Not logged in
{

	$connection = new TwitterOAuth($CONSUMER_KEY, $CONSUMER_SECRET);
	$request_token = $connection->getRequestToken($OAUTH_CALLBACK); //get Request Token

	if(	$request_token)
	{
		$token = $request_token['oauth_token'];
		$_SESSION['request_token'] = $token ;
		$_SESSION['request_token_secret'] = $request_token['oauth_token_secret'];
		
		switch ($connection->http_code) 
		{
			case 200:
				$url = $connection->getAuthorizeURL($token);
				//redirect to Twitter .
		    	header('Location: ' . $url); 
			    break;
			default:
			    echo "Connection with twitter Failed";
		    	break;
		}

	}
	else //error receiving request token
	{
		echo "Error Receiving Request Token";
	}
	

}



?>
