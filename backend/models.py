from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
**tablename** = "users"

```
id = Column(Integer, primary_key=True)
username = Column(String(100))
email = Column(String(200))
```

class License(Base):
**tablename** = "licenses"

```
id = Column(Integer, primary_key=True)
user_id = Column(Integer)
license_type = Column(String(50))
```

class FraudLog(Base):
**tablename** = "fraud_logs"

```
id = Column(Integer, primary_key=True)
event = Column(String(500))
```

class CostReport(Base):
**tablename** = "cost_reports"

```
id = Column(Integer, primary_key=True)
provider = Column(String(50))
cost = Column(Float)
```
