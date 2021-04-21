from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M: %S %Z%z"
# obtiene la hora actual in UTC
nowUtc = datetime.now(timezone('UTC'))
print(nowUtc)

nowEst = nowUtc.astimezone(timezone('America/Santiago'))
print('Santiago: ', nowEst)

now_berlin = nowUtc.astimezone(timezone('Europe/Berlin'))
print('Berlin: ', now_berlin)