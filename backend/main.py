from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/stores/{name}")
def create_store(name: str):
    subprocess.run(["kubectl", "create", "namespace", name])
    subprocess.run(["helm", "install", name, "bitnami/wordpress", "-n", name])
    return {"message": f"{name} provisioning started"}


@app.delete("/stores/{name}")
def delete_store(name: str):
    subprocess.run(["helm", "uninstall", name, "-n", name])
    subprocess.run(["kubectl", "delete", "namespace", name])
    return {"message": f"{name} deleted"}
