import syntaxtree.*;
import visitor.*;

public class P4 {
   public static void main(String [] args) {
      try {
         Node root = new MiniIRParser(System.in).Goal();
         root.accept(new GJDepthFirst(), null);
         root.accept(new GJDepthFirstCopy1(), null);
      }
      catch (ParseException e) {
         System.out.println(e.toString());
      }
   }
} 


