package YearHeightTree;


import java.io.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

public class TreeProcessor {

	public static void main(String[] args) throws IOException {
		
		
		String inputSource = "/Users/shero/Desktop/DSBA/BDATP/Hadoop_Project/Data/arbres.csv";
		String outputSource = "";
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
			
			while (line != null){
				
				String treeLine = Tree.processTree(line);
				bw.write(treeLine);
				
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
