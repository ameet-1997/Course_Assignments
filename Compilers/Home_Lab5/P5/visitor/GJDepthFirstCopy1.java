//
// Generated by JTB 1.3.2
//

package visitor;
import syntaxtree.*;
import java.util.*;

/**
 * Provides default methods which visit each node in the tree in depth-first
 * order.  Your visitors may extend this class.
 */
public class GJDepthFirstCopy1<R,A> extends GJDepthFirst<R,A> {
   //
   // Auto class visitors--probably don't need to be overridden.
   //

    int argument_number = 0;
    boolean is_call_statement = false;
    boolean to_be_written = false;
    String spilled_in_move = null;
   public R visit(NodeList n, A argu) {
      R _ret=null;
      int _count=0;
      for ( Enumeration<Node> e = n.elements(); e.hasMoreElements(); ) {
         e.nextElement().accept(this,argu);
         _count++;
      }
      return _ret;
   }

   public R visit(NodeListOptional n, A argu) {
      if ( n.present() ) {
         R _ret=null;
         int _count=0;
         for ( Enumeration<Node> e = n.elements(); e.hasMoreElements(); ) {
            e.nextElement().accept(this,argu);
            _count++;
         }
         return _ret;
      }
      else
         return null;
   }

   public R visit(NodeOptional n, A argu) {
      if ( n.present() ){
        ClassTable ct = (ClassTable) argu;
        String label = (String) n.node.accept(this,argu);
        System.out.print(ct.procedure_name+"_"+label+" ");                        // Print the label after which the statement will be printed
         return (R) label;
       }
      else
         return null;
   }

   public R visit(NodeSequence n, A argu) {
      R _ret=null;
      int _count=0;
      for ( Enumeration<Node> e = n.elements(); e.hasMoreElements(); ) {
         e.nextElement().accept(this,argu);
         _count++;
      }
      return _ret;
   }

   public R visit(NodeToken n, A argu) { return null; }

   //
   // User-generated visitor methods below
   //

   String get_v_register(int a){
      if(a == 0){
          return "v1";
      }
      else if(a == 1){
          return "v0";
      }
      else{
        // System.out.println("Error in Spilled Arguments in function get_v_register");
        return "v1";
      }
   }

   String get_spilled(String cur, String temp_no, int num_of_args){
      if(cur != null){
          return cur;
      }
      else{
          int temp = Integer.parseInt(temp_no);
          if((temp > 3)&&(num_of_args >= temp)){
              return Integer.toString(temp-4);
          }
          else{
              return null;
          }
      }
   }

