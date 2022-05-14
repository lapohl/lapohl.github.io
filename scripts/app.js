function findPose(){

	let countArray = [0,0,0,0,0,0];

	if (document.getElementById("depressed").checked){countArray[0]++;}
	if (document.getElementById("tired").checked){countArray[0]++;}	
	if (document.getElementById("indifferent").checked){countArray[0]++;}

	if (document.getElementById("illusionary").checked){countArray[1]++;}
	if (document.getElementById("detached").checked){countArray[1]++;}	
	if (document.getElementById("fearful").checked){countArray[1]++;}

	if (document.getElementById("judgemental").checked){countArray[2]++;}
	if (document.getElementById("insecure").checked){countArray[2]++;}	
	if (document.getElementById("isolated").checked){countArray[2]++;}

	if (document.getElementById("anxious").checked){countArray[3]++;}
	if (document.getElementById("scattered").checked){countArray[3]++;}	
	if (document.getElementById("uncertain").checked){countArray[3]++;}

	if (document.getElementById("dependent").checked){countArray[4]++;}
	if (document.getElementById("negative").checked){countArray[4]++;}	
	if (document.getElementById("arrogant").checked){countArray[4]++;}

	if (document.getElementById("confident").checked){countArray[5]++;}
	if (document.getElementById("emotional").checked){countArray[5]++;}	
	if (document.getElementById("negative").checked){countArray[5]++;}


	let maxInit = 0;
	let maxPlace = -1;
	for (let i =0; i<countArray.length; i++){
		if (countArray[i]>maxInit){
			maxInit = countArray[i];
			maxPlace = i;
		}
	}
	
	const poseArray = [["headstand", "forward bend", "bound angle"],["puppy","lizard","mediation"],["bridge","fish","child's pose"],["warrior I","boat","warrior II"],["pigeon","chair","cow face"],["eagle","mountain pose","tree"]];
	
	document.getElementById("selectionsScreen").style.display = "none";
	document.getElementById("poses").style.display = "block";
	document.getElementById("poses").style.visibility = "visible";
	document.getElementById("Pose1").innerHTML = poseArray[maxPlace][0];
	document.getElementById("Pose2").innerHTML = poseArray[maxPlace][1];
	document.getElementById("Pose3").innerHTML = poseArray[maxPlace][2];


}

