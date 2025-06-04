FROM python:3.12-slim

# Set working directory
WORKDIR /build

# Install build tool
RUN pip install --upgrade build wheel

# Copy only the necessary files to build the package
COPY . /build

# Build the wheel at runtime
ENTRYPOINT ["python", "-m", "build", "--wheel", "--outdir", "/build/dist"]