/** Generated from shared model D4/northwind. Source: FR-PM-01, FR-PM-02, FR-PM-03, FR-PM-04, FR-PM-05, FR-PM-06, FR-PM-07 */
public class Product {
    private java.lang.String productCode;
    private java.lang.String name;
    private java.lang.String description;
    private double price;
    private double unitCost;
    private double retailPrice;
    private int reorderLevel;
    private int targetLevel;
    private int minimumReorderQuantity;
    private boolean discontinued;
    private ProductCategory productCategory;

    /** Operation. */
    public void associateVendor() {
        throw new UnsupportedOperationException();
    }
}
