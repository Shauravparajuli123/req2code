/** Generated from shared model D4/northwind. Source: FR-SOP-01 */
public class Order {
    private java.lang.String customer;
    private java.lang.String employee;
    private java.lang.String orderStatus;
    private java.lang.String shipper;
    private double taxRate;
    private java.lang.String taxStatus;
    private java.time.LocalDate invoiceDate;
    private java.lang.String paymentMethod;
    private java.time.LocalDate paymentDate;
    private java.lang.String orderDetails;
    private OrderDetailItem orderDetailItem;

    /** Operation. */
    public void addOrderDetail() {
        throw new UnsupportedOperationException();
    }
}
