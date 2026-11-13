/** Generated from shared model D2/SimpleAirlineDomain. Source: R2, R6, R7, R9, R10 */
public class Flight {
    private int maxNumberOfPassengers;
    private java.time.LocalTime departureTime;
    private java.lang.String originAirport;
    private java.lang.String passengers;
    private java.util.List<Airport> airports;
    private Time time;
    private Airplane airplane;

    /** Operation. */
    public void addPassenger() {
        throw new UnsupportedOperationException();
    }

    /** Operation. */
    public void removePassenger() {
        throw new UnsupportedOperationException();
    }
}
