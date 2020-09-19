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
public class Rectangle {
    private double length;
    private double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }
    
    
    
    public boolean isSquare(){
        return this.length == this.width;
    }
    
    public double area(){
        return this.length * this.width;
    }
    
    public double perimeter(){
        return (2 * this.length) + (2 * this.width);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        //String squareTxt = "Square";
        String kind = this.isSquare() ? "Square" : "Rectangle";
        sb.append(kind +  "{" + "length=" + length + ", width=" + width + "}\n");
        sb.append("----------------------------------------------\n");
        sb.append("\nArea : " + this.area());
        sb.append("\nPerimeter : " + this.perimeter() );
        return sb.toString();
    }
    
    
    
}
