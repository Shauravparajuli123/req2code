/** Generated from shared model D1/grocery. Source: R1, R6, R7, R13, R15, R47, R48 */
public class Employee {
    private java.lang.String name;
    private java.lang.String certificate;
    private java.lang.String status;
    private java.lang.String group;
    private java.lang.String qualification;
    private SalaryStatement salaryStatement;
    private java.util.List<Notification> notifications;
    private Schedule schedule;
    private java.util.List<Complaint> complaints;

    /** Realizes UC7 "Express Working Hours" (R7). */
    public void expressWorkingHours() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC12 "View Schedule" (R13, R14). */
    public void viewSchedule() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC34 "Change Information" (R47). */
    public void changeInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC35 "View Contract" (R32). */
    public void viewContract() {
        throw new UnsupportedOperationException();
    }
}
