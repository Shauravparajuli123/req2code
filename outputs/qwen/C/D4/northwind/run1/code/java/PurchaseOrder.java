/** Generated from shared model D4/northwind. Source: FR-POP-01 */
public class PurchaseOrder {
    private java.lang.String vendor;
    private java.lang.String employeeSubmitted;
    private java.lang.String employeeApproved;
    private java.lang.String status;
    private java.time.LocalDate orderDate;
    private java.lang.String purchaseOrderDetails;
    private Employee employee;
    private PurchaseOrderDetailItem purchaseOrderDetailItem;

    /** Operation. */
    public void addPurchaseOrderDetail() {
        throw new UnsupportedOperationException();
    }
}
