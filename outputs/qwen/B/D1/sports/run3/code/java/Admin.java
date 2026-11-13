/** Generated from shared model D1/sports. Source: R20, R38, R47, R48, R49, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59, R62, R63 */
public class Admin {
    private java.lang.String name;
    private java.lang.String notifications;
    private java.lang.String subscriptions;
    private java.lang.String trainer;
    private java.lang.String lessonSchedule;
    private boolean lessonEdit;
    private boolean lessonCancel;
    private java.lang.String lessonNotification;

    /** Realizes UC31 "Edit Any Lesson" (R38). */
    public void editLesson() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC32 "Cancel Lesson" (R39, R40). */
    public void cancelLesson() {
        throw new UnsupportedOperationException();
    }
}
