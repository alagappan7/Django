i=1200
			function onTimer(){
    		document.getElementById('mycounter').innerHTML=i;
    		i--;
    		if(i<0){
        		alert('Your have run out on time');
    	}
    		else{
        	setTimeout(onTimer,1000);
    }
}