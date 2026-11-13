/** Generated from shared model D1/school. Source: R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17 */
public class Student {
    private java.lang.String teacher;
    private java.lang.String mentor;
    private java.lang.String class_;
    private java.time.LocalDate dueDate;
    private java.util.List<Teacher> teachers;
    private java.util.List<Notification> notifications;
    private Timetable timetable;
    private DLM dLM;

    /** Realizes UC1 "Direct Message" (R1, R27, R28, R6, R7). */
    public void directMessage() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC6 "Hand Homework" (R8). */
    public void handHomework() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC7 "View Timetable" (R9). */
    public void viewTimetable() {
        throw new UnsupportedOperationException();
    }

    /** Operation. */
    public void viewDLM() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC3 "Receive Notification" (R11, R12, R13, R18, R19, R3, R34, R43, R53, R54). */
    public void receiveNotification() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC8 "View Account Information" (R15). */
    public void viewAccountInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC9 "View Contact Information" (R16). */
    public void viewContactInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC10 "Change Preferences" (R17). */
    public void changePreferences() {
        throw new UnsupportedOperationException();
    }
}
