package visitor;
import syntaxtree.*;
import java.util.*;    

public class ClassTable{
    String parent = null;                     // If the class inherits another class
    String current_name = null;               // Current class name
    HashMap<String,ClassTable> method;        // Method name to signature Hashmap
    LinkedList<String> method_list;

    // For functions
    String return_type;             // Return type of the function
    LinkedList<String> arguments;   // Types of the arguments
    LinkedList<String> argument_names;

    // For objects
    HashMap<String, String> id;     // <String, String> represent name and type of the id respectively 
    LinkedList<String> id_list;     // Sequential order of the objects, changed only at declaration time
    HashMap<String, String> vtable; // Stores which function to call at run time
    String vtable_assign;


    boolean for_checking_cycle = false;
    LinkedList<String> for_checking_arguments;
    String object_calling_function; // Stores the temp value associated with the calling object
    int local_variable_values;      // The starting value with which TEMP was associated
    String message_send_type;       // Type of the object calling the function
    String message_send_arguments;  // Argument lists for message send
    boolean check_if_array;         // Check if the rvalue is a new int[] expression

    public ClassTable(){
        // parent = new String();
        // parent = null;
        method = new HashMap<String,ClassTable>();
        arguments = new LinkedList<String>();
        argument_names = new LinkedList<String>();
        id = new HashMap<String, String>();
        for_checking_arguments = new LinkedList<String>();
        method_list = new LinkedList<String>();
        id_list = new LinkedList<String>();
        message_send_type = new String();
        message_send_arguments = new String();
        vtable = new HashMap<String, String>();
        vtable_assign = null;
    }
}; 
