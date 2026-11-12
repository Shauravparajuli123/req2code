/** Generated from shared model D1/sports. Source: R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R40, R49, R57, R60, R61 */
public class Trainer {
    private java.lang.String name;
    private java.lang.String lessonSchedule;
    private java.time.LocalDate lessonTime;
    private java.lang.String lessonDescription;
    private java.lang.String lessonRoom;
    private java.lang.String lessonType;
    private int maxPeopleAllowed;
    private java.lang.String pastLessons;
    private boolean canEditLessons;
    private java.time.LocalDate lessonTimeEdited;
    private java.lang.String lessonRoomEdited;
    private java.lang.String lessonDescriptionEdited;
    private int lessonMaxPeopleEdited;
    private boolean lessonCanceled;
    private boolean checkInStatus;

    /** Realizes UC12 "Admin Add Trainer" (R47). */
    public void addLesson() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC9 "Admin Edit Lesson" (R38). */
    public void editLesson() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC11 "Admin View Schedule" (R32). */
    public void viewSchedule() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC7 "Admin Cancel Lesson" (R40). */
    public void cancelLesson() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC17 "Trainer Check In" (R60). */
    public void checkIn() {
        throw new UnsupportedOperationException();
    }
}
