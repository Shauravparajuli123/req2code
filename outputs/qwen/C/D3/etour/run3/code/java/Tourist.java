/** Generated from shared model D3/etour. Source: UC15, UC16 */
public class Tourist {
    private int id;
    private boolean authenticated;
    private Feedback feedback;
    private Bookmark bookmark;
    private Site site;
    private Statistic statistic;

    /** Realizes UC15 "Change Data" (UC15, UC23). */
    public void changeData() {
        throw new UnsupportedOperationException();
    }

    /** Realizes UC16 "Delete Account" (UC16). */
    public void deleteAccount() {
        throw new UnsupportedOperationException();
    }
}
