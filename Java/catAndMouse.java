import java.lang.Math;

class catAndMouse{
    public static void main(String[] args) {
        int catM[] = [1, 3, 2];
        System.out.print(catMouse(catM));
    }
    
    public int catMouse(int cat1, int cat2, int mouse ) {
       if (math.lang.Math.abs(cat1 - mouse) == math.lang.Math.abs(cat2 - mouse)) {
            return "Mouse C";
        } else if(java.lang.Math.abs(cat1 - mouse) < java.lang.Math.abs(cat2 - mouse)) {
            return "Cat A";
        } else {
            return "Cat B";
        }
    }
}