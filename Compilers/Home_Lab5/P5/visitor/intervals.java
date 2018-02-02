package visitor;
import syntaxtree.*;
import java.util.*;    

public class intervals implements Comparable<intervals>{ 			// To be used in linear scan
	Integer start_line;
	Integer end_line;
	String temp_name;

	public int compareTo(intervals other) {
        return start_line - other.start_line;
   	}
};
