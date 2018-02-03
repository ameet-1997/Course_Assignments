import syntaxtree.*;
import visitor.*;

public class Main {
   public static void main(String [] args) {
      try {
         Node root = new MiniJavaParser(System.in).Goal();
         Object table = root.accept(new GJDepthFirst(), null); // Your assignment part is invoked here.
         root.accept(new GJDepthFirstCopy1(), table);
         System.out.println("Program type checked successfully");
      }
      catch (ParseException e) {
         System.out.println(e.toString());
      }
   }
}