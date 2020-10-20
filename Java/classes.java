/*Write a Java program which creates a class named 'Employee' having the following members: 
Name, Age, Phone number, Address, Salary. It also has a method named 'printSalary( )' 
which prints the salary of the Employee. Two classes 'Officer' and 'Manager' inherits the 'Employee' class. 
The 'Officer' and 'Manager' classes have data members 'specialization' and 'department' respectively. 
Now, assign name, age, phone number, address and salary to an officer and a manager 
by making an object of both of these classes and print the same. */

class Employee{
    String Name,Address,phone;
    double age,sal;
    void printSalary()
    {
        System.out.print(sal);
    }

}
class Officer extends Employee{
    String Specialization;
}
class Manager extends Employee{
    String Department;

}

public class classes
{
public static void  main(String args[])
{
    Officer o1=new Officer();
    Manager m1=new Manager();
    o1.Address="Vaduthala";
    o1.Name="Suresh";
    o1.age=25;
    o1.phone="9188068688";
    o1.sal=60000;
    o1.Specialization="Designer";
    m1.Address="Kakkanad";
    m1.Name="Sita";
    m1.age=23;
    m1.phone="9496022887";
    m1.sal=45000;
    m1.Department="Marketing";
    System.out.print(o1.Name+"\t"+o1.Address+"\t"+o1.Specialization+"\t"+o1.age+"\t"+o1.phone+"\t");
    o1.printSalary();
    System.out.print("\n"+m1.Name+"\t"+m1.Address+"\t"+m1.Department+"\t"+m1.age+"\t"+m1.phone+"\t");
    m1.printSalary();



}
}
