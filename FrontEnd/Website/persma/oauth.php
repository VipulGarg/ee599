<?php
session_start();
require_once('twitteroauth/twitteroauth.php');
include('config.php');


if(isset($_GET['oauth_token']))
{


	$connection = new TwitterOAuth($CONSUMER_KEY, $CONSUMER_SECRET, $_SESSION['request_token'], $_SESSION['request_token_secret']);
	$access_token = $connection->getAccessToken($_REQUEST['oauth_verifier']);
	if($access_token)
	{
			$connection = new TwitterOAuth($CONSUMER_KEY, $CONSUMER_SECRET, $access_token['oauth_token'], $access_token['oauth_token_secret']);
			$params =array();
			$params['include_entities']='false';
			$content = $connection->get('account/verify_credentials',$params);

			if($content && isset($content->screen_name) && isset($content->name))
			{
				$_SESSION['name']=$content->name;
				$_SESSION['image']=$content->profile_image_url;
				$_SESSION['twitter_id']=$content->screen_name;
				$_SESSION['oauth_token']= $access_token['oauth_token'];
				$_SESSION['oauth_token_secret']= $access_token['oauth_token_secret'];	
				//redirect to main page.
				header('Location: login.php'); 

			}
			else
			{
				echo "<h4> Login Error </h4>";
			}
	}

	else
	{

		echo "<h4> Login Error </h4>";
	}

}
else //Error. redirect to Login Page.
{
	header('Location: http://ec2-54-69-234-8.us-west-2.compute.amazonaws.com/599/index.php'); 

}

?>
