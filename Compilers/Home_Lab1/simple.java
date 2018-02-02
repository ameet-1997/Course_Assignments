#define NUM() (10+0)
#define ONE() (0+1)
#define abc(x,y) (x*y)
#define def(x,y,z) (x+(y+z))

class Factorial{
    public static void main(String[] a){
        System.out.println(new Fac().ComputeFac(NUM()));
    }
}

class Fac {
    public int ComputeFac(int num){
        int num_aux ;
        if ((num <= 1)&&(num != 1))
            num_aux = ONE() ;
        else
            num_aux = num * (this.ComputeFac(num-1)) ;

    	if(num <= 1)
    	{
    		x = def(3,4,5);
    	}
        return num_aux ;
    }
}