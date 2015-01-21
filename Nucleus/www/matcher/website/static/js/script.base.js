$(function(){
	//set userInfo
	var nucleusUser = {};
	nucleusUser.extraInfo = "default";
	nucleusUser.processor = "Intel® Core™ i7-3770 Processor";
	nucleusUser.videokaart = "Club 3D Radeon HD 5450 PCI Edition";
	nucleusUser.hardeschijf = '3';
	nucleusUser.geheugen = '4';
	nucleusUser.moederbord = 5;
	nucleusUser.voeding = 5;
	localStorage.setItem( 'nucleusUser', JSON.stringify(nucleusUser) );
	console.log( JSON.parse( localStorage.getItem( 'nucleusUser' ) ) );

	//Desing: gray out first select
    //$("#building form ul li select").click(function(sel) {
    //  	$("#building form ul li select").css("color", "#000"); 
    //});

	//open extraInfo
	$("#building a").click(function() {
		$("#extrainfo").show();
		$("#building").hide();

		var extraInfoTitle = $(this).text();
		alert(extraInfoTitle);
		//changing extraInfo title
		$("#extrainfo .title").text(extraInfoTitle);
	});

	//close extraInfo
	$("#extrainfo .exit a").click(function() {
		$("#extrainfo").hide();
		$("#building").show();
	});

	//inner extraInfo
	$.ajax({
		url: '/static/producten/data.json',
		dataType: 'json',
		type: 'get',
		cache: false,
		success: function(data) {
			$(data.table.nodes).each(function(index, value) {
				for (i = 0; i < 5; i++) { 
					if(value.properties[i] == "Antec VSK 3000E"){
						console.log(value.properties[i]);
					}
					$("#product-info ul").append("<li>" + value.properties.name + "</li>");
					$("#product-info ul").append("<li>" + value.properties.date + "</li>");
					$("#product-info ul").append("<li>" + value.properties.price + "</li>");
					$("#product-info ul").append("<li>" + value.properties.productnumber + "</li>");
				}
			});
		}
	});
});