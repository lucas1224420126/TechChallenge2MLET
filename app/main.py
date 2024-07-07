from fastapi import FastAPI, Depends
from .auth import get_current_user, router as auth_router
from .models.scraper import scrape_viticulture_data

app = FastAPI()

# Incluir o roteador de autenticação
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Viticulture API"}

@app.get("/productions", dependencies=[Depends(get_current_user)])
def get_productions():
    return scrape_viticulture_data("Produção")

@app.get("/processings", dependencies=[Depends(get_current_user)])
def get_processings():
    return scrape_viticulture_data("Processamento")

@app.get("/commercializations", dependencies=[Depends(get_current_user)])
def get_commercializations():
    return scrape_viticulture_data("Comercialização")

@app.get("/imports", dependencies=[Depends(get_current_user)])
def get_imports():
    return scrape_viticulture_data("Importação")

@app.get("/exports", dependencies=[Depends(get_current_user)])
def get_exports():
    return scrape_viticulture_data("Exportação")
