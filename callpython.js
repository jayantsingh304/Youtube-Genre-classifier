function my() {
$.getJSON($SCRIPT_ROOT + '/_array2python', {
        wordlist: JSON.stringify(list)
    }, function(data){
        console.log(data.result)
        $( "#result" ).text(data.result);
    });
	}
	my();