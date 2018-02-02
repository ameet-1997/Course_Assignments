class Test{
    public static void main(String[] a){
        System.out.println(new Fac().ComputeFac((10+0)));
        // System.out.println(3);
    }
}

class Fac extends A {

    int abc;

    public int ComputeFac(int a){
        def = this.func3(this.func2(this.func4(a)));
        return def;
    }

}

class A extends B {

    int abc;

    public int func2(int a){
        a = a*2;
        return a;
    }

}

class B extends C {

    int abc;

    public int func3(int a){
        a = a*3;
        return a;
    }

}

class C {
    int def;

    public int func4(int a){
        a = 4*a;
        return a;
    }    
}