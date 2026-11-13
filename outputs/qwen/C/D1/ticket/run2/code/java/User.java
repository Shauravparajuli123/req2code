/** Generated from shared model D1/ticket. Source: R1, R5, R6, R7, R8, R10, R49, R53 */
public class User {
    private java.lang.String name;
    private java.time.LocalDate dateOfBirth;
    private java.lang.String email;
    private java.lang.String address;
    private java.lang.String preferences;
    private java.lang.String bankAccount;
    private java.lang.String favoriteEvents;
    private Preference preference;
    private java.util.List<Ticket> tickets;

    /** Realizes UC1 "Save Information" (R1). */
    public void saveInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC2 "Edit Information" (R7). */
    public void editInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC3 "See Preference" (R5). */
    public void seePreference() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC5 "See History" (R8). */
    public void seeHistory() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC31 "Change Password" (R6). */
    public void changePassword() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC32 "Favorite Event" (R53). */
    public void favoriteEvent() {
        throw new UnsupportedOperationException();
    }
}
