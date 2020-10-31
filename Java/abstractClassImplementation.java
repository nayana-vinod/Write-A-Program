/*Write a java program to create an abstract class named Shape that contains an empty 
method named numberOfSides( ). Provide three classes named Rectangle, Triangle and Hexagon 
such that each one of the classes extends the class Shape. Each one of the classes contains only 
the method numberOfSides( ) that shows the number of sides in the given geometrical structures. 
(Exercise to understand polymorphism). */

abstract class shape{
    abstract void numberOfSides();
}
class Rectangle extends shape{
    void numberOfSides()
    {
        System.out.print("Rectangle : 4");
    }
}
class Triangle extends shape{
    void numberOfSides()
    {
        System.out.print("\nTriangle : 3");
    }
}
class Hexagon extends shape{
    void numberOfSides()
    {
        System.out.print("\nHexagon : 6");
    }
}
public class poly{
    public static void main(final String[] args)
     {
        Rectangle r1=new Rectangle();
        Triangle t1=new Triangle();
        Hexagon h1=new Hexagon();

        r1.numberOfSides();
        t1.numberOfSides();
        h1.numberOfSides();
    }
}
