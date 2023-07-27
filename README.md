### Projeto Alimentar+

Pros and cons of using a UUID as a primary key
Advantages:
    You can generate UUIDs everywhere
    This means that you can create records without connecting to a database
    The UUIDs are unique across tables, databases, systems
    This makes it easy to merge records from different tables, databases
    UUIDs make replication more easy

Disadvantages:
    Uses more memory and disk space, index tables get bigger
    But who cares about this today?
    Slower for SELECT with big tables
    But optimizations are possible
    Can be much slower for INSERT
    It takes more time to recalculate the index, can be a serious problem
    More difficult to debug because of missing insert order
    But you can add a DATETIME (microseconds) 'created_on' column and use this to sort.