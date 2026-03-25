"""Empleo en Latinoamérica: Base de Datos por País con Evolución 2000-2020 (cada 5 años). DOI: 10.6084/
DOI: https://github.com/juanmoisesd/empleo-latinoamerica-base-de-datos-por-pais-evolucion-2000-2020 | GitHub: https://github.com/juanmoisesd/empleo-latinoamerica-base-de-datos-por-pais-evolucion-2000-2020"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/empleo-latinoamerica-base-de-datos-por-pais-evolucion-2000-2020".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). Empleo en Latinoamérica: Base de Datos por País con Evolución 2000-2020 (cada 5 . Zenodo. https://github.com/juanmoisesd/empleo-latinoamerica-base-de-datos-por-pais-evolucion-2000-2020'
def info(): print(f"Dataset: Empleo en Latinoamérica: Base de Datos por País con Evolución 2000-2020 (cada 5 \nDOI: https://github.com/juanmoisesd/empleo-latinoamerica-base-de-datos-por-pais-evolucion-2000-2020\nGitHub: https://github.com/juanmoisesd/empleo-latinoamerica-base-de-datos-por-pais-evolucion-2000-2020")