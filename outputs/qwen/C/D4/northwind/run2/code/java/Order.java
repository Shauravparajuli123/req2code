/** Generated from shared model D4/northwind. Source: FR-SOP-01, FR-SOP-02, FR-SOP-03, FR-SOP-04, FR-SOP-05, FR-SOP-06, FR-SOP-07, FR-SOP-08, FR-SOP-09, FR-SOP-10 */
public class Order {
    private java.time.LocalDate date;
    private java.lang.String customer;
    private java.lang.String employee;
    private java.lang.String status;
    private java.lang.String shipper;
    private double taxRate;
    private java.lang.String taxStatus;
    private java.time.LocalDate invoiceDate;
    private java.lang.String paymentMethod;
    private java.time.LocalDate paymentDate;
    private java.lang.String details;
    private java.util.List<OrderDetailItem> orderDetailItems;

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
