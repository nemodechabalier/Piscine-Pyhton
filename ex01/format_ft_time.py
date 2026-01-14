import time
from datetime import datetime

seconds = time.time()
# Affichage du timestamp formaté
print(
    f"Seconds since January 1, 1970: "
    f"{seconds:,.4f} or {seconds:.2e} in scientific notation"
)

# Date formatée
date = datetime.fromtimestamp(seconds)
print(date.strftime("%b %d %Y"))