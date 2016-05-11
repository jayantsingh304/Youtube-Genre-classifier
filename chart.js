ar myData = new Array(['unit', 20], ['unit two', 10], ['unit three', 30], ['other unit', 10], ['last unit', 30]);
	var myChart = new JSChart('chartcontainer', 'bar');
	myChart.setDataArray(myData);
	myChart.draw();