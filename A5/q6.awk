BEGIN{ind_avg = 0; class_avg=0}

{
	
	for (i=1;i<(NF+1);i++){
		ind_avg = ind_avg + $i
	}
	ind_avg = ind_avg/(NF-1)
	avg[$1] = ind_avg
	ind_avg = 0
}

END{
	for(name in avg){
		if(avg[name] >= 90)
			print name, "A"
		else if(avg[name] >= 80)
			print name, "B"
		else if(avg[name] >= 70)
			print name, "C"
		else if(avg[name] >= 50)
			print name, "D"
		else
			print name, "F"
	}
	
}
