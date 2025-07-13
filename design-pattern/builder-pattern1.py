class sqlQueryBuilder:
    def __init__(self):
        self._select = []
        self._table = None
        self._where = []
        self._limit= None
        self._order_by = None
    def select(self,*feilds):
        self._select.extend(feilds)
        return self
    def from_table(self,name):
        self._table = name
        return self
    def where(self,condtion):
        self._where.append(condtion)
        return self
    def limit(self,num):
        self._limit = num
        return self
    def order_by(self,order):
        self._order_by = order
        return self
    def build(self):
        if not self._select or not self._table:
            raise ValueError("SELECT fields and FROM table must be provided")

        query = f"SELECT {', '.join(self._select)} FROM {self._table}"

        if self._where:
            query += f" WHERE {' AND '.join(self._where)}"

        if self._order_by:
            query += f" ORDER BY {self._order_by}"

        if self._limit is not None:
            query += f" LIMIT {self._limit}"

        return query + ";"

query = (sqlQueryBuilder()
         .select('id','name')
         .from_table('users')
         .where("age > 10")
         .order_by("desc")
         .limit(100)
         .build())
print(query)
    