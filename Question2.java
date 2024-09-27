void transfer(Account from, Account to, int amount) {
    Account firstLock = from.compareTo(to) < 0 ? from : to;
    Account secondLock = from.compareTo(to) < 0 ? to : from;
    
    synchronized(firstLock) {
        synchronized(secondLock) {
            if (amount < 0) {
                throw new IllegalArgumentException("Transfer amount must be non-negative");
            }
            if (from.getBalance() < amount) {
                throw new IllegalArgumentException("Insufficient funds in the 'from' account");
            }
            from.debit(amount);
            to.credit(amount);
        }
    }
}
