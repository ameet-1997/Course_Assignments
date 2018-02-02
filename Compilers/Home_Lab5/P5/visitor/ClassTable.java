package visitor;
import syntaxtree.*;
import java.util.*;    

public class ClassTable{
	String procedure_name; 					// Stores the string of label
	int num_of_args; 						// Number of arguments for this function
	int stack_space; 						// Maximum number of stack slots requried (including spill)
	int max_args; 							// Stores the maximum number of arguments for procedure call inside this procedure
	HashMap<String, String> temp_register;	// The register allocated to the temporary ("none" if no register allocated)
	HashMap<String, String> spilled_temps;	// The temp variable that are spilled
	Vector<liveness> temp_line;				// The temp variables line in respective line numbers (indexed from 0 onwards)
	HashMap<String, Integer> label_line; 	// Contains the label to statement number mapping
	int start_line; 						// Start line of the function
	int end_line; 							// Ending line of the function
	HashMap<String, intervals> temp_ranges_hash;
	Vector<intervals> temp_ranges; 			// Ranges of temp in sorted order
	int next_spilled; 						// The next slot in SPILLEDARG
	int which_to_use; 						// Which of v0 or v1 to use
	boolean did_it_spill; 					// Status of the spilling of temps in a procedure
	int caller_saved;

    public ClassTable(){
        temp_register = new HashMap<String, String>(); 	// Temp to register mapping
        temp_line = new Vector<liveness>(); 				// use and def sets in every statement
        label_line = new HashMap<String, Integer>();
        temp_ranges = new Vector<intervals>();
        temp_ranges_hash = new HashMap<String, intervals>();
        spilled_temps = new HashMap<String, String>();
        next_spilled = 0;
        which_to_use = 0;
        did_it_spill = false;
        stack_space = 18;
        caller_saved=-1;
    }
}; 
 
// class intervals{ 			// To be used in linear scan
// 	Integer start_line;
// 	Integer end_line;
// 	String temp_name;
// };