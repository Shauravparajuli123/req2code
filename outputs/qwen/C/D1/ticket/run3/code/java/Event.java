/** Generated from shared model D1/ticket. Source: R11, R19, R23, R28, R29, R30, R31, R32, R33, R46, R47, R49, R50, R51, R52, R53, R54 */
public class Event {
    private java.lang.String name;
    private java.time.LocalDate date;
    private java.lang.String artist;
    private java.lang.String venue;
    private java.lang.String type;
    private java.lang.String description;
    private java.lang.String link;
    private java.util.List<Ticket> tickets;

    /** Realizes UC3 "See Event" (R11, R19, R46, R47). */
    public void seeEvent() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC20 "Click Event" (R48). */
    public void clickEvent() {
        throw new UnsupportedOperationException();
    }
}
