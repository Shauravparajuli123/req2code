/** Generated from shared model D2/SimpleAirlineDomain. Source: R2, R6, R7, R9 */
public class Flight extends Airplane {
    private int maxNumberOfPassengers;
    private java.time.LocalTime departureTime;
    private java.lang.String originAirport;
    private java.util.List<Airport> airports;
    private Passenger passenger;
    private Time time;

    /** Operation. */
    public void createFlight() {
        throw new UnsupportedOperationException();
    }
}
