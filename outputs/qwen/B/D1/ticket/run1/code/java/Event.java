/** Generated from shared model D1/ticket. Source: R11, R19, R23, R28, R30, R31, R32, R33, R46, R47, R49, R52 */
public class Event {
    private java.lang.String name;
    private java.time.LocalDate date;
    private java.lang.String artist;
    private java.lang.String venue;
    private java.lang.String description;
    private java.lang.String type;
    private double price;
    private java.util.List<Ticket> tickets;

    /** Realizes UC7 "See Event" (R11, R19, R46, R47). */
    public void seeEvent() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC6 "See Overview" (R9). */
    public void seeOverview() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC29 "See Seat" (R21, R22). */
    public void seeSeat() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC30 "See Type" (R23). */
    public void seeType() {
        throw new UnsupportedOperationException();
    }
}
