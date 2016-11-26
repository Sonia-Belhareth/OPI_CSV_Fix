print "Starting the script to clean CSV"
#Opening CVS file as text file
f = open("2016-10.csv","r")
#Reading all lines
lines = f.readlines()
#Closing file
f.close()
#Open the Modified CVS file in write mode
f1 = open("2016-10_Modified.csv","w")
#Write the headre to the new CVS
f1.write(lines[0])
#Loop on all the lines
for line in lines[1:]:
	#to avoid ValueError for some wrong entry
    try:
    	#Split the line by the delimeter : , or ; 
        words = line.split(",")
        #Read only the hours of Entrada and Salida (Row 5 and Row 8)and cast them to int
        HE = int(words[5].split(":")[0])
        HS = int(words[8].split(":")[0])
        #If the hour format is correct, add the entry to the new file
        if (HE < 24 and HS < 24):
            f1.write(line)
    except ValueError:
    	print("Error Reading in cell : "+line )

#Close the new file
f1.close()