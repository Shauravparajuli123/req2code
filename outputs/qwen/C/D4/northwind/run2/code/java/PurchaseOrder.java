/** Generated from shared model D4/northwind. Source: FR-POP-01, FR-POP-02, FR-POP-03, FR-POP-04, FR-POP-05, FR-POP-06, FR-POP-07, FR-POP-08 */
public class PurchaseOrder {
    private java.time.LocalDate date;
    private java.lang.String vendor;
    private java.lang.String employee;
    private java.lang.String approver;
    private java.lang.String status;
    private java.lang.String details;
    private java.util.List<PurchaseOrderDetailItem> purchaseOrderDetailItems;

    /** Operation. */
    public void addDetail() {
        throw new UnsupportedOperationException();
    }

    /** Operation. */
    public void removeDetail() {
        throw new UnsupportedOperationException();
    }

    /** Operation. */
    public void updateStatus() {
        throw new UnsupportedOperationException();
    }
}
