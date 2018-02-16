package isd.history;


import java.io.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

public class HistoryProcessor {
	
	public static String ProcessLine(String line) {
		String USAFCode = line.substring(0, 6).trim();
		String name = line.substring(13, 42).trim();
		String countryID = line.substring(43, 45).trim();
		String elevation = line.substring(74,81).trim();

		return String.format("%s\t%s\t%s\t%s\n", USAFCode, name, countryID, elevation);
	}

	public static void main(String[] args) throws IOException {
		
		String inputSource = "/Users/shero/Desktop/DSBA/BDATP/Hadoop_Project/Data/Q2.8/isd-history.txt";
		String outputSource = "/Users/shero/Desktop/DSBA/BDATP/Hadoop_Project/Data/Q2.8/out.txt";
		if (args.length >= 1) {
			inputSource = args[0];
			outputSource = args[1];
		}
				
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(conf);
		InputStream in = fs.open(new Path(inputSource));
		OutputStream os = fs.create(new Path(outputSource));
		
		try {
			InputStreamReader isr = new InputStreamReader(in);
			BufferedReader br = new BufferedReader(isr);
			BufferedWriter bw = new BufferedWriter( new OutputStreamWriter( os, "UTF-8" ));
			
			String line = br.readLine();
			
			int i = 0;
			while (line != null){
				
				if (i < 22) {
					line = br.readLine();
					i += 1;
					continue;
				}
				
				bw.write(ProcessLine(line));
				
				line = br.readLine();
			}
			
			bw.close();
			br.close();
		}
		finally {
			in.close();
			fs.close();
		}		
	}

}
