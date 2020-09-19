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
    private String surname;
    private String firstName;
    private LEVELS level;
    private String matricule;
    private String speciality;

    public Student() {
    }

    public Student(String surname, String firstName, LEVELS level, String matricule) {
        this.surname = surname;
        this.firstName = firstName;
        this.level = level;
        this.matricule = matricule;
    }

    public Student(String surname, String firstName, LEVELS level, String matricule, String speciality) {
        this.surname = surname;
        this.firstName = firstName;
        this.level = level;
        this.matricule = matricule;
        this.speciality = speciality;
    }

    public Student(String surname, String firstName, String matricule, String speciality) {
        this.surname = surname;
        this.firstName = firstName;
        this.matricule = matricule;
        this.speciality = speciality;
    }
    
    
    
    

    
}
