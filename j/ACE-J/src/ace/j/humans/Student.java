/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ace.j.humans;
import ace.j.Utils.LEVELS;


/**
 *
 * @author Tata
 */
public class Student {
    private String firstName;
    private String surname;    
    private LEVELS level;
    private String matricule;
    private String speciality;

    public Student() {
    }

    public Student(String firstName, String surname, LEVELS level, String matricule, String speciality) {
        this.firstName = firstName;
        this.surname = surname;
        this.level = level;
        this.matricule = matricule;
        this.speciality = speciality;
    }



    @Override
    public String toString() {
        return "Student{" + "firstName=" + firstName + ", surname=" + surname + ", level=" + level + ", matricule=" + matricule + ", speciality=" + speciality + '}';
    }
    
    
    
    
    
    

    
}
