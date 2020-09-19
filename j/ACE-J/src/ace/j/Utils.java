package ace.j;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Tata
 */
public class Utils {
    public enum LEVELS{
        LEVEL_1(1),
        LEVEL_2(2),
        LEVEL_3(3),
        LEVEL_4(4),
        LEVEL_5(5),
        UNKNOWN(0);
        
        private final int level;
        
        LEVELS(int l){
            if(l < 1){
                this.level = 0;
            }else{
                this.level = l;
            }            
        }

        @Override
        public String toString() {
            return "LEVEL_" + this.level;
        }
        
        
        
    }
    
    public enum SPECIALITIES{
        ACCOUNTANT("Accountant"),
        SCIENTIST("Scientist");

        private final String value;
        
        private SPECIALITIES(String s) {
            this.value = s;
        }
        
        
    }
    
    public static enum VEHICLE_KIND{
        INDUSTRIAL,
        SUV,
        LIMOSINE,
        
        
    }
}
