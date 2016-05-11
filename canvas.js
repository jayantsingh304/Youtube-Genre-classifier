  var a;
  var obj ;
  var url;
  
	
function getdata()
{

  chrome.tabs.query({
    active: true,
    lastFocusedWindow: true
}, function(tabs) 
 {
    // and use that tab to fill in out title and url
  var tab = tabs[0];
  console.log(tab.url);
  url=tab.url;
  if(url.indexOf("www.youtube.com/watch?v=")!==-1)
  {
		 if(window.XMLHttpRequest)
				{xmlhttp=new XMLHttpRequest();
				}
			
		else
			{
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
xmlhttp.onreadystatechange=function()
{
if(xmlhttp.readyState==4 && xmlhttp.status==200)
	{var b=xmlhttp.response;
	 continueExecution(b);
	}
}

xmlhttp.open('POST','http://localhost:5000/',true);

xmlhttp.send(url.substring(32, url.length));
}else
{
alert("not an youtube video");
}

  //alert(url.substring(32, url.length));
});
  

	

}
	
			
window.onload = function () {

getdata();
}

function continueExecution(b)
{

 a = b;
    obj = JSON.parse(a);


	
	console.log(a);
	
	var chart = new CanvasJS.Chart("chartContainer",
	{
	
		title:{
			text: "Youtube Video classifier"
		},
		legend: {
			maxWidth: 8,
			itemWidth: 4
		},
		data: [
		{
		
			type: "pie",
			showInLegend: true,
			legendText: "{indexLabel}",
			
			dataPoints:[
				{ y: obj.politics, indexLabel: "Politics" },
				{ y: obj.song, indexLabel: "song" },
				{ y: obj.comedy, indexLabel: "Comedy" },
				
				
			]
	

		}
		]
	});
	
	chart.render();
		
}
