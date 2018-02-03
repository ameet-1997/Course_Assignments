import java.util.*;

public class test {
	public static void main(String[] args){
		LinkedList<String> a = new LinkedList<String>();
		String temp = "oslab_projects";

		for(int i=0;i<1024*1024*8;++i){
			a.add(temp);
		}

		System.out.println("Done");
	}
}
