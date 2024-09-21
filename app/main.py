from fastapi import FastAPI

from app.routers.v1.lamina_engineering_constants import router as lamina_engineering_constants_router_v1
from app.routers.v1.laminate_plate_properties import router as laminate_plate_properties_router_v1
from app.routers.v1.laminate_3d_properties import router as laminate_3d_properties_router_v1
from app.routers.v1.UDFRC_properties import router as udfrc_properties_router_v1

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello SwiftComp API"}

app.include_router(lamina_engineering_constants_router_v1, prefix="/api/v1")
app.include_router(laminate_plate_properties_router_v1, prefix="/api/v1")
app.include_router(laminate_3d_properties_router_v1, prefix="/api/v1")
app.include_router(udfrc_properties_router_v1, prefix="/api/v1")