import syntaxtree.*;
import visitor.*;

public class P3 {
   public static void main(String [] args) {
      try {
         Node root = new MiniJavaParser(System.in).Goal();
         Object table = root.accept(new GJDepthFirst(), null);
         // GJDepthFirstCopy1.all_tables = GJDepthFirst.all_tables;
         root.accept(new GJDepthFirstCopy1(), null);
         // System.out.println("Program type checked successfully");
      }
      catch (ParseException e) {
         System.out.println(e.toString());
      }
   }
}