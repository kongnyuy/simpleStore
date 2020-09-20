/*
 * The MIT License
 *
 * Copyright 2020 Tata.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package ace.j;

import ace.j.humans.Student;
import ace.j.Utils.LEVELS;

import java.io.InputStream;
import java.util.Scanner;
import java.io.OutputStream;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author Tata
 */
public class Console {

    private Scanner inScanner;
    private InputStream in;
    private OutputStream out;
    private Pattern studPattern = Pattern.compile("\\w*");

    public Console() {
        this.inScanner = new Scanner(System.in);

    }

    public Student addStudent() {
        System.out.println("New Student");
        System.out.println("Format: surname, firstName, level, matricule, speciality");
        System.out.println("Example: Mida, John higs, 3, 39ssh30f09, Accountant\n");
        if (this.inScanner != null) {
            String studTxt = inScanner.nextLine();
            String[] sa = studTxt.split(",");
            return new Student(sa[0].trim(), sa[1].trim(), LEVELS.of(Integer.parseInt(sa[2].trim())), sa[3].trim(), sa[4].trim());

        }

        return null;
    }

}
