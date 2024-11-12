Feature: Invoice Details

  Background:
    Given user login with username "demouser" and password "abc123"

  Scenario Outline: Validate invoice details
    When user clicks in first invoice details
    Then Invoice Details Page is open
    And Hotel Name must be "<HotelName>"
    And Invoice Date must be "<InvoiceDate>"
    And Due Date must be "<DueDate>"
    And Invoice Number must be "<InvoiceNumber>"
    And Booking Code must be "<BookingCode>"
    And Customer Details must be "<CustomerDetails>"
    And Room must be "<Room>"
    And Check In must be "<CheckIn>"
    And Check Out must be "<CheckOut>"
    And Total Stay Count must be "<TotalStayCount>"
    And Total Stay Amount must be "<TotalStayAmount>"
    And Deposit Now must be "<DepositNow>"
    And Tax & VAT must be "<Tax&VAT>"
    And Total Amount must be "<TotalAmount>"
    Examples:
      | HotelName       | InvoiceDate | DueDate   | InvoiceNumber | BookingCode | CustomerDetails                       | Room            | CheckIn   | CheckOut  | TotalStayCount | TotalStayAmount | DepositNow | Tax&VAT    | TotalAmount |
      | Rendezvous Hotel| 14/01/2018  | 15/01/2018| 110           | 0875        | JOHNY SMITHR2, AVENUE DU MAROC 123456 | Superior Double | 14/01/2018| 15/01/2018| 1              | $150            | USD $20.90 | USD $19.00 | USD $209.00 |