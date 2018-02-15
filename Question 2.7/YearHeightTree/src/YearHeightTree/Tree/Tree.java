package YearHeightTree;

public class Tree {

	public static String processTree(String line) {
			
		String[] components = line.split(";");
		String year = components[5];
		String height = components[6];
		
		if (year.trim().isEmpty()) {
			year = "UNK";
		}
		
		return year + '\t' + height + '\n';
	}
}