   /**
    * f0 -> "MAIN"
    * f1 -> StmtList()
    * f2 -> "END"
    * f3 -> ( Procedure() )*
    * f4 -> <EOF>
    */
   public R visit(Goal n, A argu) {
      R _ret=null;
      number_of_lines = 0;
      ClassTable ct = procedures.get("MAIN");
      argu = (A) ct;
      n.f0.accept(this, argu);
      System.out.print("MAIN");System.out.print(" [");System.out.print(ct.num_of_args);System.out.print("]");System.out.print(" [");System.out.print(ct.stack_space);System.out.print("]");System.out.print(" [");System.out.print(max_args_in_program);System.out.println("]");
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      System.out.println("END");
      if(ct.did_it_spill){                    // Print if any variable was spilled or not
          System.out.println("// SPILLED");
      }
      else{
          System.out.println("// NOTSPILLED");
      }System.out.println();
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> ( ( Label() )? Stmt() )*
    */
   public R visit(StmtList n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> Label()
    * f1 -> "["
    * f2 -> IntegerLiteral()
    * f3 -> "]"
    * f4 -> StmtExp()
    */
   public R visit(Procedure n, A argu) {
      R _ret=null;
      String proc_name = (String) n.f0.accept(this, argu);
      ClassTable ct = procedures.get(proc_name);
      argu = (A) ct;
      System.out.print(ct.procedure_name);System.out.print(" [");System.out.print(ct.num_of_args);System.out.print("]");System.out.print(" [");System.out.print(ct.stack_space);System.out.print("]");System.out.print(" [");System.out.print(max_args_in_program);System.out.println("]");
      
      ct.next_spilled = Math.max(0, ct.num_of_args-4);    // If there are more than 4 arguments
      int current_spilled = ct.next_spilled;
      for(int i=0;i<8;++i){                                           // Callee saved registers
        System.out.print("ASTORE SPILLEDARG ");System.out.print(i+ct.next_spilled);
        System.out.print(" s");System.out.println(i);
      }

      for(int i=0;i<ct.num_of_args;++i){
          // // Debug
          // System.out.println("Looking at TEMP:"+Integer.toString(i));

          if(ct.temp_register.get(Integer.toString(i)) == null){
            continue;
          }
          if(ct.temp_register.get(Integer.toString(i)).length()<=2){
              System.out.print("MOVE "+ct.temp_register.get(Integer.toString(i))+" a");System.out.println(i);
          }
      }
      
      ct.next_spilled = ct.next_spilled + 8;
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);

      for(int i=0;i<8;++i){                                           // Callee saved registers
        System.out.print("ALOAD s");System.out.print(i);System.out.print(" SPILLEDARG ");System.out.println(i+current_spilled);
        // System.out.print("ALOAD SPILLEDARG ");System.out.print(i+current_spilled);
        // System.out.print(" s");System.out.println(i);
      }

      System.out.println("END");
      
      if(ct.did_it_spill){                    // Print if any variable was spilled or not
          System.out.println("// SPILLED");
      }
      else{
          System.out.println("// NOTSPILLED");
      }System.out.println();
      
      return _ret;
   }

   /**
    * f0 -> NoOpStmt()
    *       | ErrorStmt()
    *       | CJumpStmt()
    *       | JumpStmt()
    *       | HStoreStmt()
    *       | HLoadStmt()
    *       | MoveStmt()
    *       | PrintStmt()
    */
   public R visit(Stmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      ClassTable ct = (ClassTable) argu;
      ct.which_to_use = 0;                // After this statement, v0 and v1 need not be used again
      number_of_lines++;
      return _ret;
   }

   /**
    * f0 -> "NOOP"
    */
   public R visit(NoOpStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      System.out.println("NOOP");
      return _ret;
   }

   /**
    * f0 -> "ERROR"
    */
   public R visit(ErrorStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      System.out.println("ERROR");
      return _ret;
   }

   /**
    * f0 -> "CJUMP"
    * f1 -> Temp()
    * f2 -> Label()
    */
   public R visit(CJumpStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      ClassTable ct = (ClassTable) argu;
      String temp = (String) n.f1.accept(this, argu);
      String label = (String) n.f2.accept(this, argu);

      System.out.println("CJUMP "+temp+" "+ct.procedure_name+"_"+label);
      return _ret;
   }

   /**
    * f0 -> "JUMP"
    * f1 -> Label()
    */
   public R visit(JumpStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      ClassTable ct = (ClassTable) argu;
      String label = (String) n.f1.accept(this, argu);

      System.out.println("JUMP "+ct.procedure_name+"_"+label);
      return _ret;
   }

   /**
    * f0 -> "HSTORE"
    * f1 -> Temp()
    * f2 -> IntegerLiteral()
    * f3 -> Temp()
    */
   public R visit(HStoreStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      String temp1 = (String) n.f1.accept(this, argu);
      String intl = (String) n.f2.accept(this, argu);
      String temp2 = (String) n.f3.accept(this, argu);
      System.out.println("HSTORE "+temp1+" "+intl+" "+temp2);   // Print the statement
      return _ret;
   }

   /**
    * f0 -> "HLOAD"
    * f1 -> Temp()
    * f2 -> Temp()
    * f3 -> IntegerLiteral()
    */
   public R visit(HLoadStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      to_be_written = true;
      String temp1 = (String) n.f1.accept(this, argu);
      String local_spilled_in_move = null;
      if(spilled_in_move != null){
          local_spilled_in_move = new String(spilled_in_move);
      }
      spilled_in_move=null;
      to_be_written = false;
      String temp2 = (String) n.f2.accept(this, argu);
      String intl = (String) n.f3.accept(this, argu);
      System.out.println("HLOAD "+temp1+" "+temp2+" "+intl);

      if(local_spilled_in_move != null){                // ASTORE statement if we write to a spilled variable
        System.out.println("ASTORE SPILLEDARG "+local_spilled_in_move+" "+temp1);
      }

      return _ret;
   }

   /**
    * f0 -> "MOVE"
    * f1 -> Temp()
    * f2 -> Exp()
    */
   public R visit(MoveStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      to_be_written = true;
      String temp = (String) n.f1.accept(this, argu);

      // String local_spilled_in_move = spilled_in_move;
      String local_spilled_in_move = null;
      if(spilled_in_move != null){
          local_spilled_in_move = new String(spilled_in_move);
      }
      spilled_in_move = null;
      to_be_written =false;
      String exp = (String) n.f2.accept(this, argu);
      System.out.println("MOVE "+temp+" "+exp);
      if(local_spilled_in_move != null){                // ASTORE statement if we write to a spilled variable
        // System.out.println("IMPOSSOBLE TO MISS THIS");
        System.out.println("ASTORE SPILLEDARG "+local_spilled_in_move+" "+temp);
      }      
      return _ret;
   }

   /**
    * f0 -> "PRINT"
    * f1 -> SimpleExp()
    */
   public R visit(PrintStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      String exp = (String) n.f1.accept(this, argu);
      System.out.println("PRINT "+exp);
      return _ret;
   }

   /**
    * f0 -> Call()
    *       | HAllocate()
    *       | BinOp()
    *       | SimpleExp()
    */
   public R visit(Exp n, A argu) {
      R _ret=null;
      String temp = (String) n.f0.accept(this, argu);
      return (R) temp;
      // return _ret;
   }

   /**
    * f0 -> "BEGIN"
    * f1 -> StmtList()
    * f2 -> "RETURN"
    * f3 -> SimpleExp()
    * f4 -> "END"
    */
   public R visit(StmtExp n, A argu) {
      R _ret=null;
      ClassTable ct = (ClassTable) argu;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      String exp = (String) n.f3.accept(this, argu);
      ct.which_to_use = 0;
      number_of_lines++;
      n.f4.accept(this, argu);

      System.out.println("MOVE v0 "+exp);     // Return value to be stored here
      return _ret;
   }

   /**
    * f0 -> "CALL"
    * f1 -> SimpleExp()
    * f2 -> "("
    * f3 -> ( Temp() )*
    * f4 -> ")"
    */
   public R visit(Call n, A argu) {
      R _ret=null;

      ClassTable ct = (ClassTable) argu;

      // int current_spilled = ct.next_spilled;
      // ct.caller_saved = ct.next_spilled;
      if(ct.caller_saved == -1){
        ct.caller_saved = ct.next_spilled;
      }
      // System.out.print("Next Spilled is : ");System.out.println(ct.next_spilled);
      for(int i=0;i<10;++i){                                           // Caller saved registers
        System.out.print("ASTORE SPILLEDARG ");System.out.print(i+ct.caller_saved);
        System.out.print(" t");System.out.println(i);
      }
      ct.next_spilled = ct.next_spilled+10;

      argument_number = 0;
      n.f0.accept(this, argu);
      String exp = (String) n.f1.accept(this, argu);
      is_call_statement = true;
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      is_call_statement = false;
      argument_number = 0;

      System.out.println("CALL "+exp);    // Call the function

      for(int i=0;i<10;++i){                                           // Callee saved registers
        System.out.print("ALOAD t");System.out.print(i);System.out.print(" SPILLEDARG ");System.out.println(i+ct.caller_saved);
        // System.out.print("ALOAD SPILLEDARG ");System.out.print(i+current_spilled);
        // System.out.print(" s");System.out.println(i);
      }
      // Return value is stored in the v0 register
      return (R) "v0";
      // return _ret;
   }

   /**
    * f0 -> "HALLOCATE"
    * f1 -> SimpleExp()
    */
   public R visit(HAllocate n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      String se = (String) n.f1.accept(this, argu);
      return (R) ("HALLOCATE "+se);
      // return _ret;
   }

   /**
    * f0 -> Operator()
    * f1 -> Temp()
    * f2 -> SimpleExp()
    */
   public R visit(BinOp n, A argu) {
      R _ret=null;
      String op= (String) n.f0.accept(this, argu);
      String temp = (String) n.f1.accept(this, argu);
      String se = (String) n.f2.accept(this, argu);
      return (R) (op+" "+temp+" "+se);
      // return _ret;
   }

   /**
    * f0 -> "LE"
    *       | "NE"
    *       | "PLUS"
    *       | "MINUS"
    *       | "TIMES"
    *       | "DIV"
    */
   public R visit(Operator n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return (R) n.f0.choice.toString();
      // return _ret;
   }

   /**
    * f0 -> Temp()
    *       | IntegerLiteral()
    *       | Label()
    */
   public R visit(SimpleExp n, A argu) {
      R _ret=null;
      String temp = (String) n.f0.accept(this, argu);
      return (R) temp;
      // return _ret;
   }

   /**
    * f0 -> "TEMP"
    * f1 -> IntegerLiteral()
    */
   public R visit(Temp n, A argu) {
      R _ret=null;
      ClassTable ct = (ClassTable) argu;
      n.f0.accept(this, argu);
      String temp_no = (String) n.f1.accept(this, argu);

      if(is_call_statement){    // If it is a call statement, then push to arguments
        String vregister = "v1";
        // vregister = get_v_register(ct.which_to_use);
        // ct.which_to_use++;
        if(ct.temp_register.get(temp_no).length()>2){       // It is a spilled variable
          if((ct.num_of_args >= Integer.parseInt(temp_no))&&(Integer.parseInt(temp_no) > 3)){
              System.out.println("ALOAD "+vregister+" SPILLEDARG "+Integer.toString(Integer.parseInt(temp_no)-4));
                if(argument_number < 4){
                  System.out.print("MOVE a");System.out.print(argument_number);System.out.println(" v1");
                }
                else{
                  System.out.print("PASSARG ");System.out.print(argument_number-4+1);System.out.println(" v1");
                }
              argument_number++;
              return (R) vregister;
          }
          
            if(!ct.spilled_temps.containsKey(temp_no)){
                ct.spilled_temps.put(temp_no, Integer.toString(ct.next_spilled));     // Assign Stack Space
                ct.next_spilled++;
            }
            
                vregister = "v1";     
                System.out.println("ALOAD "+vregister+" SPILLEDARG "+ct.spilled_temps.get(temp_no));

                if(argument_number < 4){
                  System.out.print("MOVE a");System.out.print(argument_number);System.out.println(" v1");
                }
                else{
                  System.out.print("PASSARG ");System.out.print(argument_number-4+1);System.out.println(" v1");
                }
          
        }
        else{ 
                String current_register = ct.temp_register.get(temp_no);
                if(argument_number < 4){
                  System.out.print("MOVE a");System.out.print(argument_number);System.out.println(" "+current_register);
                }
                else{
                  System.out.print("PASSARG ");System.out.print(argument_number-4+1);System.out.println(" "+current_register);
                }
            // return (R) ct.temp_register.get(temp_no);       // Return the right register
        }


        argument_number++;
        return _ret;
      }

      // // Debug Statements
      // System.out.println("Temp number is:::"+temp_no);
      // System.out.println(ct.temp_register.get(temp_no));
      if(ct.temp_register.get(temp_no) == null){ct.temp_register.put(temp_no, "v1");}
      if(ct.temp_register.get(temp_no).length()>2){       // It is a spilled variable

        String vregister;
          if((ct.num_of_args >= Integer.parseInt(temp_no))&&(Integer.parseInt(temp_no) > 3)){
              vregister = get_v_register(ct.which_to_use);
              ct.which_to_use++;
              if(to_be_written){/*System.out.println("LOLZ");*/ spilled_in_move = get_spilled(ct.spilled_temps.get(temp_no), temp_no, ct.num_of_args); return (R) vregister;}    // If it is being written, no need to load
              System.out.println("ALOAD "+vregister+" SPILLEDARG "+Integer.toString(Integer.parseInt(temp_no)-4));
              return (R) vregister;
          }
          if(!ct.spilled_temps.containsKey(temp_no)){
              ct.spilled_temps.put(temp_no, Integer.toString(ct.next_spilled));     // Assign Stack Space
              ct.next_spilled++;
          }
          // if(ct.spilled_temps.containsKey(temp_no)){     // Put if statement for assertion if required
              vregister = get_v_register(ct.which_to_use);
              ct.which_to_use++;
              if(to_be_written){spilled_in_move = ct.spilled_temps.get(temp_no); return (R) vregister;}    // If it is being written, no need to load
              System.out.println("ALOAD "+vregister+" SPILLEDARG "+ct.spilled_temps.get(temp_no));
          // }
          return (R) vregister;
      }
      else{
          return (R) ct.temp_register.get(temp_no);       // Return the right register
      }
      // return _ret;
   }

   /**
    * f0 -> <INTEGER_LITERAL>
    */
   public R visit(IntegerLiteral n, A argu) {
      R _ret=null;
      ClassTable ct = (ClassTable) argu;       // Class table for the procedure
      n.f0.accept(this, argu);
      return (R) n.f0.toString();     // Return the integer literal as a string. Parse when it is being used
      // return _ret;
   }

   /**
    * f0 -> <IDENTIFIER>
    */
   public R visit(Label n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return (R) n.f0.toString();     // Return the label
      // return _ret;
   }

}
