/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ace.j.shapes;

/**
 *
 * @author Tata
 */
public class Circle {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
    
    public double area(){
        return Math.PI * Math.pow(this.radius, 2);
    }
    
    public double perimeter(){
        return 2 * Math.PI * this.radius;
    }
    
    public static double computeArea(double radius){
        return Math.PI * Math.pow(radius, 2);
    }

    @Override
    public String toString() {        
        StringBuilder sb = new StringBuilder();
        sb.append("\nCircle{" + "radius=" + radius + '}');
        sb.append("--------------------------");        
        sb.append("Area of circle: " + this.area());
        sb.append("Perimeter of circle: " + this.perimeter());
        sb.append("--------------------------");        
        return sb.toString();
    }
    
    
    
    
    
    
    
    
}
