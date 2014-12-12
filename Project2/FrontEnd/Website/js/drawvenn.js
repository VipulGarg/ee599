function draw_venn(ses_fbtoken, ses_token, ses_token_secret){
// define sets and set set intersections
var url = "http://54.69.234.8:200/intersection/?token=" + ses_token + "&token_secret=" + ses_token_secret + "&fbtoken=" + ses_fbtoken + "&format=json";
	var d;
	$.ajax({
	  url: url,
	  dataType : 'json'
	}).done(function(data) {
	 	var sets = [{label: "Facebook Friends : "+data.facebook, size: data.facebook}, {label: "Twitter Followers : "+data.twitter, size: data.twitter}],
    overlaps = [{sets: [0,1], size: data.intersection}];
	
	d3.select("#featured-content").html('');
	var div1 = document.createElement("div");	
	div1.setAttribute("id", "intersection");
	div1.setAttribute("value", data.intersection);
	div1.setAttribute("width", "900px");
	div1.setAttribute("height", "10px");
	div1.setAttribute("style","font-size:50px;font-style:bold;text-align:center");
	div1.innerHTML = "Intersection Count : "+ data.intersection;
	document.getElementById("featured-content").appendChild(div1);
	
	// get positions for each set
	sets = venn.venn(sets, overlaps);

	// draw the diagram in the 'simple_example' div
	var diagram = venn.drawD3Diagram(d3.select("#featured-content"), sets, 900, 900);

	var colours = ['blue', 'red', 'blue', 'green']
	diagram.circles.style("fill-opacity", 0)
				   .style("stroke-width", 10)
				   .style("stroke-opacity", .5)
					.style("fill", function(d,i) { return colours[i]; })
					.style("stroke", function(d,i) { return colours[i]; });

	diagram.text.style("fill", function(d,i) { return colours[i]})
				.style("font-size", "24px")
				.style("font-weight", "100");

	diagram.nodes
		.on("mouseover", function(d, i) {
			var node = d3.select(this).transition();
			node.select("circle").style("fill-opacity", .1);
			node.select("text").style("font-weight", "100")
							   .style("font-size", "36px");
		})
		.on("mouseout", function(d, i) {
			var node = d3.select(this).transition();
			node.select("circle").style("fill-opacity", 0);
			node.select("text").style("font-weight", "100")
							   .style("font-size", "24px");
		});

	}).fail(function(jqXHR, textStatus){
		console.log("fail");
	});

}