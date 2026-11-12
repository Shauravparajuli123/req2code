/** Generated from shared model D1/sports. Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R51, R52, R53, R54, R55, R56, R58, R59 */
public class Customer {
    private java.lang.String name;
    private java.lang.String personalInformation;
    private java.lang.String bankingDetails;
    private java.lang.String membershipType;
    private java.time.LocalDate subscriptionEndDate;
    private boolean previousInformation;
    private boolean isSubscribed;
    private java.lang.String password;
    private java.lang.String personalDetails;
    private java.lang.String paymentDetails;
    private java.lang.String familyMembers;
    private boolean familyMembership;
    private java.lang.String availableLessons;
    private java.lang.String bookedLessons;
    private java.lang.String lessonHistory;
    private boolean lessonBooked;
    private boolean lessonCanceled;
    private java.lang.String notificationMethod;
    private java.lang.String preferredNotifications;
    private boolean lessonCanceledNotification;
    private boolean checkInStatus;
    private boolean subscriptionStatus;

    /** Realizes UC1 "Create Account" (R1, R2, R3, R4, R5, R6, R7). */
    public void createAccount() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC2 "Manage Personal Information" (R10, R11, R12, R13, R14, R58, R59). */
    public void managePersonalInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC3 "Book Lessons" (R15, R16, R17, R23, R24, R50, R51, R52, R53, R54, R55, R56, R57). */
    public void bookLessons() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC4 "Call Gym To Book Lesson" (R21, R22). */
    public void callGymToBookLesson() {
        throw new UnsupportedOperationException();
    }

    /** Operation. */
    public void callGymToCancelLesson() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC5 "Book Personal Training Session" (R21, R22). */
    public void bookPersonalTrainingSession() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC6 "Cancel Lesson" (R39). */
    public void cancelLesson() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC8 "Edit Lesson" (R33, R34, R35, R36, R37). */
    public void editLesson() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC10 "View Schedule" (R32). */
    public void viewSchedule() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC16 "Customer Check In" (R61, R62). */
    public void checkIn() {
        throw new UnsupportedOperationException();
    }

    /** Operation. */
    public void adminCheckIn() {
        throw new UnsupportedOperationException();
    }
}
