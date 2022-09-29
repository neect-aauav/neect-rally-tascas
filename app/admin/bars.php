<?php 
	require $_SERVER['DOCUMENT_ROOT'].'/php/check-session.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin | Rallyween</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="../css/signup.css">
    <link rel="stylesheet" href="../css/admin/bars.css">
</head>
<body>
    <div class="absolute-centered form">
        <p>Choose a Bar</p>
        <div id="bars-list"></div>
    </div>

    <script src="/scripts/admin/bars.js"></script>
</body>
</html>