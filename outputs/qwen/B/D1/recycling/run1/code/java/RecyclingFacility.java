/** Generated from shared model D1/recycling. Source: R3, R4, R6, R10, R11, R16, R17, R20, R22, R23, R24, R26, R30, R32, R33, R34, R35, R36, R37, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R50, R51 */
public class RecyclingFacility {
    private java.lang.String name;
    private java.lang.String type;
    private java.lang.String openingHour;
    private java.lang.String location;
    private java.lang.String schedule;
    private java.lang.String material;
    private Hour hour;
    private java.util.List<Material> materials;
    private Profile profile;
    private java.util.List<Feedback> feedbacks;

    /** Realizes UC11 "Add Recycling Center Information" (R40). */
    public void addInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC30 "Onboard Recycling Center" (R42). */
    public void onboardFacility() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC14 "Communicate Site" (R51). */
    public void communicateSite() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC13 "Communicate Facility" (R47). */
    public void communicateFacility() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC7 "Handle Activity" (R30). */
    public void handleActivity() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC18 "View Dashboard" (R22, R46). */
    public void viewDashboard() {
        throw new UnsupportedOperationException();
    }

    /** Operation. */
    public void viewUserStats() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC32 "Reply User Question" (R45). */
    public void replyUserQuestion() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC34 "Update Information" (R49). */
    public void updateInformation() {
        throw new UnsupportedOperationException();
    }
}
