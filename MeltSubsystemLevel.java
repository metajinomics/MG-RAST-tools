// java MeltSubsystemLevel input

import java.io.*;
import java.util.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

class MeltSubsystemLevel {
    public static void main(String[] args) {
        
        
        //Track time of process
        DateFormat dateformat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date1 = new Date();
        System.out.println("Program START at " + dateformat.format(date1));
        
        
        //read subsystem
        String filesubsystem = "subsystem";
        HashMap <String,List<String>> subMap = new HashMap <String,List<String>> ();
        //key option level=4 or level=5 (fig|peg)
        int level = 4;
        readsubsystem(filesubsystem,subMap,level);
        //System.out.println(subMap.size());
        
        
        //read input file
        String fileName1 = args[0];
        
        Scanner fileScanner = null;
		try {
			fileScanner = new Scanner(new File(fileName1));
		} catch(FileNotFoundException e) {
			System.err.println("Could not find file '" + fileName1 + "'.");
			System.exit(1);
		}//try
		String line = null;
		
		
		while(fileScanner.hasNext()) {
			line = fileScanner.nextLine();
			String[] entry = line.split("\t");
			//System.out.println(entry[entry.length-1]);
			String[] tempFun = entry[entry.length-1].split(";");
			
			for (int i=0;i<tempFun.length;i++){
				if(tempFun[i].equals("hypothetical protein")){continue;}
				String [] slash = tempFun[i].split("/");
				for (int j=0;j<slash.length;j++){
					/*
					if(slash[j].contains("EC")){
						String [] pron = slash[j].split("EC");
						slash[j] = pron[0].substring(0,pron[0].length()-1);
					}
					*/
					
				if(subMap.containsKey(slash[j].trim())){
					List<String> tempList = subMap.get(slash[j].trim());
					//System.out.println(tempList.get(0)+"\t"+tempList.get(1)+"\t"+tempList.get(2)+"\t"+entry[entry.length-1]);
				}else{
					System.out.println(slash[j].trim());
				}
				}
			
			}
		}
		fileScanner.close();
        
        
		
		//Track time
        Date date2 = new Date();
        long time = (date2.getTime() - date1.getTime())/1000;
        System.out.println("Program DONE in " + time + " secs");
        System.out.println();
        
        
    }
    
    private static void readsubsystem(String fileName,HashMap <String,List<String>> subMap,int level){
    	Scanner fileScanner = null;
		try {
			fileScanner = new Scanner(new File(fileName));
		} catch(FileNotFoundException e) {
			System.err.println("Could not find file '" + fileName + "'.");
			System.exit(1);
		}//try
		String line = null;
		
		
		while(fileScanner.hasNext()) {
			line = fileScanner.nextLine();
			String[] entry = line.split("\t");
			List<String> tempList = new ArrayList<String>();
			tempList.add(entry[0]);
			tempList.add(entry[1]);
			tempList.add(entry[2]);
			subMap.put(entry[3],tempList);
			//System.out.println(entry[level-1]);
		}
		fileScanner.close();
    
    
    
    }
}
