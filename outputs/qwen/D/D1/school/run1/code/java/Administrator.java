/** Generated from shared model D1/school. Source: R47, R48, R49, R50, R51, R52, R53, R54, R55, R56 */
public class Administrator {
    private java.util.List<Student> students;
    private java.util.List<Teacher> teachers;
    private java.util.List<Guardian> guardians;
    private Notification notification;
    private Schedule schedule;
    private Class class_;
    private Account account;
    private Dashboard dashboard;
    private java.util.List<Message> messages;

    /** Realizes UC33 "Send Direct Message" (R48). */
    public void sendDirectMessage() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC34 "Assign Schedules" (R49). */
    public void assignSchedules() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC35 "Create Account" (R50). */
    public void createAccount() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC36 "Edit Account Data" (R51). */
    public void editAccountData() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC37 "Change Dashboard View" (R52). */
    public void changeDashboardView() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC3 "Receive Notification" (R12, R18, R19, R27, R3, R44, R53, R54). */
    public void receiveNotification() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC38 "Register Changes" (R55). */
    public void registerChanges() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC39 "Register Absence" (R56). */
    public void registerAbsence() {
        throw new UnsupportedOperationException();
    }
}
