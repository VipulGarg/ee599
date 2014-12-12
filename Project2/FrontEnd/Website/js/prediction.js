function get_analysis(){
	var coverdiv = document.getElementById("featured-content");
	coverdiv.innerHTML= "";
	
	var div = document.createElement("div");
	div.setAttribute("id", "account");
	div.setAttribute("style","position:relative;float:left;margin-right:25px;margin-left:10px");
	document.getElementById("featured-content").appendChild(div);
	addlabel("account", "account_lbl", "Choose Twitter Account : ");
	addSelectBox("account");	
	
	var div1 = document.createElement("div");
	div1.setAttribute("id", "model");
	div1.setAttribute("style","position:relative;float:left;margin-right:25px;margin-left:10px");
	document.getElementById("featured-content").appendChild(div1);
	addlabel("model", "model_lbl", "Choose Model : ");
	addSelectModelBox("model");

	addGraphs("featured-content");
	addtitle("graph1", "Historical Average Retweet Count");
	addtitle("graph2", "Predicted Average Retweet Count");
	addtitle("graph3", "What-If Analysis");

	addinfo("graph2", "pred_avgrtcont", "true", "Average Retweet Count : ");
	addinfo("graph2", "pred_growthchange", "true", "Change in Follower Growth : ");
	
	addinfo("graph3", "what_avgrtcont", "false", "Average Retweet Count : ");
	addinfo("graph3", "what_growthchange", "false", "Change in Follower Growth : ");
	addbutton("graph3");

	var selectbox = document.getElementById("selectbox");
	var fullname = selectbox.options[selectbox.selectedIndex].value;
	var firstname = fullname.split(" ");
	var selectModelBox = document.getElementById("selectmodelbox");
	var fullModelname = selectModelBox.options[selectModelBox.selectedIndex].value;
	var fullModelnameArr = fullModelname.split(" ");
	
	getmodeldata(firstname[0].toLowerCase(), fullModelnameArr[1], "avgrtcont", "growthchange");
}

function getmodeldata(name, degree, text1, text2){
	var url = "http://54.69.234.8:200/modeling/model/?name=" + name + "&degree=" + degree;
	var d;
	$.ajax({
	  url: url,
	  dataType : 'json'
	}).done(function(data) {
	 	console.log("success");
	 	
	 	document.getElementById('pred_'+text1+'_text').setAttribute("value", data.count);
	 	document.getElementById('what_'+text1+'_text').setAttribute("value", data.count);
	 	document.getElementById('pred_'+text2+'_text').setAttribute("value", data.changeingrowthrate);
	 	document.getElementById('what_'+text2+'_text').setAttribute("value", data.changeingrowthrate);
		updategraph(name, degree);

	}).fail(function(jqXHR, textStatus){
		console.log("fail");
	});

}

function addSelectBox(divname) {
   var newDiv=document.createElement('div');
   var html = '<select id ="selectbox" onchange="changetrigger()" style="margin-left:20px">', dates = GenerateNames(), i;
   for(i = 0; i < dates.length; i++) {
       html += "<option value='"+dates[i]+"'>"+dates[i]+"</option>";
   }
   html += '</select>';
   newDiv.innerHTML= html;
   document.getElementById(divname).appendChild(newDiv);
}

function addSelectModelBox(divname) {
   var newDiv=document.createElement('div');
   var html = '<select id ="selectmodelbox" onchange="changetrigger()" style="margin-left:20px">', models = GenerateModelNames(), i;
   for(i = 0; i < models.length; i++) {
       html += "<option value='"+models[i]+"'>"+models[i]+"</option>";
   }
   html += '</select>';
   newDiv.innerHTML= html;
   document.getElementById(divname).appendChild(newDiv);
}

function GenerateNames() {
   var NameArray = new Array();
   NameArray[0] = "Katy Perry";
   NameArray[1] = "Barack Obama";
   NameArray[2] = "Cristiano Ronaldo";
   NameArray[3] = "Bill gates";
   NameArray[4] = "Jimmy Fallon";
   return NameArray;
}

function GenerateModelNames() {
   var ModelNameArray = new Array();
   ModelNameArray[0] = "Model 1";
   ModelNameArray[1] = "Model 2";
   return ModelNameArray;
}

