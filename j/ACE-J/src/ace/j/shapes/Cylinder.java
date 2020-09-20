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
public class Cylinder {
    private double height;
    private double radius;

    public Cylinder(double height, double radius) {
        this.height = height;
        this.radius = radius;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
    
    
    
    public double volume(){
        return baseCircleArea() * this.height;
    }
    
    public double baseCircleArea(){
        return Math.PI * Math.pow(this.radius, 2);        
    }
    
    public double baseCirclePerimeter(){
        return 2 * Math.PI * this.radius;
    }
    
    public double sideSurfaceArea(){
        return this.baseCirclePerimeter() * this.height;
    }
    
    public double totalSurfaceArea(){
        return (2 * this.baseCircleArea()) + this.sideSurfaceArea();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\nCylinder{" + "height=" + height + ", radius=" + radius + '}');
        sb.append("-----------------------------------");
        sb.append("\nTotal surface area: " + this.totalSurfaceArea());
        sb.append("\nVolume:" + this.volume());                
        return sb.toString();
    }
    
    
    
}
