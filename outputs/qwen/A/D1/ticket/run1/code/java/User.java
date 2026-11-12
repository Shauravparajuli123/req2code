/** Generated from shared model D1/ticket. Source: R1, R5, R6, R7, R8, R9, R35, R36, R37, R38, R39, R40 */
public class User {
    private java.lang.String name;
    private java.time.LocalDate dateOfBirth;
    private java.lang.String email;
    private java.lang.String address;
    private java.lang.String preferences;
    private java.lang.String paymentDetails;
    private java.lang.String password;
    private java.lang.String favoriteArtists;
    private java.lang.String favoriteEvents;
    private java.lang.String ticketHistory;
    private java.lang.String profileSurvey;
    private java.util.List<Ticket> tickets;

    /** Realizes UC1 "Create Profile" (R1, R5, R6, R7, R15, R16, R17). */
    public void createProfile() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC2 "View Personal Information" (R5, R7, R17). */
    public void viewPersonalInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC3 "Edit Personal Information" (R7, R17). */
    public void editPersonalInformation() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC4 "View Ticket History" (R8, R17). */
    public void viewTicketHistory() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC5 "View Upcoming Events" (R9, R17). */
    public void viewUpcomingEvents() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC6 "Favorite Events Or Artists" (R10, R17, R53). */
    public void favoriteEventsOrArtists() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC7 "Search For Events" (R11, R18, R28, R29, R30, R31, R32, R33, R46, R47, R48, R53). */
    public void searchForEvents() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC8 "Buy Tickets" (R12, R18, R19, R20, R21, R22, R23, R24, R25, R26, R17). */
    public void buyTickets() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC9 "Resell Tickets" (R35, R36, R37, R38, R39, R40, R41, R42, R43, R45). */
    public void resellTickets() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC10 "View Event Information" (R11, R49, R50, R51, R52, R53, R54). */
    public void viewEventInformation() {
        throw new UnsupportedOperationException();
    }
}
