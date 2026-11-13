/** Generated from shared model D1/grocery. Source: R36, R37 */
public class Message {
    private java.lang.String sender;
    private java.lang.String receiver;
    private java.lang.String content;
    private java.lang.String status;
    private Application application;

    /** Realizes UC24 "Message Other Employees" (R36). */
    public void sendMessage() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC25 "Forward Messages" (R37). */
    public void forwardMessage() {
        throw new UnsupportedOperationException();
    }
}
