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