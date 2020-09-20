/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ace.j.automobiles;

import java.math.BigDecimal;
import java.util.Calendar;
import java.util.Date;
import java.util.Objects;

/**
 *
 * @author Tata
 */
public class Vehicle {
    private String model;
    private String maker;
    private String color;
    private String description;
    private Date makeDate;
    private BigDecimal cost;
    private double maxSpeed;
    private boolean isManual;
    private boolean hasGPS;
    private String useCase;
    private short numWheels;

    public Vehicle() {
        this.makeDate = Calendar.getInstance().getTime();
        this.numWheels = 4;
        this.hasGPS = false;
        this.isManual = true;
    }

    public Vehicle(String model, String maker, String color, double maxSpeed, boolean isManual, boolean hasGPS, String useCase) {
        this.model = model;
        this.maker = maker;
        this.color = color;
        this.maxSpeed = maxSpeed;
        this.isManual = isManual;
        this.hasGPS = hasGPS;
        this.useCase = useCase;
        this.makeDate = Calendar.getInstance().getTime();
        this.numWheels = 4;
        this.hasGPS = true;
        this.isManual = false;
    }

    
    
    
    public Vehicle(String model, String maker, String color, String description, Date makeDate, BigDecimal cost, double maxSpeed, boolean isManual, boolean hasGPS, String useCase, short numWheels) {
        this.model = model;
        this.maker = maker;
        this.color = color;
        this.description = description;
        this.makeDate = makeDate;
        this.cost = cost;
        this.maxSpeed = maxSpeed;
        this.isManual = isManual;
        this.hasGPS = hasGPS;
        this.useCase = useCase;
        this.numWheels = numWheels;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getMaker() {
        return maker;
    }

    public void setMaker(String maker) {
        this.maker = maker;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Date getMakeDate() {
        return makeDate;
    }

    public void setMakeDate(Date makeDate) {
        this.makeDate = makeDate;
    }

    public BigDecimal getCost() {
        return cost;
    }

    public void setCost(BigDecimal cost) {
        this.cost = cost;
    }

    public double getMaxSpeed() {
        return maxSpeed;
    }

    public void setMaxSpeed(double maxSpeed) {
        this.maxSpeed = maxSpeed;
    }

    public boolean isIsManual() {
        return isManual;
    }

    public void setIsManual(boolean isManual) {
        this.isManual = isManual;
    }

    public boolean isHasGPS() {
        return hasGPS;
    }

    public void setHasGPS(boolean hasGPS) {
        this.hasGPS = hasGPS;
    }

    public String getUseCase() {
        return useCase;
    }

    public void setUseCase(String useCase) {
        this.useCase = useCase;
    }

    public short getNumWheels() {
        return numWheels;
    }

    public void setNumWheels(short numWheels) {
        this.numWheels = numWheels;
    }

    @Override
    public String toString() {
        return "Vehicle{" + "model=" + model + ", maker=" + maker + ", color=" + color + ", description=" + description + ", makeDate=" + makeDate + ", cost=" + cost + ", maxSpeed=" + maxSpeed + ", isManual=" + isManual + ", hasGPS=" + hasGPS + ", useCase=" + useCase + ", numWheels=" + numWheels + '}';
    }

    @Override
    public int hashCode() {
        int hash = 5;
        hash = 67 * hash + Objects.hashCode(this.model);
        hash = 67 * hash + Objects.hashCode(this.maker);
        hash = 67 * hash + Objects.hashCode(this.color);
        hash = 67 * hash + Objects.hashCode(this.makeDate);
        hash = 67 * hash + Objects.hashCode(this.cost);
        hash = 67 * hash + (int) (Double.doubleToLongBits(this.maxSpeed) ^ (Double.doubleToLongBits(this.maxSpeed) >>> 32));
        hash = 67 * hash + (this.isManual ? 1 : 0);
        hash = 67 * hash + (this.hasGPS ? 1 : 0);
        hash = 67 * hash + this.numWheels;
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Vehicle other = (Vehicle) obj;
        if (Double.doubleToLongBits(this.maxSpeed) != Double.doubleToLongBits(other.maxSpeed)) {
            return false;
        }
        if (this.isManual != other.isManual) {
            return false;
        }
        if (this.hasGPS != other.hasGPS) {
            return false;
        }
        if (this.numWheels != other.numWheels) {
            return false;
        }
        if (!Objects.equals(this.model, other.model)) {
            return false;
        }
        if (!Objects.equals(this.maker, other.maker)) {
            return false;
        }
        if (!Objects.equals(this.cost, other.cost)) {
            return false;
        }
        return true;
    }
    
    
        
    
    
}
