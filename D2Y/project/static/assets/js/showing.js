


$('#apartment').hide()
$('#rent').hide()
flag = 0;


$('#give').on('click',function(){
  $('#give').attr('disabled', true);
  $('#find').attr('disabled', false);
  $('#apartment').fadeIn("slow");
  $('#rent').fadeIn("slow");
  flag = 1;

});
$('#find').on('click',function(){
  $('#give').attr('disabled', false);
  $('#find').attr('disabled', true);
  $('#apartment').fadeIn("slow");
  $('#rent').fadeIn("slow");
  flag = 2;
});


function newUrlApartment() {
	
	if (flag == 1) {
		$( location ).attr("href", "giveapartment");
	} else {
		$( location ).attr("href", "findapartment");
	}
}



function newUrlRent() {
	if (flag == 1) {
		$( location ).attr("href", "giverent");
	} else {
		$( location ).attr("href", "findrent");
	}
}


