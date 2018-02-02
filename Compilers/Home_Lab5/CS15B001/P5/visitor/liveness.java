package visitor;
import syntaxtree.*;
import java.util.*;

public class liveness{
	Set<String> use; 		// Represents the used, def, in and out in each of the nodes (basic blocks)
	Set<String> def;
	Set<String> in;
	Set<String> out;

	LinkedList<String> next; 		// Represents the "next" node in the Control Flow Graph
									// Single statements as basic blocks can have a maximum of two edges

	liveness(){
		use = new HashSet<String>();
		def = new HashSet<String>();
		in = new HashSet<String>();
		out = new HashSet<String>();
		next = new LinkedList<String>();
	}
};
