class Factorial{
    public static void main(String[] a){
        System.out.println(new Fac().ComputeFac(10));
    }
}

class Fac {
    public int ComputeFac(int num){
        int num_aux ;
        int[] num_arr;
        boolean flag;
        num_aux = 3;
        num_arr[3] = 4;
        num_arr[4] = 5/3;
        num_arr[3] = num_arr[12];
        flag = true;
        flag = true || true;
        while(true)
        {
        	num_aux = this.ComputeFac(num_aux-1);
        	num_aux = num_aux * (this.ComputeFac(num_aux-1)) ;
        }
        return num_aux ;
    }
}


class A extends B{
	A a;
	B b;
	public int abc(){
		b = a;
		return 3;
	}
}

class B extends C{
	public int check_func(int num, int num, int num){

		return 0;
	}
}

class C extends D{
	public int check_func(int num, int num2, int num3){

		return 0;
	}
}

class D extends Fac{

	public int check_func(int num, int num2, int num3){

		return 0;
	}
}