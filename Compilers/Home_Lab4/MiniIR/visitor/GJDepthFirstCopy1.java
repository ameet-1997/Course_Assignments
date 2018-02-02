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


    public int variable_counter = 20;    // Use these temporaries to replace the existing TEMPS
    public boolean is_procedure = false;
    public boolean is_hstore = false;
    public boolean is_hstore_label = false;
    public boolean is_arguments = false;
   //
   // Auto class visitors--probably don't need to be overridden.
   //
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
      if ( n.present() )
         return n.node.accept(this,argu);
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

   /**
    * f0 -> "MAIN"
    * f1 -> StmtList()
    * f2 -> "END"
    * f3 -> ( Procedure() )*
    * f4 -> <EOF>
    */
   public R visit(Goal n, A argu) {
      R _ret=null;
      variable_counter = max_temp + 1 + 20;    // Get the value of max temp from the First Pass

      System.out.println("MAIN");System.out.println();
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);

      System.out.println();
      System.out.println("END");System.out.println();

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
      String label = (String) n.f0.accept(this, argu);    // Label gets printed in the label block itself
      n.f1.accept(this, argu);
      String int_ = (String) n.f2.accept(this, argu);
      n.f3.accept(this, argu);

      System.out.println("[ "+int_+" ]");

      is_procedure = true;
      String stmtexp = (String) n.f4.accept(this, argu);

      
      // System.out.println(stmtexp);

      is_procedure = false;
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
    * f1 -> Exp()
    * f2 -> Label()
    */
   public R visit(CJumpStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      String temp = (String) n.f1.accept(this, argu);
      System.out.print("CJUMP "+temp+" ");
      String label = (String) n.f2.accept(this, argu);    // Label gets printed in label block
      // System.out.println("CJUMP "+temp+" "+label);
      return _ret;
   }

   /**
    * f0 -> "JUMP"
    * f1 -> Label()
    */
   public R visit(JumpStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      System.out.print("JUMP ");
      String label = (String) n.f1.accept(this, argu);    // Label gets printed in label block
      return _ret;
   }

   /**
    * f0 -> "HSTORE"
    * f1 -> Exp()
    * f2 -> IntegerLiteral()
    * f3 -> Exp()
    */
   public R visit(HStoreStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      

      String temp1 = (String) n.f1.accept(this, argu);
      String int_ = (String) n.f2.accept(this, argu);

      
      

      is_hstore = true;
      String temp2 = (String) n.f3.accept(this, argu);
      is_hstore = false;
      int current_variable_counter = variable_counter;
      System.out.println("MOVE TEMP "+variable_counter+" "+temp2);variable_counter++;

      System.out.println("HSTORE "+temp1+" "+int_+" TEMP "+current_variable_counter);
      
      is_hstore = false;
      return _ret;
   }

   /**
    * f0 -> "HLOAD"
    * f1 -> Temp()
    * f2 -> Exp()
    * f3 -> IntegerLiteral()
    */
   public R visit(HLoadStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      String temp1 = (String) n.f1.accept(this, argu);
      String temp2 = (String) n.f2.accept(this, argu);
      String int_ = (String) n.f3.accept(this, argu);

      System.out.println("HLOAD "+temp1+" "+temp2+" "+int_);
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
      String temp1 = (String) n.f1.accept(this, argu);
      String temp2 = (String) n.f2.accept(this, argu);

      System.out.println("MOVE "+temp1+" "+temp2);
      return _ret;
   }

   /**
    * f0 -> "PRINT"
    * f1 -> Exp()
    */
   public R visit(PrintStmt n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      String temp = (String) n.f1.accept(this, argu);
      
      System.out.println("PRINT "+temp);
      return _ret;
   }

   /**
    * f0 -> StmtExp()
    *       | Call()
    *       | HAllocate()
    *       | BinOp()
    *       | Temp()
    *       | IntegerLiteral()
    *       | Label()
    */
   public R visit(Exp n, A argu) {
      R _ret=null;
      LinkedList<String> arguments = (LinkedList<String>) argu;   // If the function is called from CALL, we need arguments

      boolean is_arguments_local = is_arguments;
      is_arguments = false;

      String expr = (String) n.f0.accept(this, argu);
      if(is_hstore&&is_hstore_label){
        is_hstore = false;
        is_hstore_label = false;    // Set the flags as false
        return (R) expr;
      }

      System.out.println("MOVE TEMP "+variable_counter+" "+expr);variable_counter++;
      

      if(is_arguments_local){
        // System.out.println("In correct Branch");
        arguments.add("TEMP "+(variable_counter-1));
      }
      else{
        // System.out.println("In Wrong Branch");
      }

      is_arguments = is_arguments_local;    // Assign it back to original value

      return (R) ("TEMP "+(variable_counter-1));
      // return _ret;
   }

   /**
    * f0 -> "BEGIN"
    * f1 -> StmtList()
    * f2 -> "RETURN"
    * f3 -> Exp()
    * f4 -> "END"
    */
   public R visit(StmtExp n, A argu) {
      R _ret=null;
      is_hstore = false;
      boolean is_procedure_local = is_procedure;
      is_procedure = false;
      n.f0.accept(this, argu);

      if(is_procedure_local){
        System.out.println("BEGIN");
      }

      n.f1.accept(this, argu);    // Prints all statements in block
      n.f2.accept(this, argu);

      String expr = (String) n.f3.accept(this, argu);

      if(is_procedure_local){
        System.out.println("RETURN "+expr);
      }

      n.f4.accept(this, argu);

      if(is_procedure_local){
        System.out.println("END");
      }

      if(!is_procedure_local){
        return (R) (expr);    // Return the temp value
      }

      return _ret;
   }

   /**
    * f0 -> "CALL"
    * f1 -> Exp()
    * f2 -> "("
    * f3 -> ( Exp() )*
    * f4 -> ")"
    */
   public R visit(Call n, A argu) {
      R _ret=null;
      is_hstore = false;
      LinkedList<String> arguments = new LinkedList<String>();
      argu = (A) arguments;

      // if(argu != null){
      //   System.out.println("Works fine");
      // }
      // else{
      //   System.out.println("Does not Work fine");
      // }

      n.f0.accept(this, argu);
      String func_name = (String) n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      is_arguments = true;
      n.f3.accept(this, argu);
      is_arguments = false;
      n.f4.accept(this, argu);
      String to_return = "";
      // System.out.println("CALL "+func_name);
      to_return = "CALL "+func_name;

      // Print the linked list using an iterator

      Iterator x = arguments.listIterator(0);

      // System.out.print("( ");
      to_return = to_return + " ( ";

      while (x.hasNext()) {

        // System.out.print(x.next());
        // System.out.print(" ");
        to_return = to_return + x.next();
        to_return = to_return + " ";
      }

      // System.out.println(")");
      to_return = to_return + ")";
      return (R) to_return;
      // return _ret;
   }

   /**
    * f0 -> "HALLOCATE"
    * f1 -> Exp()
    */
   public R visit(HAllocate n, A argu) {
      R _ret=null;
      is_hstore = false;

      n.f0.accept(this, argu);
      String temp = (String) n.f1.accept(this, argu);

      return (R) ("HALLOCATE "+temp);
      // return _ret;
   }

   /**
    * f0 -> Operator()
    * f1 -> Exp()
    * f2 -> Exp()
    */
   public R visit(BinOp n, A argu) {
      R _ret=null;
      is_hstore = false;
      String opr = (String) n.f0.accept(this, argu);
      String temp1 = (String) n.f1.accept(this, argu);
      String temp2 = (String) n.f2.accept(this, argu);

      return (R) (opr+" "+temp1+" "+temp2);
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
    * f0 -> "TEMP"
    * f1 -> IntegerLiteral()
    */
   public R visit(Temp n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      String int_ = (String) n.f1.accept(this, argu);
      return (R) ("TEMP "+int_);
      // return _ret;
   }

   /**
    * f0 -> <INTEGER_LITERAL>
    */
   public R visit(IntegerLiteral n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return (R) n.f0.toString();
      // return _ret;
   }

   /**
    * f0 -> <IDENTIFIER>
    */
   public R visit(Label n, A argu) {          // For Label
      R _ret=null;
      n.f0.accept(this, argu);
      if(!is_hstore){
        System.out.println(n.f0.toString());  
        // is_hstore_label = true;
      }
      else{
        // is_hstore = false;
        is_hstore_label = true;
        return (R) n.f0.toString();        
      }
      

      // return (R) n.f0.toString();
      return _ret;
   }

}