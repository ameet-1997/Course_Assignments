import syntaxtree.*;
import visitor.*;

public class P6 {
   public static void main(String [] args) {
      try {
         Node root = new MiniRAParser(System.in).Goal();
         root.accept(new GJDepthFirst(), null);
         root.accept(new GJDepthFirstCopy1(), null);
         // root.accept(new GJDepthFirstCopy2(), null);
      }
      catch (ParseException e) {
         System.out.println(e.toString());
      }
   }
} 

// https://www.cs.duke.edu/courses/compsci250/current/MIPS-ASM.pdf      -         Assembly Manual
// https://tio.run/#spim                                                -         Online Interpreter