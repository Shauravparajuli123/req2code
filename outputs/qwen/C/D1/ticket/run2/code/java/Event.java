/** Generated from shared model D1/ticket. Source: R11, R12, R13, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51, R52, R53, R54 */
public class Event {
    private java.lang.String name;
    private java.time.LocalDate date;
    private java.lang.String artist;
    private java.lang.String venue;
    private java.lang.String type;
    private double price;
    private java.lang.String description;
    private java.util.List<Ticket> tickets;

    /** Realizes UC7 "See Event" (R11, R19, R46, R47). */
    public void seeEvent() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC11 "Click Event" (R48). */
    public void clickEvent() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC29 "See Seat" (R21, R22). */
    public void seeAvailableSeats() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC30 "See Type" (R23). */
    public void seeType() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC27 "Add Ticket" (R24). */
    public void addTicketToCart() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC28 "See Order Summary" (R25). */
    public void seeOrderSummary() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC15 "Sort Search Result" (R31). */
    public void sortSearchResults() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC14 "Filter Search Result" (R33). */
    public void filterSearchResults() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC6 "See Overview" (R9). */
    public void seeUpcomingEvents() {
        throw new UnsupportedOperationException();
    }
}
