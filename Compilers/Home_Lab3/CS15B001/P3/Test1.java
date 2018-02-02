class Test1{
    public static void main(String[] a){
        System.out.println(new Fac().checking());
        // System.out.println(3);
    }
}

class Fac extends A {

    int abc;

    public int ComputeFac(int a){
    	System.out.println(1);    
        return 0;
    }

    public int checking(){
    	A id;
    	int a;
    	id = new Fac();
    	a = id.ComputeFac(1);
    	return 9999;
    }

} 

class A{

	public int trash(int b){
		return 0;
	}
	public int ComputeFac(int a){
		System.out.println(0);
		return 0;
	}
}
