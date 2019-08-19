BEGIN{ind_avg = 0; class_avg=0}

{
	for (i=0;i<NF;i++){
		if($i == 0){
			print $1, "scored a 0"
			break
		}
	}
	for (i=1;i<(NF+1);i++){
		ind_avg = ind_avg + $i
	}
	ind_avg = ind_avg/(NF-1)
	class_avg = class_avg + ind_avg
	
	print $1, "'s average score is:", ind_avg
	ind_avg = 0
	if(NF != 11) {
		print $1, "is missing", (11-NF), "scores"
	}

}
END{class_avg = class_avg/NR; print "The class average is:", class_avg}
