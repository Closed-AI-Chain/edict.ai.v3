//the alert is collapsible yay
$(".alert").on("click", function() {
	$(this).hide("slow");
});

//apprearance
$("input.variation").on("click", function() {
	if ($(this).val() > 3) {
		$("body").css("background", "#111");
		$("footer").attr("class", "dark");
	} else {
		$("body").css("background", "#f9f9f9");
		$("footer").attr("class", "");
	}
});

//login works
$("#login").on("click", function() {
	$(".form-login .spinner__wrapper").css({ opacity: 1, "z-index": 5 });
});

//heart button works
$('a.comment__reaction__heart').on('click',function(){
	$(this).toggleClass('toggled');
	if ($(this).hasClass('toggled')) {
		$(this).find('span').html('26 hearts');
	} else {
		$(this).find('span').html('25 hearts');
	}
});