import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# -------------------------
# CONFIG
# -------------------------

NUM_CLIENTES = 10000
NUM_PRODUCTOS = 50
NUM_TRANSACCIONES = 500000
NUM_CREDITOS = 30000
NUM_SUCURSALES = 200

start_date = datetime.now() - timedelta(days=365)

# -------------------------
# DIM CLIENTES
# -------------------------

clientes = []

for i in range(NUM_CLIENTES):
    clientes.append({
        "cliente_id": i+1,
        "nombre": fake.name(),
        "segmento": random.choice(["gold","silver","bronze"]),
        "score_credito": random.randint(300,850),
        "fecha_alta": fake.date_between(start_date='-5y', end_date='today'),
        "ciudad": fake.city()
    })

df_clientes = pd.DataFrame(clientes)

# -------------------------
# DIM PRODUCTOS
# -------------------------

productos = []

for i in range(NUM_PRODUCTOS):
    productos.append({
        "producto_id": i+1,
        "tipo_producto": random.choice(["credito","tarjeta","prestamo"]),
        "tasa_interes": round(random.uniform(0.01,0.35),2),
        "plazo_meses": random.choice([12,24,36,48])
    })

df_productos = pd.DataFrame(productos)

# -------------------------
# DIM SUCURSALES
# -------------------------

sucursales = []

for i in range(NUM_SUCURSALES):
    sucursales.append({
        "sucursal_id": i+1,
        "region": random.choice(["norte","sur","centro"]),
        "ciudad": fake.city(),
        "tipo_oficina": random.choice(["principal","secundaria"])
    })

df_sucursales = pd.DataFrame(sucursales)

# -------------------------
# FACT TRANSACCIONES
# -------------------------

transacciones = []

for i in range(NUM_TRANSACCIONES):

    monto = round(abs(np.random.normal(200,100)),2)

    # anomalías
    if random.random() < 0.01:
        monto = monto * 10

    transacciones.append({
        "transaccion_id": i+1,
        "cliente_id": random.randint(1,NUM_CLIENTES),
        "producto_id": random.randint(1,NUM_PRODUCTOS),
        "monto": monto,
        "tipo_tx": random.choice(["compra","pago","retiro"]),
        "fecha": start_date + timedelta(days=random.randint(0,365)),
        "canal": random.choice(["web","app","atm"]),
        "estado": random.choice(["ok","rechazada"])
    })

df_transacciones = pd.DataFrame(transacciones)

# -------------------------
# FACT CREDITOS
# -------------------------

creditos = []

for i in range(NUM_CREDITOS):

    monto = random.randint(1000,20000)

    creditos.append({
        "credito_id": i+1,
        "cliente_id": random.randint(1,NUM_CLIENTES),
        "producto_id": random.randint(1,NUM_PRODUCTOS),
        "monto_aprobado": monto,
        "saldo_actual": monto - random.randint(0,monto),
        "dias_mora": random.choice([0,0,0,10,20,40,90]),
        "fecha_desembolso": start_date + timedelta(days=random.randint(0,365))
    })

df_creditos = pd.DataFrame(creditos)

# -------------------------
# EXPORT
# -------------------------

df_clientes.to_csv("dim_clientes.csv",index=False)
df_productos.to_csv("dim_productos.csv",index=False)
df_transacciones.to_csv("fact_transacciones.csv",index=False)
df_creditos.to_csv("fact_creditos.csv",index=False)
df_sucursales.to_csv("dim_sucursales.csv",index=False)

print("Data generated successfully")