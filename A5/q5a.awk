# script to find the middle grade in the class

BEGIN{ind_avg = 0}

{
	
	for (i=1;i<(NF+1);i++){
		ind_avg = ind_avg + $i
	}
	ind_avg = ind_avg/(NF-1)
	grade[$1] = ind_avg
	ind_avg = 0
	

}

END{
		
	for (name in grade){
		print name, grade[name]
		}
		
	
		
}

