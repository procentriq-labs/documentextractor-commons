FROM python:3.12-slim

# Set working directory
WORKDIR /build

# Install build tools
RUN pip install --upgrade build wheel

# Copy source
COPY . .

# Build the wheel
RUN python -m build --wheel --outdir dist