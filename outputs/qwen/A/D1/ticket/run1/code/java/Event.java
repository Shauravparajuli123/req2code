/** Generated from shared model D1/ticket. Source: R19, R20, R21, R22, R23, R24, R25, R26, R46, R47, R48, R52, R53, R54 */
public class Event {
    private java.lang.String name;
    private java.time.LocalDate date;
    private java.lang.String location;
    private java.lang.String artist;
    private java.lang.String type;
    private double price;
    private java.lang.String venue;
    private java.lang.String genre;
    private java.lang.String ticketType;
    private java.lang.String seats;
    private java.lang.String description;
    private java.util.List<Ticket> tickets;

    /** Realizes UC10 "View Event Information" (R11, R49, R50, R51, R52, R53, R54). */
    public void viewEventInformation() {
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
    public void viewEventPage() {
        throw new UnsupportedOperationException();
    }
}
