	echo "Begin"
	$folderLocation = "c:\procedures\"
	$folderLocationTemp = $folderLocation + "*"
	
    $connectionString = ""
    $sqlCommand = "Select [NAME] name  from sysobjects where type = 'P' and category = 0"
	
    $connection = new-object system.data.SqlClient.SQLConnection($connectionString)
    $command = new-object system.data.sqlclient.sqlcommand($sqlCommand,$connection)
    $connection.Open()
    
    $adapter = New-Object System.Data.sqlclient.sqlDataAdapter $command
    $dataset = New-Object System.Data.DataSet
    $adapter.Fill($dataSet) | Out-Null
    
    $connection.Close()

	$data = $dataSet.Tables[0]
		
	Remove-Item $folderLocationTemp -include "*.prc"
		
	foreach($row in $data)
	{ 
		$sqlCommand = "sp_helptext '" + $row.name + "'"
		$sqlCommand
		$connection = new-object system.data.SqlClient.SQLConnection($connectionString)
		$command = new-object system.data.sqlclient.sqlcommand($sqlCommand,$connection)
		$connection.Open()
		
		$adapter = New-Object System.Data.sqlclient.sqlDataAdapter $command
		$dataset = New-Object System.Data.DataSet
		$adapter.Fill($dataSet) | Out-Null
		$data2 = $dataSet.Tables[0]
		
		$fullFileName = $folderLocation + $row.name + ".prc"
		$newFile = New-Item $fullFileName -ItemType file
		
		Add-Content $fullFileName $data2.Text
		$fullFileName
	}
	echo "End"