function changetrigger(){
	var selectbox = document.getElementById("selectbox");
	var fullname = selectbox.options[selectbox.selectedIndex].value;
	var firstname = fullname.split(" ");
	
	var selectModelBox = document.getElementById("selectmodelbox");
	var fullModelname = selectModelBox.options[selectModelBox.selectedIndex].value;
	var fullModelnameArr = fullModelname.split(" ");
	
	getmodeldata(firstname[0].toLowerCase(), fullModelnameArr[1], "avgrtcont", "growthchange");
	cleargraphs();
}

function addGraphs(divname){
	var div1 = document.createElement("div");
	var div2 = document.createElement("div");
	var div3 = document.createElement("div");
	div1.setAttribute("id","graph1");
	div1.setAttribute("style","border:5px solid black;margin-top: 5%;");
	div2.setAttribute("id","graph2");
	div2.setAttribute("style","border:5px solid black;margin-top: 10%;");
	div3.setAttribute("id","graph3");
	div3.setAttribute("style","border:5px solid black;margin-top: 10%;");
	var coverdiv = document.getElementById(divname);
	coverdiv.appendChild(div1);
	coverdiv.appendChild(div2);
	coverdiv.appendChild(div3);
}

function addinfo(divname, id, disabled, label){
	var div = document.createElement("div");
	div.setAttribute("id", id);
	div.setAttribute("style","position:relative;float:left;margin-right:25px;margin-left:10px");
	document.getElementById(divname).appendChild(div);
	addlabel(id, id+"_lbl", label);
	addtextbox(id, id+"_text", disabled);
}

function addtextbox(divname, id, disabled){
	var input = document.createElement('input'); 
	input.type = "text"; 
	if(disabled == "true")
		input.disabled = disabled;
	input.setAttribute("id", id);
	input.setAttribute("value", "");
	input.setAttribute("style","margin-left:10px");
	document.getElementById(divname).appendChild(input);
}

function addlabel(divname, id, val){
    var labdiv = document.createElement("div");
	labdiv.setAttribute("style","font-size:20px;font-style:bold;position:relative;float:left;");
    labdiv.setAttribute("id", id);
    labdiv.innerHTML = val;
    document.getElementById(divname).appendChild(labdiv);
}

function addtitle(divname, titlename){
	var title = document.createElement("div");	
	title.setAttribute("style","font-size:50px;font-style:bold;text-align:center");
	title.innerHTML = titlename;
	document.getElementById(divname).insertBefore(title,document.getElementById(divname).firstChild);
}

function addbutton(id){
	var del = document.createElement('input');
	del.type = 'button';
	del.value = 'Submit';
	del.setAttribute("id", id+"_btn");
	del.setAttribute("style","font-size:20px;font-style:bold");
	del.onclick = function(){
		    		updatewhatif();
		  		};
	document.getElementById(id).appendChild(del);
}

function updategraph(name, degree){
	paststat(name, degree);
	futurestat(name, degree);
	var count = document.getElementById("what_avgrtcont_text").value;
	var growthrate = document.getElementById("what_growthchange_text").value;
	whatif(name, degree, count, growthrate);
}

function cleargraphs(){
	var svgtags = document.getElementsByTagName("svg");
	var tag1 = svgtags[0];
	var tag2 = svgtags[1];
	var tag3 = svgtags[2];
	tag1.parentElement.removeChild(tag1);
	tag2.parentElement.removeChild(tag2);
	tag3.parentElement.removeChild(tag3);
}

function updatewhatif(){
	var svgtags = document.getElementsByTagName("svg");
	svgtags[2].parentElement.removeChild(svgtags[2]);
	var selectbox = document.getElementById("selectbox");
	var fullname = selectbox.options[selectbox.selectedIndex].value;
	var firstname = fullname.split(" ");
	
	var selectModelBox = document.getElementById("selectmodelbox");
	var fullModelname = selectModelBox.options[selectModelBox.selectedIndex].value;
	var fullModelnameArr = fullModelname.split(" ");
	
	var count = document.getElementById("what_avgrtcont_text").value;
	var growthrate = document.getElementById("what_growthchange_text").value;
	whatif(firstname[0].toLowerCase(), fullModelnameArr[1], count, growthrate);
}