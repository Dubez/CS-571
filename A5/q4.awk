BEGIN{ind_avg = 0; class_avg=0}

{
	
	for (i=1;i<(NF+1);i++){
		ind_avg = ind_avg + $i
	}
	ind_avg = ind_avg/(NF-1)
	class_avg = class_avg + ind_avg
	
	print $1,"'s average score is:", ind_avg
	ind_avg = 0
	

}
END{class_avg = class_avg/NR; print "The class average is:", class_avg}
