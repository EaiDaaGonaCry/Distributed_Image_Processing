# Distributed Image Processing Server

A high-performance, Client-Server architecture for parallel image processing, developed for the Network Programming course at FMI[cite: 1]. The system applies mathematical matrix transformations to images using numerical approximations of derivatives[cite: 2].

## Architecture & Technologies
- **Network Layer:** Asynchronous I/O using FastAPI and `asyncio` to implement the Reactor Pattern[cite: 1, 4].
- **Parallel Processing:** Utilizes `concurrent.futures.ProcessPoolExecutor` to distribute heavy CPU-bound matrix calculations across multiple CPU cores, effectively bypassing the Python Global Interpreter Lock (GIL)[cite: 4].
- **Algorithms:** Built with `NumPy` and `SciPy` for applying Laplace filters, Gaussian blur, and Sobel edge detection[cite: 2].

## Features
- **Non-blocking I/O:** The server remains responsive to new network requests while processing heavy images in the background[cite: 4].
- **Thread-safe & Race-condition free:** Processes isolated memory spaces to prevent shared state issues[cite: 3].
- **Scalability:** Designed to allow performance speedup measurements (Amdahl's law) by testing with N={1, 2, 4, 8} processes[cite: 3].

## Project Structure
- `/server`: Contains the FastAPI application (`main.py`) and the numerical processing logic (`image_math.py`).
- `/tests`: Includes Pytest suites for automated verification of matrix transformations.
- `/client`: (Upcoming) Asynchronous client for submitting image processing requests.
