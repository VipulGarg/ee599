<?php

	require_once('twitteroauth/twitteroauth.php');	
	include('config.php');
	
	function debug_to_console($data)
	{
		if(is_array($data) || is_object($data))
		{
			echo("<script>console.log('PHP: ".json_encode($data)."');</script>");
		} else {
			echo("<script>console.log('PHP: ".$data."');</script>");
		}
	}
	
	function compare_results ( $a, $b ) {
		$diff = $a->followers_count - $b->followers_count;
		return $diff < 0 ? 1 : -1;  // descending order
	}
	$arr = array ('name'=>'flare','children'=>$list1);
	$connection = new TwitterOAuth($CONSUMER_KEY, $CONSUMER_SECRET, $_GET["token"], $_GET["token_secret"]);
	$params =array();
	$params['count']=50;
	$response = $connection->get('followers/list',$params);
	$users = $response->users;
	uasort( $users, compare_results );
	$ret = array();
	$x = 0;
	foreach ($users as $user)
	{
		if ($x == 10)
		{
			break;
		}
		$ssarr=array();
		$params['screen_name']=$user->screen_name;
		$subresponse = $connection->get('followers/list',$params);
		$subusers = $subresponse->users;
		uasort( $subusers, compare_results );
		$sum=0;
		foreach ($subusers as $subuser)
		{
			$sum += $subuser->followers_count;
		}
		foreach ($subusers as $subuser)
		{
			$size = ($subuser->followers_count / $sum) * ($user->followers_count);
			$subarray = array ('name'=>$subuser->name, 'size'=>$size);		
			array_push($ssarr, $subarray);	
		}
		$sarr = array ('name'=>$user->name, 'children'=>$ssarr);		
		array_push($ret, $sarr);
		$x++;
	}
	$arr = array ('name'=>'flare','children'=>$ret);
    echo json_encode($arr);
	
	
	
?>