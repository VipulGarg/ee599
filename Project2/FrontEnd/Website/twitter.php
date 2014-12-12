<?php
session_start();
if( ! (isset($_SESSION['name']) && isset($_SESSION['twitter_id'])) ) //check whether user already logged in with twitter
{
    header('Location: index.php');
}
?>

<!DOCTYPE html>
<html>
  <head>

    <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
    <title>PERSMA</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- StyleSheets -->
    <link type="text/css" rel="stylesheet" href="css/style.css"/>
    <link type="text/css" rel="stylesheet" href="css/hierarchical_edge_bundling.css"/>
    <link type="text/css" rel="stylesheet" href="css/sidebar.css">

    <!-- Scripts -->
    <script src="http://code.jquery.com/jquery-latest.min.js"></script>
    <script type="text/javascript" src="js/d3.js"></script>
    <script type="text/javascript" src="js/d3.layout.js"></script>
    <script type="text/javascript" src="js/packages.js"></script>

  </head>
  <body>
    <script> draw_hierarchical('<?php session_start(); echo $_SESSION['oauth_token']; ?>', '<?php session_start(); echo $_SESSION['oauth_token_secret']; ?>'); </script>

    <nav class='sidebar sidebar-menu-collapsed'> <a href='' id='justify-icon'>
        <span class='glyphicon glyphicon-align-justify'></span>
      </a>

        <ul class='level1'>
            <li class='active'> <a class='expandable' href='' title='Twitter Analysis'>
              <span class='expanded-element'>Twitter Analysis</span>
              </a>

               <ul class='level2'>
                    <li onclick=" draw_hierarchical('<?php session_start(); echo $_SESSION['oauth_token']; ?>', '<?php session_start(); echo $_SESSION['oauth_token_secret']; ?>')" title='Followers'> <a href=''>Followers</a></li>
               </ul>
            </li>  

            <li><a class='expandable' href='logout.php' id='logout-icon' title='Logout'>
              <span class='glyphicon glyphicon-off collapsed-element'></span>
              <span class='expanded-element'>Logout</span>
              </a>
            </li> 
        </ul> 
    </nav>

    <div class="container" id="profile">
        <img id="profile_pic" width="100" src= <?php session_start(); 
                    echo $_SESSION['image']; ?> />
        <h2 id="welcome">Welcome to PERSMA  <?php session_start(); 
                              echo $_SESSION['name']; ?> &nbsp;
        </h2><br/><br/>
         
    </div>

  <!--  <div style="position:absolute;bottom:0;font-size:18px;">tension: <input style="position:relative;top:3px;" type="range" min="0" max="100" value="85"></div>   
   --> 
    <script type="text/javascript" src="js/hierarchical_edge_bundling.js"></script>
    <div id="featured-content"></div>
    
    <script src="https://togetherjs.com/togetherjs.js"></script>
    <script type="text/javascript" src="js/sidebar.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>