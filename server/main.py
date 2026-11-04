from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response
import numpy as np
from PIL import Image
import io
import asyncio
from concurrent.futures import ProcessPoolExecutor

from image_math import laplace_filter, gaussian_blur, sobbel_detection

app = FastAPI()

proc_pool = ProcessPoolExecutor()

@app.post("/process")
async def process_image(file: UploadFile = File(...), filter_type: str = Form(...)):
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes)).convert('L')
    img_matrix = np.array(img)

    if filter_type == "laplace":
        func = laplace_filter
    elif filter_type == "gaussian":
        func = gaussian_blur
    elif filter_type == "sobel":
        func = sobbel_detection
    else:
        return Response(content="Invalid filter", status_code=400)

    loop = asyncio.get_event_loop()
    result_matrix = await loop.run_in_executor(proc_pool,func,img_matrix)

    result_img = Image.fromarray(result_matrix)
    buf = io.BytesIO()
    result_img.save(buf,format="JPEG")

    return Response(content=buf.getvalue(), media_type="image/jpeg")

