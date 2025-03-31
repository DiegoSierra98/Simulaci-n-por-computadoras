from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Definición de argumentos por defecto para el DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Creación del DAG
dag = DAG(
    'ejemplo_dag',
    default_args=default_args,
    description='Un ejemplo sencillo de DAG en Apache Airflow',
    schedule_interval=timedelta(days=1),
)

# Tarea 1: Imprimir la fecha actual
tarea1 = BashOperator(
    task_id='imprimir_fecha',
    bash_command='date',
    dag=dag,
)

# Tarea 2: Ejecutar un retardo de 5 segundos
tarea2 = BashOperator(
    task_id='dormir',
    bash_command='sleep 5',
    dag=dag,
)

# Tarea 3: Imprimir un mensaje
tarea3 = BashOperator(
    task_id='imprimir_mensaje',
    bash_command='echo "Airflow es genial!"',
    dag=dag,
)

# Definición de las dependencias entre tareas
tarea1 >> tarea2 >> tarea3
