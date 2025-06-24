package Day87;

public class BankAccount {
    // write the code of bank account class here

    String accountNumber;
    int balance;
    double roi;

    double getSimpleInterest(int years){
        return (this.balance*this.roi*years)/100;
    }

    double getBalanceWithInterest(int years){
        return this.balance + (this.balance*this.roi*years)/100;
    }
}



